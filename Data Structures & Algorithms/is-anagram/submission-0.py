class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = False
        if len(s) == len(t):
            my_dict_s = {}
            my_dict_t = {}
            for i in range(len(s)):
                my_dict_s[s[i]] = my_dict_s.get(s[i], 0) + 1
            for i in range(len(s)):
                my_dict_t[t[i]] = my_dict_t.get(t[i], 0) + 1
            if my_dict_s == my_dict_t:
                is_anagram = True
        return is_anagram


    


#my own thought process: we have 2 strings, and we have ot find out if they are anagrams, measn we dont care the order of the characters, we just have to find a way to count the number of each unique character and compare these 2. We know that we can access the different characters using an index. e.g. s = 'cat' -> s[0] = 'c' etc. 
#so we can use a for loop to run through all the characters of the string. and we need to store these in a list/set. and we know that sets are unordered, so we probably need to use sets here. my question is, does sets store it in a fixed way for all different orders? can we equate two sets together?