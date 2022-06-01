from helpers.CodeReader import IdleonReader
from helpers.codesplitting.CodeSplitter import CodeSplitter
from helpers.codesplitting.TypeCastRemover import TypeCastRemover

newV = IdleonReader("157", True)
newFile = TypeCastRemover.remove(newV.version)
CodeSplitter.Split(newFile, newV.version)

newV = IdleonReader("158", True)
newFile = TypeCastRemover.remove(newV.version)
CodeSplitter.Split(newFile, newV.version)
