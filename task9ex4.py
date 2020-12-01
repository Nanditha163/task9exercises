listn=[16,21,27,108,3,18,44,36,82,90]
result=list(filter(lambda x:(x%9==0),listn))
print("Numbers divisible by 9 are:",result)


OUTPUT:
Numbers divisible by 9 are: [27, 108, 18, 36, 90]