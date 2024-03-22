"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def containsDuplicate(nums):
    
    result = False
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                result = True if (nums[i] == nums[j]) else result                
    return result

examples = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]

for e in examples:
    print("Does " + str(e) + " contains duplicates?: " + str(containsDuplicate(e)))