age = [22, 42, 16, 50]
names = ['Alice', 'Bob', 'Charlie', 'Diana']
for number, name in enumerate(names):
    print(f"{name} is {age[number]} old", end=", ")
    # Output: Alice is 22 old, Bob is 42 old, Charlie is 16 old, Diana is 50 old,

for name, age in zip(names, age):
    print(f"{name} is {age} old", end=", ")
    # same output as above
