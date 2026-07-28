class Solution:
    def maxArea(self, height):
        length = len(height)
        left = 0
        right = length - 1
        wamount = min(height[left],height[right])*(right - left)
        while left<right:
            if height[left]<=height[right]:
                left+=1
            
            else:
                right-=1

            wamount = max(wamount,min(height[left],height[right])*(right - left))


        return wamount

sol = Solution()
print(sol.maxArea([2,2,2]))