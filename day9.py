students = []

def add_student():
    print("\n=== Студент қосу ===")

    name = input("Аты-жөні: ")

    try:
        age = int(input("Жасы: "))
        gpa = float(input("GPA: "))
    except ValueError:
        print("Қате! Сан енгізу керек.")
        return

    group = input("Тобы: ")

    student = {
        "name": name,
        "age": age,
        "group": group,
        "gpa": gpa
    }

    students.append(student)
    print("Студент сәтті қосылды!\n")


def show_students():
    print("\n=== Студенттер тізімі ===")

    if not students:
        print("Тізім бос.\n")
        return

    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} | {s['age']} жас | {s['group']} | GPA: {s['gpa']}")

    print()


def search_student():
    print("\n=== Студент іздеу ===")

    name = input("Атын енгізіңіз: ")

    found = False

    for s in students:
        if name.lower() in s["name"].lower():
            print(f"\nТабылды:")
            print(f"Аты-жөні: {s['name']}")
            print(f"Жасы: {s['age']}")
            print(f"Тобы: {s['group']}")
            print(f"GPA: {s['gpa']}")
            found = True

    if not found:
        print("Студент табылмады.\n")


def save_file():
    with open("students.txt", "w", encoding="utf-8") as file:
        for s in students:
            file.write(
                f"{s['name']},{s['age']},{s['group']},{s['gpa']}\n"
            )

    print("Мәліметтер файлға сақталды.\n")


def load_file():
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            students.clear()

            for line in file:
                name, age, group, gpa = line.strip().split(",")

                students.append({
                    "name": name,
                    "age": int(age),
                    "group": group,
                    "gpa": float(gpa)
                })

        print("Мәліметтер файлдан оқылды.\n")

    except FileNotFoundError:
        print("Файл табылмады!\n")


def sort_students():
    students.sort(key=lambda x: x["name"])
    print("Студенттер аты бойынша сұрыпталды.\n")


while True:
    print("=================================")
    print("      СТУДЕНТТЕР ЖҮЙЕСІ")
    print("=================================")
    print("1. Студент қосу")
    print("2. Студенттер тізімін көрсету")
    print("3. Студент іздеу")
    print("4. Студенттерді сұрыптау")
    print("5. Файлға сақтау")
    print("6. Файлдан оқу")
    print("7. Шығу")

    choice = input("\nТаңдауыңыз: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        sort_students()

    elif choice == "5":
        save_file()

    elif choice == "6":
        load_file()

    elif choice == "7":
        print("Бағдарлама аяқталды.")
        break

    else:
        print("Қате! Қайтадан енгізіңіз.\n")