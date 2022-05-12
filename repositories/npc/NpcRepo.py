import re
from typing import List, Dict, Set

from definitions.common.Component import Component
from definitions.common.CustomReq import CustomReq
from definitions.common.ExpType import ExpType
from definitions.questdef.CustomQuest import CustomQuest
from definitions.questdef.DialogueLine import DialogueLine
from definitions.questdef.ItemQuest import ItemQuest
from definitions.questdef.Npc import Npc
from definitions.questdef.Quest import ExpReward, CoinReward, RecipeReward, TalentReward
from helpers.CodeReader import IdleonReader
from helpers.Constants import Constants
from helpers.HelperFunctions import formatStr, replaceUnderscores, strToArray, isRecipe, isTalent
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.Repository import Repository
from repositories.npc.NPCNoteRepo import NpcNoteRepo
from repositories.npc.NpcHeadRepo import NpcHeadRepo
from repositories.npc.QuestNameRepo import QuestNameRepo


class NpcRepo(Repository[Npc]):
	questToName: Dict[str, str] = {}

	@classmethod
	def getCategory(cls) -> str:
		return "Npc"

	@classmethod
	def initDependencies(cls, log = True) -> None:
		NpcHeadRepo.initialise(cls.codeReader)
		QuestNameRepo.initialise(cls.codeReader, log)
		NpcNoteRepo.initialise(cls.codeReader)
		ItemDetailRepo.initialise(cls.codeReader, log)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Quests"]

	@classmethod
	def generateRepo(cls) -> None:
		reNpcs = r'..\.addDialogueFor\("([a-zA-Z0-9_]*)", [^\s"]*\)'
		reQuest = r"\.addLine_([a-zA-Z]*)\({"
		reQData = r" ?,?([a-zA-Z]*): "
		questText = formatStr(cls.getSection(), ["\n"])
		questData = re.split(reNpcs, questText)

		for i in range(1, len(questData), 2):
			if quests := re.split(reQuest, questData[i + 1]):
				npcName = replaceUnderscores(questData[i])
				npcName = Constants.nameConflicts.get(npcName, npcName)
				currentNpc = Npc(
					head = NpcHeadRepo.getHead(npcName),
					dialogue = [],
					quests = {}
				)
				for j in range(1, len(quests), 2):
					temp = {"Type": quests[j]}
					if data := re.split(reQData, quests[j + 1]):
						for k in range(1, len(data), 2):
							atr = formatStr(data[k])
							val = formatStr(data[k + 1], ['"', ",})", " })", ";"]).replace("@", "<br>")
							val = strToArray(val) if "[" in val else formatStr(val, [","], replaceUnderscores = True)
							temp[atr] = val
					if qName := QuestNameRepo.get(f"{npcName}{j // 2}"):
						temp["Difficulty"] = qName.difficulty
						temp["Name"] = qName.name
						if quests[j] != "None":
							cls.questToName[temp["QuestName"]] = qName.name
							temp["note"] = NpcNoteRepo.getNote(npcName, qName.name)
					cls.formatRewards(temp)
					if quests[j] == "Custom":
						cls.addCustomQuest(currentNpc, temp)
					elif quests[j] == "ItemsAndSpaceRequired":
						cls.addItemQuest(currentNpc, temp)

					currentNpc.dialogue.append(DialogueLine.parse_obj(temp))

				cls.add(npcName, currentNpc)

	@classmethod
	def addItemQuest(cls, currentNpc, temp):
		itemReqs = []
		items = temp.get("ItemTypeReq")
		quants = temp.get("ItemNumReq")
		for item, quant in zip(items, quants):
			itemReqs.append(Component(
				item = item,
				quantity = quant
			))
		temp["ItemReq"] = itemReqs.copy()
		currentNpc.quests[temp.get("Name", "Filler")] = (ItemQuest.parse_obj(temp))

	@classmethod
	def addCustomQuest(cls, currentNpc, temp):
		customReqs = []
		reqs = temp["CustomArray"]
		for k in range(0, len(reqs), 4):
			customReqs.append(CustomReq(
				desc = replaceUnderscores(reqs[k]),
				finalV = reqs[k + 1],
				type = reqs[k + 2],
				startV = reqs[k + 3]
			))
		temp["CustomArray"] = customReqs.copy()
		currentNpc.quests[temp.get("Name", "Filler")] = (CustomQuest.parse_obj(temp))

	@classmethod
	def formatRewards(cls, temp):
		if "Rewards" not in temp:
			return
		rew = temp.get("Rewards")
		questRew = []
		for k in range(0, len(rew), 2):
			if "Experience" == rew[k][:10]:
				questRew.append(ExpReward(
					type = ExpType(int(rew[k][10:])),
					amount = rew[k + 1]
				))
				continue
			if "COIN" in rew[k]:
				questRew.append(CoinReward(
					coins = rew[k + 1],
				))
				continue
			if isRecipe(rew[k]):
				questRew.append(RecipeReward(
					item = rew[k],
					quantity = rew[k + 1]
				))
				continue
			if isTalent(rew[k]):
				questRew.append(TalentReward(
					item = rew[k],
					quantity = rew[k + 1]
				))
				continue
			questRew.append(Component(
				item = rew[k],
				quantity = rew[k + 1]
			))
		temp["Rewards"] = questRew.copy()

	@classmethod
	def getQuestByName(cls, name: str) -> str:
		name = replaceUnderscores(name)
		return cls.questToName.get(name)

	@classmethod
	def isQuestName(cls, name: str) -> bool:
		name = replaceUnderscores(name)
		return name in cls.questToName

	@classmethod
	def compareVersions(cls, v1: IdleonReader, v2: IdleonReader, ignored: Set[str] = set(), useIgnore = True):
		return super().compareVersions(v1, v2, ignored = {"head", "QuestName", "CustomType", "note", "NextIndex",
		                                                  "dialogue", "NoSpaceIndex"})

	@classmethod
	def _ignore(cls, name: str, data: Npc) -> bool:
		if name in {"FillerNPC", "Game Message", "Unmade Character", "Omar Da Ogar", "Mecha Pete"}:
			return True
		return False
