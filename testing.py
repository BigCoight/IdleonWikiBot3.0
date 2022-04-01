from builds.Build import Build, BuildTab, BuildTalent
from helpers.CodeReader import IdleonReader
from helpers.JsonEncoder import CompactJSONEncoder
from repositories.enemies.BossDetailRepo import BossDetailRepo
from repositories.misc.ColosseumRepo import ColosseumRepo
from repositories.misc.world3.ShrineRepo import ShrineRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

newV = IdleonReader("152", True)

oldV = IdleonReader("151", True)

# SpecificItemRepo.compareVersions(oldV, newV)
ColosseumRepo.initialise(newV.codeReader)

# classes = {
# 	"Beginner": ["Beginner"],
# 	"Journeyman": ["Beginner", "Journeyman"],
# 	"Maestro": ["Beginner", "Journeyman", "Maestro"],
# 	"Virtuoso": [],
# 	"Infinilyte": [],
# 	"Warrior": ["Rage Basics", "Warrior"],
# 	"Barbarian": ["Rage Basics", "Warrior", "Barbarian"],
# 	"Squire": ["Rage Basics", "Warrior", "Squire"],
# 	"Blood_Berserker": [],
# 	"Death_Bringer": [],
# 	"Divine_Knight": [],
# 	"Royal_Guardian": [],
# 	"Archer": ["Calm Basics", "Archer"],
# 	"Bowman": ["Calm Basics", "Archer", "Bowman"],
# 	"Hunter": ["Calm Basics", "Archer", "Hunter"],
# 	"Siege Breaker": [],
# 	"Mayheim": [],
# 	"Wind_Walker": [],
# 	"Beast_Master": [],
# 	"Mage": ["Savvy Basics", "Mage"],
# 	"Shaman": ["Savvy Basics", "Mage", "Shaman"],
# 	"Wizard": ["Savvy Basics", "Mage", "Wizard"],
# 	"Elemental_Sorcerer": [],
# 	"Spiritual_Monk": [],
# 	"Bubonic_Conjuror": [],
# 	"Arcane_Cultist": [],
# }
#
# for skill_class, tabs in classes.items():
# 	neededTabs = []
# 	for tab in tabs:
# 		currentTab = []
# 		for name, talent in TalentTreeRepo.get(tab).talents.items():
# 			currentTab.append(BuildTalent(skillIndex =talent.skillIndex, level = 0, name = name, note = ""))
# 		neededTabs.append(BuildTab(name = tab, talents = currentTab.copy(), note = ""))
#
# 	testBuild = Build(
# 		title = f"{skill_class} Build (lv)",
# 		notes = "",
# 		version = "1.51",
# 		level = 0,
# 		tabs = neededTabs.copy(),
# 		idleonClass = skill_class)
#
# 	with open(f"./builds/templates/{skill_class}_template.json", 'w') as outfile:
# 		outfile.write(CompactJSONEncoder(indent = 4).encode(testBuild.toDict()))
