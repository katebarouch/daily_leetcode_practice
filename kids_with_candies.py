class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output_list =[]
        max_candies = max(candies)
        
        for index in range(len(candies)):
                if candies[index] + extraCandies >= max_candies:
                    output_list.append(True)
                else:
                    output_list.append(False)
            
        return output_list
