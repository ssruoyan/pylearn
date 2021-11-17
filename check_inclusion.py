def check_inclusion(s1: str, s2: str) -> bool:
    ln1 = len(s1)
    ln2 = len(s2)
    if (ln1 > ln2): return False
    dict1 = {}
    dict2 = {}
    for i in range(0, ln1):
        if (s1[i] in dict1): dict1[s1[i]] += 1
        else: dict1[s1[i]] = 1
        if (s2[i] in dict2): dict2[s2[i]] += 1
        else: dict2[s2[i]] = 1

    if (dict1 == dict2): return True
    k = 0
    while (k < ln2 - ln1):
        l = s2[k]
        r = s2[k + ln1]
        print(l, r)
        k = k + 1
        dict2[l] -= 1
        if (dict2[l]) == 0: del dict2[l]
        if (r in dict2): dict2[r] += 1
        else: dict2[r] = 1
        if dict2 == dict1: return True
    return False
 
st1 = 'ab'
st2 = 'eidbaooo'
print(check_inclusion(st1, st2))
