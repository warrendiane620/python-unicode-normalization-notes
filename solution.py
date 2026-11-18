import unicodedata

def solve(value):
    return unicodedata.normalize('NFC', value)
