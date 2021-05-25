import random

def get_answer():
    while True:
        answer = input()
        if len(answer) > 0 :
            if answer[0] == "-":
                if answer[1:].isnumeric():
                    return int(answer) 
            else:
                if answer.isnumeric():
                    return int(answer)
        print("Incorrect format.")

def get_level():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        number = input()
        if number in ("1", "2"):
            return int(number)
        print("Incorrect format.")

def level2():
    mark = 0
    for i in range(5):
        a = random.randint(11, 29)
        print(a)
        answer = get_answer()
        result = "Right!" if answer == a * a else "Wrong!"
        mark += 1 if answer == a * a else 0
        print(result)
    return mark

def level1():
    mark = 0
    for i in range(5):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        ope = random.choice(["+", "-", "*"])
        print(a, ope, b)
        answer = get_answer()
        if ope == "+":
            c = a + b
        elif ope == "-":
            c = a - b
        elif ope == "*":
            c = a * b
        result = "Right!" if answer == c else "Wrong!"
        mark += 1 if answer == c else 0
        print(result)
    return mark

def write_result(mark, level):
    print("What is your name?")
    name = input()
    file = open("results.txt", "a", encoding="utf-8")
    if level == 1:
        text = f"{name}: {mark}/5 in level 1 (simple operations with numbers 2-9)."
    else:
        text = f"{name}: {mark}/5 in level 2 (integral squares of 11-29)."
    file.write(text + "\n")
    file.close()
    print('The results are saved in "results.txt".')

level = get_level()
if level == 1:
    mark = level1()
else:
    mark = level2()
print(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
yesno = input()
if yesno.lower() == "yes":
    write_result(mark, level)