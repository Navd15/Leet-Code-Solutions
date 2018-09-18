# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
      length=len(points)

      if length>0:       
        maxPoints=[None]*length
        for i in range(length):
           diag=1
           hor=1
           vert=1
           for j in range(length):
            #   if(marked[i][j]==False):
                if i!=j:
                    vals=points[i]
                    nvals=points[j] 
                    
                    diff_X=(abs(max(nvals.x,vals.x)))-(abs(min(vals.x,nvals.x )))
                    diff_Y=(abs(max(nvals.y,vals.y)))-(abs(min(vals.y,nvals.y )))
                    
                    if(nvals.x==vals.x and vals.y==nvals.y and length<=2):
                        diag=diag+1
                    else:    
                     if diff_X==0:
                         vert=vert+1
                          
                        #  maxPoints[i][1]=vert              
                     else:
                      if diff_Y==0:
                         hor=hor+1
                      else:                        
                        if diff_X==diff_Y:
                           diag=diag+1
                      
                    #    Takes out max from 3 values and store it in maxPoints array
                maxPoints[i]=max([diag,hor,vert])
                
                        # maxPoints[i][2]=hor   
        
        return max(maxPoints)    
      return 0



# You may input an 2d list to maxPoints() method