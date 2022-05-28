# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(s1, s2):
    if (sorted(s1) == sorted(s2)):
            print(sorted(s1), sorted(s2))
            return True
    return False

print(find_anagram("hello", "check"))

def find_anagram(s1, s2):
    if (sorted(s1) == sorted(s2)):
            print(sorted(s1), sorted(s2))
            return True
    return False

print(find_anagram("below", "elbow"))