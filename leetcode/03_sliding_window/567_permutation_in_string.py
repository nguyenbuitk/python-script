import collections

class Solution:
    def checkInclusion(self, s1, s2):
        # Step 1: count the frequency of character in s1
        count_s1 = collections.Counter(s1)
        count_s2 = {}
        left = 0    # left pointer for the sliding window
        
        # Step 2: iterate through s2 using a sliding window
        for index, value in enumerate(s2):
            # add the current character to count_s2 frequency dict
            count_s2[value] = count_s2.get(value, 0) + 1
            
            if count_s2 == count_s1:
                return True

            # if the current character is not in s1, reset the window
            if value not in count_s1:
                count_s2 = {}
                left = index + 1
                continue
            
            # if count of a character exceeds that in s1, shrink the window till it equal to s1
            elif count_s2[value] > count_s1[value]:
                while count_s2[value] > count_s1[value]:
                    count_s2[s2[left]] -= 1
                    
                    # Remove key if value becomes zero (to match Counter behavior)
                    if count_s2[s2[left]] == 0:
                        del count_s2[s2[left]]
                    left += 1
        return False
            
solution = Solution()
print(solution.checkInclusion('dinitrophenylhydrazine', 'acetylphenylhydrazine'))
