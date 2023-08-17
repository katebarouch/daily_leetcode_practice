class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        # create dictionary to store frequencies
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1

        # sort the dictionary items 
        # first by value -x[1] (descending) and then by key x[0] (lexicographical)
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

        # extract the top k words
        ans = []
        for i in range(k):
            word = sorted_counts[i][0]
            ans.append(word)
        
        return ans