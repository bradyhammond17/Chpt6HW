def main():
    infile = open("philosophers.txt", "r")

    file_contents = infile.read()

    print(file_contents)


def add_my_name():
    outfile = open("philosophers.txt", "a")
    outfile.write("Brady Hammond")
    outfile.close()


main()
add_my_name()
