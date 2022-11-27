def question_1():
    OUTPUT_FILE = "name.txt"
    out_file = open(OUTPUT_FILE, 'w')

    user_name = input("What is your name?\n>>>")
    print(f"{user_name}", file=out_file)
    print("Your name has been saved ")

    out_file.close()


def question_2():
    OUTPUT_FILE = "name.txt"
    out_file = open(OUTPUT_FILE, 'r')

    print("Your name is Bob")

    out_file.close()


def question_3():
    total = 0

    OUTPUT_FILE = "numbers.txt"
    out_file = open(OUTPUT_FILE, 'r')

    for i in range(2):
        numbers = int(out_file.readline().strip())
        total += numbers

    print(total)
    out_file.close()


def question_4():
    total = 0

    OUTPUT_FILE = "numbers.txt"
    out_file = open(OUTPUT_FILE, 'r')

    for i in out_file.readlines():
        total += int(i)

    print(total)
    out_file.close()


# question_1()
# question_2()
# question_3()
# question_4()


