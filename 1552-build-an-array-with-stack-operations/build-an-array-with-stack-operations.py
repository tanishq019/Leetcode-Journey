class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        m=len(target)
        ind,i=0,1
        ans=[]

        while ind<m:
            if target[ind]!=i:
                ans.append("Push")
                ans.append("Pop")

            if target[ind]==i:
                ans.append("Push")
                ind+=1
            i+=1

        return ans