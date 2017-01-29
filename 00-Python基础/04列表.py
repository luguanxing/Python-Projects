list = [1,2,3,4]
print("list")
print(list)
print("\n")

list.append(55)
print("list.append(5)")
print(list)
print("\n")

list.extend([6,7,8,9])
print("list.extend([6,7,8])")
print(list)
print("\n")

list.insert(0,0)
print("list.insert(0,0)")
print(list)
print("\n")

list.remove(55)
print("list.remove(55)")
print(list)
print("\n")

del list[1]
print("del list[1]")
print(list)
print("\n")

out = list.pop()
print("out = list.pop()")
print(list)
print("out=" +str(out)+"\n")


list2 = list[1:4]
print("list2 = list[1:4]")
print("list2="+str(list2))
print("\n")

list3 = list[1:]
print("list3 = list[1:]")
print("list3="+str(list3))
print("\n")

list4 = list[1::2]
print("list4 = list[1::2]")
print("list4="+str(list4))
print("\n")

listr = list[::-1]
print("listr = list[::-1]")
print("listr="+str(listr))
print("\n")

print(">>>>>>>>>>>>>>>\n")

print("list="+str(list)+"\n")
print("3 in list")
print(3 in list)
print("\n")

print("5 not in list")
print(5 not in list)
print("\n")

print("list.count(1)")
print(list.count(1))
print("\n")

print("list.index(3)")
print(list.index(3))
print("\n")

list.reverse()
print("list.reverse()")
print(list)
print("\n")

list.sort()
print("list.sort()")
print(list)
print("\n")

list.sort(reverse=True)
print("list.sort(reverse=True)")
print(list)
print("\n")

listp=list
listc=list[:]
print("listp=list")
print("listc=list[:]")
listp.append(999)
print("listp.append(999)\n")
print("list="+str(list))
print("listp="+str(listp))
print("listc="+str(listc))

del list

