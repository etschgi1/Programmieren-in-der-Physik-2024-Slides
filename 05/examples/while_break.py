fruits = ["apple", "banana", "cherry"]
search_item = "banana"
i = 0

while i < len(fruits):
    if fruits[i] == search_item:
        print("Found", search_item, "at index", i)
        break
    i += 1
else:
    print(search_item, "not found in list")
