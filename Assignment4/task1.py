try:
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        for number, line in enumerate(file.readlines()):
            print(f"Line {number + 1}: {line}", end="")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
