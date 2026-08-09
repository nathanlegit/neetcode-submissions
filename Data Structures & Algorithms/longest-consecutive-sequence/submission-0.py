class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        for num in nums:
            my_set.add(num)
        streak = 0
        for s in my_set:
            if s - 1 in my_set:
                continue
            current_streak = 1
            i = 1
            while s + i in my_set:
                i += 1
                current_streak += 1
            streak = max(streak, current_streak)
        return streak
