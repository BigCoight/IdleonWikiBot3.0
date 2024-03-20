from helpers.CodeReader import IdleonReader
from repositories.npc.NpcHeadRepo import NpcHeadRepo

idleonReader = IdleonReader("204", steam = True)
codeReader = idleonReader.codeReader

# WikiSetRepo.initialise(codeReader, True)
# ItemNoteRepo.initialise(codeReader, True)
NpcHeadRepo.initialise(codeReader, True)
# NpcNoteRepo.initialise(codeReader, True)
