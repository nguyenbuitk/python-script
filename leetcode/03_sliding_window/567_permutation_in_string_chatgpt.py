from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False  # s1 is longer than s2, so no permutation is possible

        # Character frequency count for s1 and initial window in s2
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len_s1])

        # Check initial window
        if count_s1 == count_s2:
            return True

        # Slide the window across s2
        for i in range(len_s1, len_s2):
            count_s2[s2[i]] += 1  # Add new char to window
            count_s2[s2[i - len_s1]] -= 1  # Remove old char from window

            # Remove key if value becomes zero (to match Counter behavior)
            if count_s2[s2[i - len_s1]] == 0:
                del count_s2[s2[i - len_s1]]

            # Check if current window matches s1's frequency
            if count_s1 == count_s2:
                return True

        return False
