class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Convert digits manually
        result = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit

            # 4. Check 32-bit range
            if sign == 1 and result > 2147483647:
                return 2147483647

            if sign == -1 and -result < -2147483648:
                return -2147483648

            i += 1

        return sign * result
        