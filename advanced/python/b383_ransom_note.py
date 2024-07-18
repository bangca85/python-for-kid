'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''
from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_counter = Counter(ransomNote)
    magazine_counter = Counter(magazine)
    print(ransom_counter, magazine_counter)
    for char, count in ransom_counter.items():
        if magazine_counter[char] < count:
            return False
    
    return True

def canConstruct2(ransomNote: str, magazine: str) -> bool:
    # Create a dictionary to count the frequency of each character in the magazine
    magazine_count = {}
    
    for char in magazine:
        if char in magazine_count:
            magazine_count[char] += 1
        else:
            magazine_count[char] = 1
    
    # Check if ransomNote can be constructed
    for char in ransomNote:
        if char not in magazine_count or magazine_count[char] == 0:
            return False
        magazine_count[char] -= 1
    
    return True
# Example usage:
print(canConstruct2("a", "b"))     
print(canConstruct2("aa", "ab"))    
print(canConstruct2("aa", "aab"))   

# 