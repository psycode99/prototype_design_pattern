list_1 = [1, 2, 3, 4]
print(list_1)
list_2 = list_1
print(list_2)
list_2.append(5)
print(list_1)
print(list_2)

# problem with the code above is that when i append an item to list_2, I'm also appending
# that item to list_1. Why? this is because list_2 is referencing list_1 and as such they
# both have the same memory address - this is known as shallow copying.
# to deep copy that's where the prototype design pattern comes in