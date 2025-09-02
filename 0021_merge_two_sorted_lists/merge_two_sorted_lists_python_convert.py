class Solution(object):
    def mergeTwoLists(self, list1, list2):
        values = []
        while list1:
            values.append(list1.val)
            list1 = list1.next
        while list2:
            values.append(list2.val)
            list2 = list2.next
        values.sort()

        dummy = ListNode()
        current = dummy
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next