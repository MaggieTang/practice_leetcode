# 11. Container With Most Water
'Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines 
'are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).'
'Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.'


#try1  O(n2)
def maxArea(self, height: List[int]) -> int:
        volumn = []
        max_volumn = 0
        for i in range(0, len(height)):
            volumn = max([abs(j-i)*min(height[i],height[j]) for j in range(i, len(height))])
            if max_volumn < volumn:
                max_volumn = volumn
        return max_volumn
      
# which is run out of time when input dataset is large


#try2.   O(n)
def maxArea(self, height: List[int]) -> int:
        size = len(height)
        left = 0
        right = size-1
        area = 0
        
        for width in range (size-1, 0, -1):
            if height[left] < height[right]:
                area = max(area, height[left] * width)
                left = left +1
                
            else:
                area = max(area, height[right] * width)
                right = right -1
                
        return area
      
      
 ###################
# Using two-points
