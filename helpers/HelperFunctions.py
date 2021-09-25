import re
from typing import List


def getFromSplitArray(v: str) -> List[List[str]]:
    """
    Converts a section into a list of strings based upon the exportation of an array represented as
    "0 1 2 3 4 5 6 7 8 9".split(" ")
    Args:
        v:

    Returns:

    """
    section = formatStr(v, ["  ", "\n"])
    subSections = re.findall(
        r'"([ a-zA-Z0-_\'n()@,!$+{}%:.]*)"\.', section)
    subSections = [x.split(" ") for x in subSections]
    newList = []
    for subSection in subSections:
        internalList = []
        for i in range(len(subSection)):
            internalList.append(replaceUnderscores(subSection[i]))
        newList.append(internalList[:])
    return newList


def getFromArrayArray(v: str) -> List[List[str]]:
    """
    Converts a string representation of a 2d array into an actual 2d array
    Args:
        v:

    Returns:

    """
    section = formatStr(v, ["  ", "\n"])
    subSections = section.split("],[")
    return [strToArray(x) for x in subSections]

def formatStr(val: str, remove: List[str] = [], replaceUnderscores: bool = False) -> str:
    """Formats the given string by first stripping the left and right, then removes all occurrences of all strings
        inside the remove list and finally replaces underscores with a space

    Args:
        val (str): [The string to be formatted]
        remove (List[str], optional): [A list of substrings to be removed from the input string]. Defaults to [].
        replaceUnderscores (bool, optional): [Whether to replace underscores with spaces]. Defaults to False.

    Returns:
        str: [The formatted string]
    """
    if val:
        for rep in remove:
            val = val.replace(rep, "")
        if replaceUnderscores:
            val = val.replace("_", " ")
            if val[0] != "|":
                val = val.replace("|", " ")
        return val.lstrip().rstrip()
    return val


def scientificToInt(val: str) -> int:
    """Converts a string reprisenting an integer in scientific notion to the corresponding integer

    Eg: scientificToInt("4e2") = "400"

    Args:
        val (str): the string to convert

    Returns:
        int: the resulting integer
    """
    if "e" in val:
        return int(float(val))
    return int(val)


def replaceUnderscores(val: str) -> str:
    return formatStr(val, replaceUnderscores=True)


def wrap(v: str) -> str:
    return f"[[{v}]]"


def strToArray(v: str) -> List[str]:
    """
    Converts a string reprisentation of a list to an actual python list
    strToArray("[1,2,3,4]") = ["1", "2", "3", "4"]
    Args:
        v: [str] the string to convert

    Returns:
        the resulting list

    """
    string = v.replace(",_", "&&&&")
    parts = formatStr(string, ["[", "]", '"', "return", ";", "\n", "{", "}"]).split(",")
    return [formatStr(x).replace("&&&&", ", ") for x in parts]
