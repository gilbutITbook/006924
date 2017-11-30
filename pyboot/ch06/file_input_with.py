try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError as fne:
    print(fne)
