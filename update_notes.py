from helpers.CodeReader import IdleonReader
from repositories.npc.NpcHeadRepo import NpcHeadRepo

idleonReader = IdleonReader("180", steam=True)
codeReader = idleonReader.codeReader

# EnemyNoteRepo.initialise(codeReader, True)
# ItemNoteRepo.initialise(codeReader, True)
# NpcNoteRepo.initialise(codeReader, True)
NpcHeadRepo.initialise(codeReader, True)
