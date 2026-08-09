class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1
        while left_index < right_index:
            guess = numbers[left_index] + numbers[right_index]
            if guess == target:
                return [left_index + 1, right_index + 1]
            if guess < target:
                left_index += 1
                guess = numbers[left_index] + numbers[right_index]
            if guess > target:
                right_index -= 1
                guess = numbers[left_index] + numbers[right_index]

        