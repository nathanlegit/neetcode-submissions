class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num , 0) + 1
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for key , value in my_dict.items():
            freq_buckets[value].append(key)
        output = []
        for num_list in reversed(freq_buckets):
            for num in num_list:
                k = k - 1
                output.append(num)
                if k == 0:
                    return output

            