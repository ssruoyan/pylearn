def length_of_longest_substring(s):
  maxSubLen = 0
  curSubLen = 0
  i, ln = 0, len(s)
  dic = ''
  while (i < ln):
      ss = s[i]
      if (ss in dic):
          if (curSubLen > maxSubLen):
            maxSubLen = curSubLen
          idx = dic.index(ss)
          dic = dic[idx + 1:]
          curSubLen = curSubLen - idx - 1
      curSubLen += 1
      dic += ss
      i += 1
  if (curSubLen > maxSubLen): maxSubLen = curSubLen
  return maxSubLen

def length_of_longest_substring2(s):
  start = 0
  ret = 0
  dic = {}
  ln = len(s)
  for i in range(0, ln):
    ss = s[i]
    # 到底了
    if ss in dic and start <= dic[ss]:
      ret = max(ret, i - start)
      start = dic[ss] + 1
    dic[ss] = i
  ret = max(ret, ln - start)
  return ret
    

print(length_of_longest_substring2(" a 1s"))