tuple1 = (1,2,3,4,5,6,7,8)

print("tuple1 = (1,2,3,4,5,6,7,8)")
print(tuple1)
print("\n")

print("tuple1[:5]")
print(tuple1[:5])
print("\n")

tuple2 = 1,2,3
print("tuple2 = 1,2,3,4")
print(tuple2)
print("\n")

emptytuple = ()
mytuple = 1,
print("emptytuple = ()\nmytuple = 1,")
print(emptytuple)
print(mytuple)
print("\n")

tuple1=tuple1[:3]+(999,)+tuple1[3:]
print("tuple1=tuple1[:3]+(999,)+tuple1[3:]")
print(tuple1)
print("\n")

tuple1=tuple1[:3]+tuple1[4:]
print("tuple1=tuple1[:3]+tuple1[4:]")
print(tuple1)
print("\n")

del tuple1
