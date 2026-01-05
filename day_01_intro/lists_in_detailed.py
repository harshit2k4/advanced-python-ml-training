names = ["Alice", "Bob", "Carol", "David"]

# Unpacking the list and then applying the looping
# * operator unpacks or opens up the list
def print_names(*names):
  for name in names:
    print(name)

print_names(names)

print("----------------------------------")

list1 = [1,2,3]
list2 = [6,7,8]

combined = [*list1, *list2]
print(combined)

# we can print without using loops too
print(*list1)
print(*list2)

print(f"Combined List: {combined}\n")

# some other ways to do the same are append() and extend()
# they are not the same, they work differently
# run them separately to get proper output

list1.append(list2)
print(list1)

list1.extend(list2)
print(list1)