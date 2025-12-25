from collections import deque
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(enumerate(tickets))  # (index, tickets)
        time = 0

        while True:
            idx, t = q.popleft()
            t -= 1
            time += 1

            if t == 0:
                if idx == k:
                    return time
            else:
                q.append((idx, t))
