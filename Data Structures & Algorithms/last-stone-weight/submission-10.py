class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            # -7, -3
            if first != second:
                heapq.heappush(stones, first - second)
        if stones:
            return stones[0] * -1
        return 0
            