import csv

path = input("Path to csv: ")
path = path.replace('"', "").replace("\\", "/") 
with open(path, "r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter='\n')
    query = ""
    for row in csvReader:
        query += ""+row[0]+","
    newFile = open("C:/Users/bbarker/Desktop/PythonOutput.txt", "w")
    newFile.write(query)
    newFile.close()
