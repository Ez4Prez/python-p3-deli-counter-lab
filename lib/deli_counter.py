katz_deli = []

def line(line):
    if len(line) == 0:
        print("The line is currently empty.")
    else:
        line_message = "The line is currently:"
        for i, person in enumerate(line, start = 1):
            line_message += f" {i}. {person}"
        print(line_message)
    


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)

    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)


