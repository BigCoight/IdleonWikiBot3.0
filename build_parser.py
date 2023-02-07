import json
from glob import glob

from definitions.talents.Build import Build
from helpers.CodeReader import IdleonReader
from helpers.JsonEncoder import CompactJSONEncoder
from repositories.talents.TalentTreeRepo import TalentTreeRepo

build_paths = glob("./builds/ic_builds/**/*.json", recursive = True)

idleonReader = IdleonReader("174", steam = True)
codeReader = idleonReader.codeReader
TalentTreeRepo.initialise(codeReader)

for build_path in build_paths:
	with open(build_path, 'r') as infile:
		build = json.load(infile)
	template_tabs = TalentTreeRepo.getClassTabs(build["class"])
	build_tabs = build["tabs"]
	for template_tab, build_tab in zip(template_tabs, build_tabs):
		for str_ind, lvl in build_tab["skills"].items():
			ind = int(str_ind) - 1
			if lvl.isnumeric():
				template_tab.talents[ind].level = int(lvl)
			else:
				template_tab.talents[ind].note = lvl
		template_tab.note = build_tab["comment"].replace('"', r"'")
	proper_build = Build(
		title = build["title"],
		notes = build["notes"].replace('"', r"\""),
		version = build["version"],
		level = build.get("level", 0),
		tabs = template_tabs.copy(),
		idleonClass = build["class"])
	build_out_path = build_path.replace("ic_builds", "ic_parsed")
	with open(build_out_path, mode = "w") as outfile:
		outfile.write(CompactJSONEncoder(indent = 4).encode(proper_build))
