target_count = {}
        window_count = {}
        for char in t:
            target_count[char] = 1 + target_count.get(char, 0)
        p1 = 0
        p2 = 0
        res = ''
        res_len = float('inf')
        
        for p2 in range(len(s)):
            window_count[s[p2]] = 1 + window_count.get(s[p2], 0)
            
            valid_window = True
            for char in target_count.keys():
                if window_count.get(char, 0) < target_count[char]:
                    valid_window = False
            while valid_window:
                if res_len > p2 - p1 + 1:
                    res = s[p1:p2 + 1]
                    res_len = len(res)
                window_count[s[p1]] -= 1
                p1 += 1
                for char in target_count.keys():
                    if window_count[char] < target_count[char]:
                        valid_window = False
        return res
