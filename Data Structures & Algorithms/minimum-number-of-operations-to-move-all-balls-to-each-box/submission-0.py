class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        n = len(boxes)

        for i in range(n):
            dist_back, dist_for = 0, 0
            
            step_back, step_for = 0, 0
            for j in range(i-1, -1, -1):
                dist_back += 1
                if boxes[j] == '1':
                    step_back += dist_back

            for j in range(i+1, n):
                dist_for += 1
                if boxes[j] == '1':
                    step_for += dist_for

            res.append(step_back + step_for)            


        return res