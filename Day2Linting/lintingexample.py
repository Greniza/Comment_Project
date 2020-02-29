def terminal(teacher1 = "Teacher 1", teacher2 = "Teacher 2"):
    '''takes in teacher names and returns a message'''
    name = input("What is your name? ")
    rs = f"{teacher1} and {teacher2} are glad that you are learning to use your terminal, {name}."
    return rs


def main():
    print(terminal("Lauren", "Matt"))


if __name__ == "__main__":
    main()
