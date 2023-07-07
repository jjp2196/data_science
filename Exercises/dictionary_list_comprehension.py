# Given the following list of people:

# people = [
#     {'name': 'Dr. Anniston', 'age': 37, 'role': 'doctor'},
#     {'name': 'Nurse Clara', 'age': 45, 'role': 'nurse'},
#     {'name': 'Alex', 'age': 20, 'role': 'patient'},
#     {'name': 'Junie', 'age': 33, 'role': 'patient'},
# ]

# Use a list comprehension to return the names of students who are younger than 37.

def find_younger_than_37():
    people = [
        {'name': 'Dr. Anniston', 'age': 37, 'role': 'doctor'},
        {'name': 'Nurse Clara', 'age': 45, 'role': 'nurse'},
        {'name': 'Alex', 'age': 20, 'role': 'patient'},
        {'name': 'Junie', 'age': 33, 'role': 'patient'},
    ]
    return [person['name'] for person in people if person['age'] < 37 and person['role'] == 'patient']

result = find_younger_than_37()
print("Result:", result)