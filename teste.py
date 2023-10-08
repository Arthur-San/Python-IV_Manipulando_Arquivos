courses = []

with open("courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.strip().split(",")
        course = {}
        course["linguagem"] = linguagem
        course["categoria"] = categoria
        courses.append(course)    
print(courses)

def get_linguagem(course):
    return course["linguagem"]

def get_categoria(course):
    return course["categoria"]

for course in sorted(courses, key=get_linguagem):
    print(f"{course['linguagem']} - {course['categoria']}")