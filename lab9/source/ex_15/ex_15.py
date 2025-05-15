import os


def directory_line_reader(root_path):
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith(".txt"):
                with open(os.path.join(dirpath, filename), "r") as f:
                    for line in f:
                        yield line.strip()


root = "/Users/dmitriy/PycharmProjects/PPYTasks/lab9/source/ex_15/test_dir"
for ln in directory_line_reader(root):
    print(ln)