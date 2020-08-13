import mysql.connector
import os

directory ="./data/"
for fileName in os.listdir(directory ):
    if fileName.endswith(".csv"):


#fileName = input("Please enter the file name to import: ")

        listOfRecords = []
        with open(directory + fileName, "r") as fileObject:
            for line in fileObject:
               listOfRecords.append(tuple(line.rstrip('\n').split(",")))



        mydb = mysql.connector.connect(
                host = "localhost",
                user = "kevin",
                password="maria",
                database="mydatabase"
                )

        mycursor = mydb.cursor()

        mycursor.execute("SHOW TABLES LIKE '" + fileName.split(".")[0] + "'" )
        if len(mycursor.fetchall()) == 1:
            raise SystemExit("Table already exists.")

        stmt = "CREATE TABLE " +fileName.split(".")[0] + " (" + listOfRecords[0][0] + " CHAR(20) PRIMARY KEY"

        for x in range(1,len(listOfRecords[0])):
            stmt += ", " + listOfRecords[0][x] + " CHAR(20)"
        stmt += ")"

        mycursor.execute(stmt)

        for x in range(1, len(listOfRecords)):
            stmt = "INSERT INTO " + fileName.split(".")[0] + " VALUES("
            for tpl in listOfRecords[x]:
                stmt += "'" +  tpl + "',"
            stmt = stmt[0:len(stmt)-1]
            stmt += ")"
            mycursor.execute(stmt)
            mydb.commit()


