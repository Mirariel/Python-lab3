import string


def task1(text, start_word):
    if not text.strip() or not start_word.strip():
        return "Некоректні вхідні дані!"

    words = text.split()
    start_word = start_word.lower()

    count = 0
    for w in words:
        clean = w.strip(string.punctuation).lower()
        if clean.startswith(start_word):
            count += 1
    return count


def task2(text):
    if not text.strip():
        return "Некоректні вхідні дані!"

    replaced_text = text.replace("а", "А").replace("a", "A")
    count_replaced = sum(1 for c in text if c in "аa")
    total_chars = len(text)
    total_letters = sum(1 for c in text if c.isalpha())

    return f"{replaced_text}, кількість замін: {count_replaced}, кількість символів:{total_chars}, кількість літер: {total_letters}"


def task3(text, word):
    if not text.strip() or not word.strip():
        return "Некоректні вхідні дані!"

    word = word.lower()
    words = [w.strip(string.punctuation).lower() for w in text.split()]
    return words.count(word)


def task4(text):
    if not text.strip():
        return "Некоректні вхідні дані!"

    words = text.split()
    mid = len(words) // 2

    first_half = [w.capitalize() for w in words[:mid]]
    second_half = [w.lower() + "*" for w in words[mid:]]

    return " ".join(first_half) + " | " + " ".join(second_half)


def task5(text, letter_n, letter_p):
    # Перевірка тексту
    if not text.strip():
        return "Некоректний текст!"

    words = text.split()
    if len(words) > 1000:
        return "Текст перевищує 1000 слів!"

    # Перевірка літер
    if (len(letter_n) != 1 or len(letter_p) != 1 or
        letter_n.lower() not in string.ascii_lowercase or
        letter_p.lower() not in string.ascii_lowercase):
        return "Літери повинні бути англійськими (A-Z)!"

    letter_n = letter_n.lower()
    letter_p = letter_p.lower()

    starts_n = []
    ends_p = []

    for w in words:
        clean = w.strip(string.punctuation).lower()
        if not clean:
            continue

        if clean.startswith(letter_n):
            starts_n.append(clean)

        if clean.endswith(letter_p):
            ends_p.append(clean)

    return starts_n, ends_p


def task6(text):
    vowels = "aeiou"
    return sum(1 for c in text.lower() if c in vowels)


def task7(text):
    words = text.split()
    result = []

    for w in words:
        clean = w.strip(string.punctuation)
        if clean and clean[0].isupper():
            result.append(clean)

    return result


while True:
    print("\n=== МЕНЮ ЗАВДАНЬ ===")
    print("1 — Завдання 1")
    print("2 — Завдання 2")
    print("3 — Завдання 3")
    print("4 — Завдання 4")
    print("5 — Завдання 5")
    print("6 — Завдання 6")
    print("7 — Завдання 7")
    print("0 — Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        text = input("Введіть текст: ")
        start_word = input("Введіть початкове слово/літеру: ")
        print("Результат:", task1(text, start_word))

    elif choice == "2":
        text = input("Введіть текст: ")
        print("Результат:", task2(text))

    elif choice == "3":
        text = input("Введіть текст: ")
        word = input("Введіть слово для пошуку: ")
        print("Результат:", task3(text, word))

    elif choice == "4":
        text = input("Введіть текст: ")
        print("Результат:", task4(text))

    elif choice == "5":
        text = input("Введіть текст: ")
        letter_n = input("Введіть першу літеру: ")
        letter_p = input("Введіть другу літеру: ")
        print("Результат:", task5(text, letter_n, letter_p))

    elif choice == "6":
        text = input("Введіть текст: ")
        print("Результат:", task6(text))

    elif choice == "7":
        text = input("Введіть текст: ")
        print("Результат:", task7(text))

    elif choice == "0":
        print("Вихід з програми.")
        break

    else:
        print("Невірний вибір!")