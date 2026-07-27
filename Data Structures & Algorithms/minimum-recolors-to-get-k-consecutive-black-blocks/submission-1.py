class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L = 0
        w = 0
        min_w = len(blocks)
        for R in range(len(blocks)):
            if blocks[R] == "W":
                w += 1
            if R - L + 1  > k:
                if blocks[L] == "W":
                    w -= 1
                L += 1

            if R - L + 1 == k:
                min_w = min(min_w, w)
        return min_w
