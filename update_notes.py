from helpers.CodeReader import IdleonReader
from repositories.enemies.EnemyNoteRepo import EnemyNoteRepo
from repositories.item.sources.ItemNoteRepo import ItemNoteRepo
from repositories.npc.NPCNoteRepo import NpcNoteRepo
from repositories.npc.NpcHeadRepo import NpcHeadRepo

idleonReader = IdleonReader("157", steam = True)
codeReader = idleonReader.codeReader

EnemyNoteRepo.initialise(codeReader, True)
ItemNoteRepo.initialise(codeReader, True)
NpcNoteRepo.initialise(codeReader, True)
NpcHeadRepo.initialise(codeReader, True)
