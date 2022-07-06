import runpy


path = "UserData"


def read_points():
    with open(path) as file:
        txt = file.read()       # txt = "2 points"
        values = txt.split()    # values = ["2", "points"]

        return int(values[0])   # values[0] = "2" => int(values[0]) = 2


def save_points(value):
    with open(path, "w") as file:
        file.write(format_points(value))


def format_points(value):
    if value == 1:
        return str(value) + " point"

    return str(value) + " points"


try:
    points = read_points()

    while True:
        command = input("Please insert command: ")
        if command == "read":
            points = read_points()
            print(format_points(points))
            continue

        if command == "add":
            points = points + 1
            print(format_points(points))
            continue

        if command == "save":
            save_points(points)
            print("Points saved")
            print(format_points(points))
            continue

        if command == "points":
            print(format_points(points))
            continue

        if command == "done":
            break

except FileNotFoundError:
    print("File Not Found")
