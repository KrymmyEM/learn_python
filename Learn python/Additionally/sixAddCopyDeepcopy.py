
list1 = [1,2,3, [4,5,6]]

print("copy")
cop_list = list1.copy()
cop_list[3].append(7)

print(list1)
print(cop_list)
print()

print("import libery ''copy'' ")
import copy

print("shallow copy ('copy.copy(l\d)')")
shallow_copy = copy.copy(list1)
shallow_copy[3].append(7)

print(list1)
print(shallow_copy)
print()

print("deep copy ('copy.deepcopy(l\d)')")
deep_copy = copy.deepcopy(list1)
deep_copy[3].append(7)

print(list1)
print(deep_copy)
print()
