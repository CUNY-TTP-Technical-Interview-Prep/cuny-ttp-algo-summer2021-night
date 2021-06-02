def isAlmostEqual(letter_count):
    for val in letter_count.values():
        if abs(val) > 3:
            return False
    return True


def areAlmostEquivalent(s,t):
    n = len(s)
    result = []

    for i in range(n):
        letter_count = {}

        for char in s[i]:
            if char not in letter_count:
                letter_count[char] =1
            else:
                letter_count[char] +=1
        
        for char in t[i]:
            if char not in letter_count:
                letter_count[char] = -1
            else:
                letter_count[char] -=1
    
        if isAlmostEqual(letter):
            result.append('YES')
        else:
            result.append('NO')
    
    return result