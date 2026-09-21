# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums=[]
        current=head
        while current:
            nums.append(current.val)
            current=current.next
            
        st,end=0,len(nums)-1
        summ,ans=0,0

        while st<end:
            summ=nums[st]+nums[end]
            st+=1
            end-=1

            ans=max(ans,summ)

        return ans