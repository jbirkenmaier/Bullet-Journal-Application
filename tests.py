# Original lists
list1 = [3, 1, 2]
list2 = ['c', 'a', 'b']

# Sorting list1 and obtaining the sorted index order
sorted_indices = sorted(range(len(list1)), key=lambda x: list1[x])
sorted_list1 = [list1[i] for i in sorted_indices]
sorted_list2 = [list2[i] for i in sorted_indices]

print("Sorted list1:", sorted_list1)
print("Sorted list2:", sorted_list2)
