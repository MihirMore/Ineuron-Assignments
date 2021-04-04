#Write a Python program to remove duplicates from a list.

sample_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
duplicate_items =set()
unique_list = []
for num in sample_list:
    if num not in duplicate_items:
        unique_list.append(num)
        duplicate_items.add(num)

print(unique_list)         