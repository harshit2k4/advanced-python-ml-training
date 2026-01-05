# create a random student_data with random and dictonary

import random
student_data = {
    "name": random.choice(["Alice", "Bob", "Charlie"]),
    "age": random.randint(18, 25),
    "skills": random.choice(["ML", "DL", "Python", "AI"]),
}
print(student_data)