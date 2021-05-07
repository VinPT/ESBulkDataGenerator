def BulkDataGenerator():

    with openExistingFile("Provide Mapping File: ", 'r') as mappingFile:
        for line in mappingFile:
            print("This is not something that workes yet.")
            firstline = line

    with openExistingFile("Provide data file: ", 'r') as dataFile:
        for line in dataFile:
            print(line)
        print("This is not something that workes yet.")

    print("reformating Data:")

    with openNewFile("Provide output file:", 'w') as outputFile:
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


def openNewFile(requestText, method):
    import os.path
    assert method == 'w', "Invalid file access method must be 'w'"
    while True:
        fileName = input(requestText)

        if not os.path.exists(fileName):
            file = open(fileName, 'w')
            break
        else:
            print("Invalid File already exists")
            input("Would you like to over-write the file(enter Y to conferm):")
            if input == 'Y' or input == 'y':
                file = open(fileName, 'w')
                break

    return file


BulkDataGenerator()
