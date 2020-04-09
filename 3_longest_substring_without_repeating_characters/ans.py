class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0
        elif l == 1:
            return 1
            
        unique_set = set()
        max_len = 0
        
        i = 0
        j = 0
        while i < l and j < l:
            #print(f'i: {i}, j: {j}')
            if s[j] not in unique_set:
                unique_set.add(s[j])
                j += 1
                max_len = max(max_len, j - i) # after j+=1, j-i just happen to be the length of current scanned characters
                #print(unique_set)
                #print(f'ans: {max_len}')
                
            else:
                #print(f'{s[j]} exist')
                unique_set.remove(s[i])
                i += 1
                #print(f'move i to: {i}')
                #print(unique_set)
                
        return max_len
