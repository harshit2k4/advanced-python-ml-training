student = {
    "name": "Alice",
    "age": 30,
    "grade": "A",
    "courses": ["Python", "ML"]
}

print(student["name"])
print(student["age"])
print(student["grade"])
print(student["courses"])

# Make your own profile

my_profile = {
    "name": "your_name",
    "age": 21,
    "skills" : ["Coding", "Thinking"],
    "scores": {"math": 95, "english": 90}
}

print(my_profile["name"])
print(my_profile["age"])
print(my_profile["skills"])
print(my_profile["scores"])

my_profile["skills"].append("ML")
print(my_profile["skills"])

my_profile["scores"]["math"] = 85
print(my_profile["scores"])