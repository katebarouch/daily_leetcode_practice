"""605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without 
violating the no-adjacent-flowers rule and false otherwise."""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        counter = 0
        possible_n = 0

        for plot in flowerbed:
            if plot == 0:
                counter += 1
            else:
                counter = 0
                
            if counter >= 3:
                possible_n += (counter - 1) // 2
                counter = 0
            
        if n <= possible_n:
            return True
        else:
            return False