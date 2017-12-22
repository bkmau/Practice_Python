'''
Given an array of integers, return indices of the two numbers

such that they add up to a specific target.

You may assume that each input would have exactly one solution,

and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].

'''

import unittest

class Solution:
    def two_sum(self, nums, target):
        test = target
        for i in range(len(nums)):
            test -= nums[i]
            for index, n in enumerate(nums[i + 1:]):
                if (test - n) == 0:
                    return [i, (index + i + 1)]
            test = target

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_none_result(self):
        self.assertIsNone(self.sol.two_sum([], 1))
        self.assertIsNone(self.sol.two_sum([1], 1))
        self.assertIsNone(self.sol.two_sum([1, 2], 1))

    def test_found_1(self):
        self.assertEqual(self.sol.two_sum([1, 1], 2), [0, 1])
        self.assertEqual(self.sol.two_sum([9, 1, 17], 26), [0, 2])
        self.assertEqual(self.sol.two_sum([1, 5, 7, 9], 10), [0, 3])
        self.assertEqual(self.sol.two_sum([1, 5, 7, 9], 12), [1, 2])
        self.assertEqual(self.sol.two_sum([9, 17, 1], 26), [0, 1])

    def test_found_2(self):
        self.assertEqual(self.sol.two_sum([1, -9], -8), [0, 1])
        self.assertEqual(self.sol.two_sum([1, -5, 7, 9], 2), [1, 2])
        self.assertEqual(self.sol.two_sum([1, 5, -7, -9], -16), [2, 3])


if __name__ == '__main__':
    unittest.main()