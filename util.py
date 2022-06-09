import re


def isMatch(pattern, string:str):
    string = str(string)
    if re.match(pattern, string) is None:
        return False
    else:
        return True


def lenInRange(min, max, string:str):
    l = len(str(string))
    if l >= min and l <= max:
        return True
    else:
        return False