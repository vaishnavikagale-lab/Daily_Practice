def areAnagrams(s1, s2):
    if sorted(s1.lower()) == sorted(s2.lower()):
        return True
    else:
        return False
s1 = input()
s2 = input()

if areAnagrams(s1,s2):
    print("Anagram")
else:
    print("Not anagrams")