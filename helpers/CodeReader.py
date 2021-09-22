import re
from typing import Dict, List, Optional


class Section:
    def __init__(self, start: str, end: str, sectionName: str) -> None:
        self.start = start
        self.end = end
        self.between = ""
        self.sectionName = sectionName


class CodeReader:
    def __init__(self, codefile: str) -> None:
        self.codefile = codefile
        self.currentSection: Optional[Section] = None
        self.sections: List[Section] = []
        self.sectionResults: Dict[str, str] = {}

    def addSection(self, start: str, end: str, sectionName: str) -> None:
        self.sections.append(Section(start, end, sectionName))

    def readCode(self) -> None:
        with open(self.codefile, mode="r") as infile:
            lines = infile.read()
            for section in self.sections:
                escapedStart = re.escape(section.start)
                escapedEnd = re.escape(section.end)
                regex = re.compile(rf"(?s){escapedStart}(.*?){escapedEnd}")
                self.sectionResults[section.sectionName] = regex.findall(lines)[
                    0]

    def getSection(self, sectionName: str) -> Optional[str]:
        return self.sectionResults.get(sectionName)
