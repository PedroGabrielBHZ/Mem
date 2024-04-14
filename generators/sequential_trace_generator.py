import random


def generate_lines(n):
    lines = []
    for i in range(n):
        line = "2 " + str(i % 8)
        lines.append(line)
    return lines


def write_to_file(lines, filename):
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")


for N in [10, 100, 1000, 10000]:
    filename = "traces/sequential_" + str(N) + "_m8.txt"
    lines = generate_lines(N)
    write_to_file(lines, filename)
