"""
Počítání slov
Implementujte funkci word_count(s), která vrátí počet slov v daném řetězci.

"""

def word_count(s):
    i = 0
    for word in str(s).split():
        i += 1
    return i

def word_count2(s):
    return len(str(s).split())


