'''task
1)create dictionary
2)USE SETS TO REMOVE DUPLICATES
3)FUNCTION COMMON STUDENTS TO CHECK
4)ALL PARTICIPENTS FUNCTION TO LIST ALL UINIQUE CANDIDATES
5)USE TUPLE TO ADD DIXED DETAILS
6)FUNCTION TO CHECK HIGHEST UNIQE CANDIDATES
7)PRINT ALL DETAILS
'''


data = {
    "Python": ["Anu", "Ravi", "Meera", "Anu", "Kiran"],
    "Data Analytics": ["Ravi", "Meera", "Arjun", "Ravi"],
    "Web Development": ["Kiran", "Arjun", "Priya", "Meera"],
}

# Remove duplicate registrations
for workshop in data:
    data[workshop] = set(data[workshop])

# Return students registered for both workshops.
def common_students(workshop1, workshop2):
    return data[workshop1] & data[workshop2]

# Return all unique workshop participants.
def all_participants():
    students = set()
    for participants in data.values():
        students |= participants
    return students

# Return the workshop with the most unique participants.
def highest_workshop():
    return max(data, key=lambda workshop: len(data[workshop]))


# Workshop details: (workshop name, room, instructor)
details = (
    ("Python", "Room 101", "Kumar"),
    ("Data Analytics", "Room 102", "Priya"),
    ("Web Development", "Room 103", "Ravi"),
)


print("Common students:", common_students("Python", "Data Analytics",))
print("All participants:", all_participants())
print("Highest registration:", highest_workshop())
print("Workshop details:", details)
print(data["Web Development"])

choice=input("Enter workshop name to display candidates: ")
if(choice == 'Python'):
    print(data["Python"])
elif(choice=="Data Analytics"):
    print(data["Data Analytics"])
elif(choice=="Web Development"):
    print(data["Web Development"])
else:
    print("Invalid choice")