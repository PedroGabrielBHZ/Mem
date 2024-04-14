import random


def generate_lines(n):
    lines = []
    for i in range(n):
        if i % 3 == 0:
            line = "2 " + str(1)
        else:
            line = "2 " + str(random.randint(0, 7))
        lines.append(line)
    return lines


def write_to_file(lines, filename):
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")


for N in [10, 100, 1000, 10000]:
    filename = "traces/temporal_" + str(N) + "_m8.txt"
    lines = generate_lines(N)
    write_to_file(lines, filename)
