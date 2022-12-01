import fileinput


def main():
    totals = []

    list = fileinput.input(files = "calories.txt")
    counter = 0
    for line in list:
        if (line != "\n"):
            counter = counter + int(line)
        else:
            totals.append(counter)
            counter = 0

    biggest = 0
    for elf in range(len(totals)):
        if (totals[elf] > biggest):
            biggest = totals[elf]

    print(biggest)

main()