"""
383. Ransom Note
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""


def can_construct(ransom_note: str, magazine: str) -> bool:
        dic = {}
        for char in magazine:
            dic[char] = dic[char]-1 if char in dic else -1
        for char in ransom_note:
            dic[char] = dic[char]+1 if char in dic else 1
            if dic[char] > 0:
                return False
        return True


if '__main__' == __name__:
    assert can_construct("a", "b") == False
    assert can_construct("aa", "ab") == False
    assert can_construct("aa", "aab") == True
    print('All tests passed!')
