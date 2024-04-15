"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""
# Constraints:

#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.

 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class TwoSum:
    def towsum(self, nums: list[int], traget: int) -> list[int]:
        #create a hash map(dic) for seen number
        seen = {}

        for curr_index in range(len(nums)):
            diff = traget - nums[curr_index]
            # print('curr_index = {}'.format(curr_index))
            # print('curr_int = {}, diff = {}'.format(nums[curr_index], diff))
            if diff in seen:
                return [seen[diff], curr_index]
            else:
                seen[nums[curr_index]] = curr_index
                # print('seen[{}] = {}'.format(curr_index,nums[curr_index]))
                # print()

if __name__ == "__main__":
    solution = TwoSum()
    
    #example array
    # nums = list(range(2, 105))
    nums = [2,2,3,4,5]
    traget = 6

    result = solution.towsum(nums, traget)
    ans = nums[result[0]] + nums[result[1]]

    if ans == traget:
        print('Answer is correct')
        print(result)
        print('{} => {} + {} = {}'.format(result, nums[result[0]], nums[result[1]], ans))
    else:
        print('Answer is wrong')
