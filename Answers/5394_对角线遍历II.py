'''
给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。

示例 1：
    输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,4,2,7,5,3,8,6,9]
示例 2：
    输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
示例 3：
    输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
    输出：[1,4,2,5,3,8,6,9,7,10,11]
示例 4：
    输入：nums = [[1,2,3,4,5,6]]
    输出：[1,2,3,4,5,6]

提示：
    1 <= nums.length <= 10^5
    1 <= nums[i].length <= 10^5
    1 <= nums[i][j] <= 10^9
    nums 中最多有 10^5 个数字。
'''

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if not (i+j) in map:
                    map[i+j] = [[i, j]]
                else:
                    map[i+j] += [[i, j]]
        res = []
        for i in map:
            map[i].sort()
            for j in map[i][::-1]:
                res.append(nums[j[0]][j[1]])
        return res