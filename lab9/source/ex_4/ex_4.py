def line_reader(file_path):
    with open(file_path) as file:
        for ln in file:
            yield ln


for line in line_reader("/Users/dmitriy/PycharmProjects/PPYTasks/lab9/source/ex_4/file.txt"):
    print(line)