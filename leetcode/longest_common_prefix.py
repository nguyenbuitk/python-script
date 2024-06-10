class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        m = {}
        for s in strs:
            for index in range(1, len(s) + 1):
                if s[0:index] not in m.keys():
                    m[s[0:index]] = 1
                else:
                    m[s[0:index]] += 1
        result = []
        print(m)
        for key, value in m.items():
            if not result:
                result.append(key)
                result.append(value)
            elif len(key) > len(result[0]) and value >= result[1]:
                result[0] = key
                result[1] = value
        print(result)
        if result[1] == 1:
            return ""
        return result[0]

sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))