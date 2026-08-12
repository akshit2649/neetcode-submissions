from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indeg = {}
        for word in words:
            for c in word:
                indeg[c] = 0
        
        for i in range(len(words) -1):
            w1 = words[i]
            w2 = words[i+1]

            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for k in range(min_len):
                if w1[k] != w2[k]:
                    graph[w1[k]].append(w2[k])
                    indeg[w2[k]] += 1
                    break

        q = deque()
        for key, val in indeg.items():
            if val == 0:
                q.append(key)
            
        order = []
        while q:
            c = q.popleft()
            order.append(c)
            for nei in graph[c]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        if len(order) != len(indeg):
            return ""
        
        return "".join(order)