import re
from typing import List, Dict

from definitions.common.Component import Component
from definitions.common.CustomReq import CustomReq
from definitions.questdef.CustomQuest import CustomQuest
from definitions.questdef.DialogueLine import DialogueLine
from definitions.questdef.ItemQuest import ItemQuest
from definitions.questdef.Npc import Npc
from helpers.HelperFunctions import formatStr, replaceUnderscores, strToArray, camelCaseToTitle
from repositories.master.Repository import Repository
from repositories.npc.NpcHeadRepo import NpcHeadRepo
from repositories.npc.QuestNameRepo import QuestNameRepo


class NpcRepo(Repository[Npc]):
	questToName: Dict[str, str] = {}

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
				currentNpc = Npc(
					head = NpcHeadRepo.get(npcName),
					dialogue = [],
					quests = {}
				)
				for j in range(1, len(quests), 2):
					temp = {"Type": quests[j]}
					if data := re.split(reQData, quests[j + 1]):
						for k in range(1, len(data), 2):
							atr = formatStr(data[k])
							val = formatStr(data[k + 1], ['"', ",})", " })", ";"])
							val = strToArray(val) if "[" in val else formatStr(val, [","], replaceUnderscores = True)
							temp[atr] = val
					if qName := QuestNameRepo.get(f"{npcName}{j // 2}"):
						temp["Difficulty"] = qName.difficulty
						temp["Name"] = qName.name
						if quests[j] != "None":
							cls.questToName[temp["QuestName"]] = qName.name
					cls.formatRewards(temp)
					if quests[j] == "Custom":
						cls.addCustomQuest(currentNpc, temp)
					elif quests[j] == "ItemsAndSpaceRequired":
						cls.addItemQuest(currentNpc, temp)
					else:
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
		if rew := temp.get("Rewards"):
			questRew = []
			for k in range(0, len(rew), 2):
				questRew.append(Component(
					item = rew[k],
					quantity = rew[k + 1]
				))
			temp["Rewards"] = questRew.copy()

	@classmethod
	def getQuestByName(cls, name: str) -> str:
		return cls.questToName.get(name)

	@classmethod
	def _writeChangelogChange(cls, item, change) -> str:
		def head(v: str) -> str:
			return "{{patchnote/head|changed=" + v + "}}\n"

		def bold(v: str) -> str:
			return "{{patchnote/bold|" + v + "}}\n"

		def patchnote(v: str, o, n) -> str:
			return "{{patchnote|" + f"{v}|{str(o)}|{str(n)}" + "}}\n"

		res = head(cls.getWikiName(item))
		for v, d in change.items():
			if isinstance(d, tuple):
				o, n = d
				res += patchnote(v, o, n)
			elif isinstance(d, list):
				res += bold(camelCaseToTitle(v))
				for i, subC in enumerate(d):
					o, n = subC
					res += patchnote(str(i), o, n)
			elif isinstance(d, dict):
				for quest, subC in d.items():
					res += bold(camelCaseToTitle(quest))
					for atr, val in subC.items():
						o, n = val
						res += patchnote(atr, o, n)

		res += '|}\n'
		return res

	@classmethod
	def _writeChangelogNew(cls, item, change) -> str:
		def head(v: str) -> str:
			return "{{patchnote/head|changed=" + v + "}}\n"

		def bold(v: str) -> str:
			return "{{patchnote/bold|" + v + "}}\n"

		def italic(v: str) -> str:
			return "{{patchnote/italic|" + v + "}}\n"

		def patchnote(v: str, o, n) -> str:
			return "{{patchnote|" + f"{v}|{str(o)}|{str(n)}" + "}}\n"

		res = head(cls.getWikiName(item))
		for v, d in change.items():
			if isinstance(d, list):
				res += bold(camelCaseToTitle(v))
				for i, subC in enumerate(d):
					res += patchnote(str(i), " ", subC)
			elif isinstance(d, dict):
				for quest, subC in d.items():
					res += bold(camelCaseToTitle(quest))
					for atr, val in subC.items():
						if isinstance(val, list):
							res += italic(camelCaseToTitle(atr))
							for n, subV in enumerate(val):
								res += patchnote(str(n), " ", subV)
							continue
						res += patchnote(atr, " ", val)
			else:
				if not d:
					continue
				res += patchnote(v, " ", d)
		res += '|}\n'
		return res
