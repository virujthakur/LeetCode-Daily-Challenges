class Solution:
    #TC: O(N) SC: O(1)
    def frequencySort(self, s: str) -> str:
        return ''.join([char * freq for char, freq in Counter(s).most_common()])
