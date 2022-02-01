def main():
    infile = open('philosophers.txt', 'r')

    file = infile.read()

    infile.close()

    print(file)

main()
