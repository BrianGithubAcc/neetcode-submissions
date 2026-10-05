class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sols={}
        for i in strs:
            if tuple(sorted(i)) in sols:
                sols[tuple(sorted(i))].append(i)
            else:
                sols[tuple(sorted(i))]=[i]
        return list(sols.values())