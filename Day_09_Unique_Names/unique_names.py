names = []
while True:
    name = input("Enter the name: ")
    if name.lower() == "stop":
        break
    names.append(name)

unique_names = set(names)
print(f"Total entries: {len(names)}")
print(f"Unique names: {len(unique_names)}")
print(unique_names)