class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []

        for i in range(1, n+1):            
            current_str = ""

            if i % 3 == 0:
                current_str += "Fizz"
            if i % 5 == 0:
                current_str += "Buzz"
            if not current_str:
                current_str = str(i)

            ans.append(current_str)

        return ans
