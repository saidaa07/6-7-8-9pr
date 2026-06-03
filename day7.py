# 1. Сөйлемді кері шығару
text = input("Мәтін енгізіңіз: ")
print("Кері мәтін:", text[::-1])

# 2. Сөздер санын анықтау
words = text.split()
print("Сөз саны:", len(words))

# 3. Сөзді алмастыру
old_word = input("Ауыстырылатын сөз: ")
new_word = input("Жаңа сөз: ")
print("Өзгертілген мәтін:", text.replace(old_word, new_word))

# 4. Факториал (рекурсия)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Факториал үшін сан енгізіңіз: "))
print("Факториал:", factorial(num))

# 5. Фибоначчи (рекурсия)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Фибоначчи үшін n енгізіңіз: "))
print("Фибоначчи саны:", fibonacci(n))

# 6. Файлдан оқу
file = open("text.txt", "r", encoding="utf-8")
content = file.read()
file.close()

print("\nФайл мәтіні:")
print(content)

# 7. Жолдар мен сөздер санын анықтау
lines = content.split("\n")
words = content.split()

print("Жол саны:", len(lines))
print("Сөз саны:", len(words))

# 8. Өңдеп жаңа файлға жазу
new_content = content.upper()

file = open("result.txt", "w", encoding="utf-8")
file.write(new_content)
file.close()

print("Нәтиже result.txt файлына жазылды.")