import re
from random import choice, randint
from typing import List, Dict, Optional

from mwparserfromhell import parse as mwparse
from pywikibot import Site, Page

from definitions.questdef.NpcHead import NpcHead
from helpers.Constants import Constants
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import formatStr, replaceUnderscores
from repositories.master.FileRepository import FileRepository
from repositories.misc.RandoListRepo import RandoListRepo, RandoListDescriptions


class NpcHeadRepo(FileRepository[NpcHead]):
	@classmethod
	def getCategory(cls) -> str:
		return "Npc"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> NpcHead:
		return NpcHead.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Quests", "Quests2"]

	@classmethod
	def initDependencies(cls, log = True) -> None:
		RandoListRepo.initialise(cls.codeReader, False)

	@classmethod
	def generateRepo(cls) -> None:
		website = Site()
		reNpcs = r'..\.addDialogueFor\("([a-zA-Z0-9_]*)", [^\s"]*\)'

		for n in range(len(cls.getSections())):
			questText = formatStr(cls.getSection(n), ["\n"])
			questData = re.split(reNpcs, questText)
			for i in range(1, len(questData), 2):
				npcName = replaceUnderscores(questData[i])
				npcName = Constants.nameConflicts.get(npcName, npcName)
				cls.add(npcName, cls.getHead(website, npcName, questData[i]))

	@classmethod
	def getHead(cls, website: Site, dispName: str, rawName: str) -> NpcHead:
		if dispName in ["", " "]: return {}
		text = Page(website, dispName).text
		replacedText = text.replace("\n", Constants.newLineRep)
		wikiCode = mwparse(replacedText)
		templates = wikiCode.filter_templates(recursive = False)
		selectedTemplate = None
		for template in templates:
			if "world" in template:
				selectedTemplate = template
				break
		codeWorld = cls.getWorld(rawName)
		if selectedTemplate is None:
			if codeWorld:
				return cls.newHead(world = codeWorld)
			return cls.newHead()
		typ = ""
		if "npcType" in selectedTemplate:
			if codeWorld:
				typ = ""
			typ = cls.getParsed(selectedTemplate, "npcType")
		notes = " "
		if "notes" in selectedTemplate:
			notes = re.escape(cls.getParsed(selectedTemplate, "notes")).replace('"', "'")
		return NpcHead(
			location = cls.getParsed(selectedTemplate, "location"),
			world = codeWorld if codeWorld else cls.getParsed(selectedTemplate, "world"),
			noQuest = cls.getParsed(selectedTemplate, "noquest"),
			type = typ,
			birthWeight = cls.getParsed(selectedTemplate, "birthweight"),
			starSign = cls.getParsed(selectedTemplate, "starsign"),
			mothersMaidenName = cls.getParsed(selectedTemplate, "mmm"),
			notes = notes
		)

	@classmethod
	def getWorld(cls, rawName: str) -> str:
		npcInWorld = [
			RandoListRepo.get(RandoListDescriptions.npcsInBlunder).elements,
			RandoListRepo.get(RandoListDescriptions.npcsInYumyum).elements,
			RandoListRepo.get(RandoListDescriptions.npcsInFrostbite).elements,
			RandoListRepo.get(RandoListDescriptions.npcsInNebulon).elements,
			RandoListRepo.get(RandoListDescriptions.npcsInSmolderin).elements
		]
		for worldIndex, worldList in enumerate(npcInWorld):
			if rawName in worldList:
				return Constants.worlds[worldIndex]
		return ""

	@classmethod
	def newHead(cls, world: str = "Unknown", noQuest: Integer = 0):
		return NpcHead(
			location = "Unknown",
			world = world,
			noQuest = noQuest,
			repeatable = "Unknown",
			type = "Unknown",
			birthWeight = cls.doBirthweight(),
			starSign = cls.doStarsign(),
			mothersMaidenName = cls.doMMM(),
			notes = " "
		)

	@classmethod
	def get(cls, key: str) -> Optional[NpcHead]:
		if cls.contains(key):
			return super().get(key)
		return cls.newHead()

	@classmethod
	def doStarsign(cls):
		return choice(
			["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn",
			 "Aquarius", "Pisces"])

	@classmethod
	def doMMM(cls):
		return choice(
			[
				"Anderson",
				"Ashwoon",
				"Aikin",
				"Bateman",
				"Bongard",
				"Bowers",
				"Boyd",
				"Cannon",
				"Cast",
				"Deitz",
				"Dewalt",
				"Ebner",
				"Frick",
				"Hancock",
				"Haworth",
				"Hesch",
				"Hoffman",
				"Kassing",
				"Knutson",
				"Lawless",
				"Lawicki",
				"Mccord",
				"McCormack",
				"Miller",
				"Myers",
				"Nugent",
				"Ortiz",
				"Orwig",
				"Ory",
				"Paiser",
				"Pak",
				"Pettigrew",
				"Quinn",
				"Quizoz",
				"Ramachandran",
				"Resnick",
				"Sagar",
				"Schickowski",
				"Schiebel",
				"Sellon",
				"Severson",
				"Shaffer",
				"Solberg",
				"Soloman",
				"Sonderling",
				"Soukup",
				"Soulis",
				"Stahl",
				"Sweeney",
				"Tandy",
				"Trebil",
				"Trusela",
				"Trussel",
				"Turco",
				"Uddin",
				"Uflan",
				"Ulrich",
				"Upson",
				"Vader",
				"Vail",
				"Valente",
				"Van Zandt",
				"Vanderpoel",
				"Ventotla",
				"Vogal",
				"Wagle",
				"Wagner",
				"Wakefield",
				"Weinstein",
				"Weiss",
				"Woo",
				"Yang",
				"Yates",
				"Yocum",
				"Zeaser",
				"Zeller",
				"Ziegler",
				"Bauer",
				"Baxster",
				"Casal",
				"Cataldi",
				"Caswell",
				"Celedon",
				"Chambers",
				"Chapman",
				"Christensen",
				"Darnell",
				"Davidson",
				"Davis",
				"DeLorenzo",
				"Dinkins",
				"Doran",
				"Dugelman",
				"Dugan",
				"Duffman",
				"Eastman",
				"Ferro",
				"Ferry",
				"Fletcher",
				"Fietzer",
				"Hylan",
				"Hydinger",
				"Illingsworth",
				"Ingram",
				"Irwin",
				"Jagtap",
				"Jenson",
				"Johnson",
				"Johnsen",
				"Jones",
				"Jurgenson",
				"Kalleg",
				"Kaskel",
				"Keller",
				"Leisinger",
				"LePage",
				"Lewis",
				"Linde",
				"Lulloff",
				"Maki",
				"Martin",
				"McGinnis",
				"Mills",
				"Moody",
				"Moore",
				"Napier",
				"Nelson",
				"Norquist",
				"Nuttle",
				"Olson",
				"Ostrander",
				"Reamer",
				"Reardon",
				"Reyes",
				"Rice",
				"Ripka",
				"Roberts",
				"Rogers",
				"Root",
				"Sandstrom",
				"Sawyer",
				"Schlicht",
				"Schmitt",
				"Schwager",
				"Schutz",
				"Schuster",
				"Tapia",
				"Thompson",
				"Tiernan",
				"Tisler",
			]
		)

	@classmethod
	def doBirthweight(cls):
		return randint(100, 1000) / 100
