from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visited = sorted(zip(timestamp, username, website))
        user_site = defaultdict(list)

        for _, user, site in visited:
            user_site[user].append(site)
        
        patter_count = defaultdict(int)
        for user, site in user_site.items():
            n = len(site)
            patterns = set()

            for i in range(0, n):
                for j in range(i+1, n):
                    for k in range(j+1, n):
                        patterns.add((site[i], site[j], site[k]))

            for pattern in patterns:
                patter_count[pattern] += 1
        
        best_pattern = []
        best_score = 0

        for pattern, score in patter_count.items():
            if score > best_score or (score == best_score and pattern < best_pattern):
                best_pattern = pattern
                best_score = score
        
        return list(best_pattern)




    
    
        