class Solution:
    def isHappy(self, n: int) -> bool:
        return self.isHappyHelper(n, set())

    def isHappyHelper(self, n, seen: set) -> bool:
        
        if seen and n in seen:
            return False
        s = sum(map(lambda x: int(x)**2, list(str(n))))
        if s==1:
            return True
        else:
            seen.add(n)
            return self.isHappyHelper(s, seen)

sol = Solution()

print(sol.isHappy(2))