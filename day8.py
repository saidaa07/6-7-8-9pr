students = []

def add_student():
    name = input("Аты-жөні: ")
    age = int(input("Жасы: "))
    group = input("Тобы: ")
    gpa = float(input("GPA: "))

    student = {
        "name": name,
        "age": age,
        "group": group,
        "gpa": gpa
    }

    students.append(student)
    print("Студент қосылды!\n")


def show_students():
    if len(students) == 0:
        print("Тізім бос.\n")
    else:
        print("\nСтуденттер тізімі:")
        for s in students:
            print(f"{s['name']} | {s['age']} жас | {s['group']} | GPA: {s['gpa']}")
        print()


def search_student():
    name = input("Ізделетін студенттің аты: ")

    found = False
    for s in students:
        if name.lower() in s["name"].lower():
            print(f"Табылды: {s['name']} | {s['group']} | GPA: {s['gpa']}")
            found = True

    if not found:
        print("Студент табылмады.\n")


def save_file():
    with open("students.txt", "w", encoding="utf-8") as file:
        for s in students:
            file.write(f"{s['name']},{s['age']},{s['group']},{s['gpa']}\n")

    print("Мәліметтер файлға сақталды!\n")


def load_file():
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            for line in file:
                name, age, group, gpa = line.strip().split(",")
                students.append({
                    "name": name,
                    "age": int(age),
                    "group": group,
                    "gpa": float(gpa)
                })
        print("Мәліметтер жүктелді!\n")
    except FileNotFoundError:
        print("Файл табылмады.\n")


while True:
    print("====== СТУДЕНТТЕР ЖҮЙЕСІ ======")
    print("1. Студент қосу")
    print("2. Студенттер тізімі")
    print("3. Студент іздеу")
    print("4. Файлға сақтау")
    print("5. Файлдан оқу")
    print("6. Шығу")

    choice = input("Таңдауыңыз: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        save_file()
    elif choice == "5":
        load_file()
    elif choice == "6":
        print("Бағдарлама аяқталды.")
        break
    else:
        print("Қате таңдау!\n")