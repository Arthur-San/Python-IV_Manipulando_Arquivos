courses = []

with open("courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        lenguage, category = line.rstrip().split(",")
        courses.append(f"{lenguage} - {category}")
        print(courses)
        
    for course in sorted(courses): #reverse=True
        print(course)