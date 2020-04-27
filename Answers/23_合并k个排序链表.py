'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
    输入:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    输出: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while None in lists:
            lists.remove(None)
        resNode = None
        while lists != []:
            mi = min(lists, key=lambda x:x.val)
            if resNode == None:
                resNode = mi
                p = mi
            else:
                p.next = mi
                p = p.next
            t = mi.next
            lists.remove(mi)
            if not t is None:
                lists.append(t)
        return resNode