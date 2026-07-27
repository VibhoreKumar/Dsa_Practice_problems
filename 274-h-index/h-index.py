class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):#by using this instead of this (for i in range (len(citations)) it will only print values but using this fori,v in enumerate(citations) will also give index's makes it compareing easier / )
            if n - i <= v:
                return n - i
        return 0