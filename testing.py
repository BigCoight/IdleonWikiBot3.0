from builds.Build import Build, Talent, Tab
from helpers.CodeReader import IdleonReader
from helpers.JsonEncoder import CompactJSONEncoder
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.dungeons.DungEnemyRepo import DungEnemyRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.sources.SourceRepo import SourceRepo
from repositories.npc.NpcRepo import NpcRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

newV = IdleonReader("151", True)
oldV = IdleonReader("150d", True)
# SpecificItemRepo.compareVersions(oldV, newV)
TalentTreeRepo.initialise(newV.codeReader)


warrior = ['Rage Basics', "Warrior"]

neededTabs = []
for tab in warrior:
	currentTab = {}
	for name, talent in TalentTreeRepo.get(tab).talents.items():
		currentTab[name] = Talent(level =0, note ="")
	neededTabs.append(Tab(name =tab, talents =currentTab.copy(), note =""))


testBuild = Build(
	title ="Warrior Build (lv)",
	notes ="",
	version ="1.51",
	level =50,
	tabs =neededTabs.copy(),
	idleonClass ="Warrior")

with open("./test.json", 'w') as outfile:
	outfile.write(CompactJSONEncoder(indent = 4).encode(testBuild.toDict()))
