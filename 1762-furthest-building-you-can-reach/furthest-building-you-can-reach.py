class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) == 1:
            return 0
        pq = []
        i = 0
        while i < len(heights) - 1:
            if heights[i + 1] <= heights[i]:
                i += 1
                continue
            diff = heights[i + 1] - heights[i]
            if bricks >= diff:
                bricks -= diff
                heapq.heappush(pq, -diff)
            elif ladders > 0:
                if pq:
                    past_bricks = -pq[0]
                    if past_bricks > diff:
                        bricks += past_bricks
                        heapq.heappop(pq)
                        bricks -= diff
                        heapq.heappush(pq, -diff)
                ladders -= 1
            else:
                break
            i += 1
        return i