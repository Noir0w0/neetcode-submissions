class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = dict()
        for num in nums:
            try:
                my_dict[num] += 1
            except KeyError:
                my_dict[num] = 1
                
        my_list = []
        for key,val in my_dict.items():
            my_list.append([val,key])
        my_list.sort()
        start_idx = len(my_list)-k
        result = []
        for grp in my_list[start_idx:]:
            result.append(grp[1])
        return result