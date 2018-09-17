class Solution:
 def method(self,nums1,nums2):
    high1=len(nums1)
    
    median=None
    high2=len(nums2)
    print(high2)
    res=[None]*(high1+high2)
    i=0
    j=0
    count=0
    while(res[(high1+high2)-1]==None) :
            if high1==0:
                for x in range(j,high2):
                 res[count]=nums2[x]
                 count=count+1
                break
            if high2==0:
                for x in range(i,high1):
                 res[count]=nums1[x]
                 count=count+1     
                break         
            if nums1[i]<nums2[j]:
               res[count]=nums1[i]
               count=count+1
               i=i+1
            else:
               if nums1[i]>nums2[j]:
                res[count]=nums2[j]
                count=count+1
                j=j+1    
               
            if i>=high1:
                for x in range(j,high2):
                 res[count]=nums2[x]
                 count=count+1
                
            if j>=high2:
                for x in range(i,high1):
                 res[count]=nums1[x]
                 count=count+1 
                
            print(res)
    
    if(high1+high2) % 2 !=0:
        median=res[int((high1+high2)/2)]
    else:
        med=int((high1+high2)/2)
        print(med)
        median=(res[med-1]+res[med] )/2    
    return median
s=Solution()
# list=[None,None]
# list[0]=1
# print(5/2)
print(s.method([1,3],[2]))
