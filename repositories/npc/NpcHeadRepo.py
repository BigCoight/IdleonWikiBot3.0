import re
from random import choice, randint
from typing import List, Dict

from pywikibot import Site, Page

from definitions.questdef.NpcHead import NpcHead
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import formatStr, replaceUnderscores
from repositories.master.FileRepository import FileRepository


class NpcHeadRepo(FileRepository[NpcHead]):

	@classmethod
	def parse(cls, value: Dict[str, any]) -> NpcHead:
		return NpcHead.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Quests"]

	@classmethod
	def generateRepo(cls) -> None:
		website = Site()
		reNpcs = r'..\.addDialogueFor\("([a-zA-Z0-9_]*)", [^\s"]*\)'
		questText = formatStr(cls.getSection(), ["\n"])
		questData = re.split(reNpcs, questText)
		for i in range(1, len(questData), 2):
			npcName = replaceUnderscores(questData[i])
			if head := cls.searchHead(website, npcName):
				cls.add(npcName, cls.parseHead(head))
				continue
			cls.add(npcName, cls.newHead())

	@classmethod
	def searchHead(cls, website: Site, siteName: str) -> str:
		if siteName not in ["", " "]:
			toSplit = "{{Quest/head}}"
			page = Page(website, siteName)
			splitText = page.text.split(toSplit)
			if len(splitText) > 1:
				searchText = page.text.split(toSplit)[0]
				return searchText
		return ""

	@classmethod
	def parseHead(cls, head: str) -> NpcHead:
		paresedHead = {}
		parts = re.findall(r"(\w*)=(.*)", head)
		for atr, val in parts:
			paresedHead[atr] = val
		return NpcHead(
			location =paresedHead.get("location", ""),
			world =paresedHead.get("world", ""),
			noQuest = paresedHead.get("noquest", 0),
			repeatable =paresedHead.get("repeatable", ""),
			birthWeight =paresedHead.get("birthweight", 0),
			starSign =paresedHead.get("starsign", ""),
			mothersMaidenName =paresedHead.get("mmm", ""),
			notes = paresedHead.get("notes", "").replace('"', r"'")
		)

	@classmethod
	def newHead(cls):
		return NpcHead(
		location = "Unknown",
		world ="Unknown",
		noQuest = Integer(0),
		repeatable ="Unknown",
		birthWeight =cls.doBirthweight(),
		starSign =cls.doStarsign(),
		mothersMaidenName =cls.doMMM(),
		notes = ""
	)

	@classmethod
	def doStarsign(cls):
	    return choice(["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])

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






