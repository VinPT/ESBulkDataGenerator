def BulkDataGenerator():
    outputFileName = input("Provide output file: ")

    with openExistingFile("Provide Mapping File: ", 'r') as mappingFile:
        for line in mappingFile:
            print("This is not something that workes yet.")
            firstline = line

    with openExistingFile("Provide data file: ", 'r') as dataFile:
        for line in dataFile:
            print(line)
        print("This is not something that workes yet.")

    print("reformating Data:")

    with open(outputFileName, 'w') as outputFile:
        data = 'Test data to output file'
        outputFile.write(data)
        outputFile.write(firstline)

    print("done!")


def openExistingFile(requestText, method):

    assert method == 'r' or method == 'a', "Invalid file access method provided"
    while True:
        fileName = input(requestText)

        try:
            file = open(fileName, method)
            break
        except:
            print("Invalid file provided")
    return file


BulkDataGenerator()
