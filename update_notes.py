from helpers.CodeReader import IdleonReader
from repositories.item.sources.ItemNoteRepo import ItemNoteRepo
from repositories.item.sources.WikiSetRepo import WikiSetRepo

idleonReader = IdleonReader("188", steam = True)
codeReader = idleonReader.codeReader

WikiSetRepo.initialise(codeReader, True)
ItemNoteRepo.initialise(codeReader, True)
