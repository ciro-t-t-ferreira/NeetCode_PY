"""
source: https://leetcode.com/problems/top-k-frequent-elements/description/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

def removeDuplicates(nums):
    distinctNums = []

    for n in nums:
        if n not in distinctNums:
            distinctNums.append(n)

    return distinctNums

def frequencyOfElements(nums):
    distinctNums = removeDuplicates(nums)    
    frequencyList = []
    for i in distinctNums:
        ocurrencesOfI = 0
        for j in nums:
            if i == j:
                ocurrencesOfI = ocurrencesOfI + 1
        frequencyList.append((i, ocurrencesOfI))  
    return frequencyList

def topKFrequent(nums, k):
    kMostFrequent = []
    frequencyList = frequencyOfElements(nums)
    sorted_list = sorted(frequencyList, key=lambda x: x[1], reverse=True)
    for i in range(k):
        kMostFrequent.append(sorted_list[i][0])
    return kMostFrequent


examples = [[[1,1,1,2,2,3], 2],[[1],1]]

for e in examples:
    print(topKFrequent(e[0], e[1]))