def BulkDataGenerator():
  print("")
  mappingFileName = input("Provide mapping file: ")
  dataFileName = input("Provide data file: ")
  outputFileName = input("Provide output file: ")
   
  with open(mappingFileName, 'r') as mappingFile:
    firstline = mappingFile.readline()


  print("reformating Data:")



  with open(outputFileName, 'w') as outputFile:
    data = 'Test data to output file'
    outputFile.write(data)
    outputFile.write(firstline)

  print("done!")

BulkDataGenerator()