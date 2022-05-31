import re
from typing import Tuple

from helpers.ColourPrinter import printYellow


class TypeCastRemover:
	@classmethod
	def remove_type_conv(cls, file: str) -> Tuple[str, int]:
		pattern = r"(?<!\w)\(null == (\w+)\s*\?\s*0[\w\s\d:\?'\"=.\(\),&|]+?\1\)\)\)"
		pattern2 = r"null == (\w+)\s*\?\s*0[\w\s\d:\?'\"=.\(\),&|]+?\1\)\)"
		pattern3 = r"null == (\w+)\s*\|\|\s*\([\w\s\d:\?\"'=.\(\),&|]+\1\)\)\)"

		parsenum = "\nfunction parseNum(num) {\n  let cast = function (a, b) {\n    if (null == a || a instanceof b) return a;\n    throw new Error('Cannot cast ' + String(a) + ' to ' + String(b));\n  }\n  return null == num ? 0\n    : 'number' == typeof num ? cast(num, Number)\n      : 'number' == typeof num && (num | 0) === num ? cast(num, {}) :\n        'boolean' == typeof num ? cast(num, Boolean) ? 1 : 0\n          : 'string' == typeof num ? parseFloat(num) : parseFloat(f.string(num))\n}"
		conv = re.compile(pattern)
		conv2 = re.compile(pattern2)
		conv3 = re.compile(pattern3)

		removeNullCheck = r"\(null != .*? (.\.getReserved\(\"?(.*?)\"?\)) : .*?\2.*?\)"
		removeNulls = r"\((\w) = null != .*? (.\.getReserved\(\"?(.*?)\"?\)) : .*?\3.*?\)"
		removeSetNullChecks = r"null != .*? (.\.setReserved\(\"?(.*?)\"?, (.*?)\)) : .*?\2 = \3\)"
		nullCheckNoBr = r"null != .*? (.\.getReserved\(\"?(.*?)\"?\)) : .*?\2"

		dnsmGet = r".\.engine\.getGameAttribute\(\"(\w+)\"\)"

		postNullConv = re.compile(r"null == \((\w+) = (.*)\)\s*[\w\s\d:\?\"'=.\(\),&|]+\1\)\)")

		dnsmGetRemove = re.compile(dnsmGet)
		nullCheckRemoveNoBr = re.compile(nullCheckNoBr)
		nullCheckRemove = re.compile(removeNullCheck)
		nullRemove = re.compile(removeNulls)
		setNullRemove = re.compile(removeSetNullChecks)
		nfile, nG = nullRemove.subn(r"(\1 = \2)", file)
		nfile, nDNSM = dnsmGetRemove.subn(r"var_\1", nfile)
		nfile, nS = setNullRemove.subn(r"\1", nfile)
		nfile, nR = nullCheckRemove.subn(r"(\1)", nfile)
		nfile, nRb = nullCheckRemoveNoBr.subn(r"\1", nfile)
		nfile, n = conv.subn(r"parseNum(\1)", nfile)
		nfile, n2 = conv2.subn(r"parseNum(\1)", nfile)
		nfile, n3 = conv3.subn(r"parseNum(\1)", nfile)
		nfile, n4 = postNullConv.subn(r"parseNum(\2)", nfile)
		nfile = nfile + parsenum
		return nfile, n + n2 + n3 + nG + nS + n4 + nR + nRb + nDNSM

	@classmethod
	def remove(cls, version: str) -> str:
		with open(f"./codefiles/idleon{version}.txt", "r") as filename:
			file = filename.read()

		nfile, n = cls.remove_type_conv(file)
		printYellow(f"Removed {n} type checks")
		with open(f"./codefiles/parsed/idleon{version}_parsed.txt", "w") as f:
			f.write(nfile)
		return nfile
