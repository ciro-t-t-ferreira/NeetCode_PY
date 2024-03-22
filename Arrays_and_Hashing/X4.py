"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
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

def alreadyInResult(element, anagrams):
    result = False
    for anagramGroup in anagrams:
        if element in anagramGroup:
            result = True
    return result

def groupAnagrams(strings):
    result = []
    for i in range(len(strings)):
        anagramGroup = []

        for j in range(i, len(strings)):

            if isAnagram(strings[i],strings[j]) and not alreadyInResult(strings[j], result):
                anagramGroup.append(strings[j])        

        if len(anagramGroup) != 0:
            result.append(anagramGroup)
    return result

examples = [["eat","tea","tan","ate","nat","bat"], [""], ["a"]]

for e in examples:
    print(groupAnagrams(e))