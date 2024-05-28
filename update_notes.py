from helpers.CodeReader import IdleonReader
from repositories.item.sources.ItemNoteRepo import ItemNoteRepo
from repositories.item.sources.WikiSetRepo import WikiSetRepo
from repositories.npc.NPCNoteRepo import NpcNoteRepo
from repositories.npc.NpcHeadRepo import NpcHeadRepo

idleonReader = IdleonReader("208", steam = True)
codeReader = idleonReader.codeReader

WikiSetRepo.initialise(codeReader, True)
ItemNoteRepo.initialise(codeReader, True)
NpcHeadRepo.initialise(codeReader, True)
NpcNoteRepo.initialise(codeReader, True)
