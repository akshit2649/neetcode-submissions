class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x] 
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_y] > rank[root_x]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        for u, v in edges:
            union(u, v)
    
        unique_root = set()
        for n in range(n):
            unique_root.add(find(n))
        return len(unique_root)
        