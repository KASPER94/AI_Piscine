from NumPyCreator import NumPyCreator

npc = NumPyCreator()

print(npc.from_list([[1,2,3], [6,4,6]]))
print()

print(npc.from_list([[1,2,3], [4,6]]))
print()

print(npc.from_list([[1,2,3],['a','b','c'],[5.0,6.1,7.8]]))
print()

print(npc.from_list([[1,2,3],{'a','b','c'},[5.0,6.1,7.8]]))
print()

print(npc.from_tuple(("a","b","c")))
print()

print(npc.from_tuple([[1,2,3],[6,3,4]]))
print()

print(npc.from_iterable(range(5)))
print()

shape=(3,5)

print(npc.from_shape(shape))
print()

print(npc.random(shape))
print()

print(npc.identity(3))
print()