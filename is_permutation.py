def isPermutation(a,b):
  if a and b :
    if len(a) != len(b):
      return False
    else:
      for i in range(len(a)):
        print(i)
        if a[i] != b[-1-i]:
          return False
      return True
  else:
    return False

print (isPermutation(None,None))
print (isPermutation("abc","cba"))
print (isPermutation("",""))
