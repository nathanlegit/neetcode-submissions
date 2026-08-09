class Solution:

    def encode(self, strs: List[str]) -> str:
        master_string = ""
        for string in strs:
            length = len(string)
            master_string = master_string + str(length) + "#" + string
        return master_string
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            target_index = s.find("#" , i)
            length_string = ""
            for j in range (i , target_index):
                length_string = length_string + s[j]
            length = int(length_string)
            string = ""
            for n in range (target_index + 1 , target_index + length + 1):
                string = string + s[n]
            result.append(string)
            i = target_index + length + 1
        return result

