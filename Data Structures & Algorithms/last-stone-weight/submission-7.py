class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        elif not stones:
            return 0
        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            # -3, -7,
            if x > y:
                heapq.heappush(stones, y - x)
            elif y > x:
                heapq.heappush(stones, x - y)
        if stones:
            return stones[0] * -1
        return 0
            