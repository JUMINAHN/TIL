new_dict = {}

print(new_dict.setdefault('a', []))
new_dict.setdefault('a', []).append(1)
print(new_dict)