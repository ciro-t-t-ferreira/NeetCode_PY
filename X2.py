"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

def remove_first_instance(array, element):
    if element in array:
        index = array.index(element)
        del array[index]
    return array

def isAnagram(s, t):
    result = False

    word = list(s)
    anagram = list(t)

    wordcopy = list(s)
    anagramcopy = list(t)

    for wletter in wordcopy:
        for aletter in anagramcopy:
            if wletter == aletter:
                word = remove_first_instance(word, wletter)
                anagram = remove_first_instance(anagram, aletter)
    if (word == [] and anagram == []):
        result = True

    return result

examples = [["anagram","nagaram"],["rat","car"]]

for e in examples:
    print("Is " + str(e[1]) + " an anagram of " + str(e[0]) + "?: " + str(isAnagram(e[0], e[1])))