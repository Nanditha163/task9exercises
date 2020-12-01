from functools import reduce
list1=[1,3,5,7]
list2=[2,4,6,8]
result1=reduce((lambda x,y:x*y),list1)
result2=reduce((lambda x,y:x*y),list2)
print("Result of list1 after multiplication:")
print(result1)
print("Result of list2 after multiplication:")
print(result2)

OUTPUT:
Result of list1 after multiplication:
105
Result of list2 after multiplication:
384