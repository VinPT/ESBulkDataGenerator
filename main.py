def BulkDataGenerator():
    mappingFileName = input("Provide mapping file: ")
    outputFileName = input("Provide output file: ")

    with open(mappingFileName, 'r') as mappingFile:
        for line in mappingFile:
            print("This is not something that workes yet.")
            firstline = line

    with openDataFile("Provide data file: ") as dataFile:
        for line in dataFile:
            print(line)
        print("This is not something that workes yet.")

    print("reformating Data:")

    with open(outputFileName, 'w') as outputFile:
        data = 'Test data to output file'
        outputFile.write(data)
        outputFile.write(firstline)

    print("done!")


def openDataFile(requestText):
    while True:
        fileName = input(requestText)

        try:
            file = open(fileName, 'r')
            break
        except:
            print("Invalid file provided")
    return file


BulkDataGenerator()
