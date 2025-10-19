hash = {}

hash["person1"] = {"name": "John", "age": 30}
hash["person2"] = {"name": "Alice", "age": 25}
hash["person3"] = {"name": "Bob", "age": 35}

for key, value in hash.items():
    print(f"{key}: {value['name']} is {value['age']} years old")
