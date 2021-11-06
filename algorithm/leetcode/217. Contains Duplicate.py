from typing import List

class Solution:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    Input  - int array
    Output -  nums 배열안에 duplicate이 있는지 없는지를 나타내는 boolean(있으면 true, else false)
    Constraints - 1 <= nums.length <= 10^5
                -109 <= nums[i] <= 109

    ds -> Set

        case 1 : int arr -> if len = 5 -> [1,2,3,4,5] -> set[int arr]-> [1,2,3,4,5] -> len(set) = 5 
        case 2 : int arr-> if len = 4 -> [1,2,1,4] - >  set[int arr]  -> set = [1,2,4] -> len(set) = 3
        int arr, set 길이비교 같으면 중복 x  같지x - > 중복된 값이있다.
    
    시간복잡도 -> o(n)
    n-> 공간복잡도 o(n), n 기준 정하기, 영향을 받는가에 따라
    """  

    def containsDuplicate(self, nums: List[int]) -> bool:
        
        l = len(nums)

        sl = len(set(nums))

        return sl != l


s = Solution()

print(s.containsDuplicate([1,2,3,4,5]))
    

    
    