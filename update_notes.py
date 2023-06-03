from helpers.CodeReader import IdleonReader
from repositories.item.sources.ItemNoteRepo import ItemNoteRepo

idleonReader = IdleonReader("184", steam = True)
codeReader = idleonReader.codeReader

# NpcHeadRepo.initialise(codeReader, True)
# EnemyNoteRepo.initialise(codeReader, True)
# NpcNoteRepo.initialise(codeReader, True)
ItemNoteRepo.initialise(codeReader, True)
