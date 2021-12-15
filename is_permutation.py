def isPermutation(a,b):
  if len(a) != len(b):
    return False
  else:
    for i in range(len(a)):
      print(i)
      if a[i] != b[-1-i]:
        return False
    return True

print (isPermutation("dcba","abcd"))
