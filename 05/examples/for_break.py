fruits = ["apple", "banana", "cherry"]
search_item = "banana"

for fruit in fruits:
    if fruit == search_item:
        print(search_item, "found in list")
        break
else:
    print(search_item, "not found in list")
