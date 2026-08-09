class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""
        lower_string = s.lower()
        for char in lower_string:
            if char.isalnum():
                cleaned_string += char
        left_index = 0
        right_index = len(cleaned_string) - 1
        while left_index < right_index:
            if cleaned_string[left_index] == cleaned_string[right_index]:
                left_index += 1
                right_index -= 1
                continue
            else:
                return False
        return True

        