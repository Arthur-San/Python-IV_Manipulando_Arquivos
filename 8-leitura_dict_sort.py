courses = []

with open("courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.strip().split(",")
        course = {}
        course["linguagem"] = linguagem
        course["categoria"] = categoria
        courses.append(course)    
print(courses)


for course in sorted(courses, key=lambda course: course["liuagem"]):
    print(f"{course['linguagem']} - {course['categoria']}")