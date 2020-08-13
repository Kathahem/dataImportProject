import mysql.connector
import os
import json

directory ="./data/"
for fileName in os.listdir(directory ):
    if fileName.endswith(".json"):
        with open(directory + fileName,"r") as read_file:
            mydb = mysql.connector.connect(
            host = "localhost",
            user = "kevin",
            password="maria",
            database="mydatabase"
            )

            mycursor = mydb.cursor()

            data = json.load(read_file)
            for table in data:
                stmt = "CREATE TABLE " +fileName.split(".")[0] + " (" 
                print(table)
                for firstRecContents in data[table][0]:
                    stmt += firstRecContents + " CHAR(50),"
                stmt = stmt[0:len(stmt)-1]
                stmt+=")"
                mycursor.execute(stmt)
                for record in data[table]:
                    stmt = "INSERT INTO " + fileName.split(".")[0] + " VALUES("
                    for entry in record:
                        stmt += "'" +  str(record[entry]) + "',"
                    stmt = stmt[0:len(stmt)-1]
                    stmt += ")"
                    mycursor.execute(stmt)
                    mydb.commit() 


       # print(type(data["Employees"][0]))


#fileName = input("Please enter the file name to import: ")

#        listOfRecords = []
#        with open(directory + fileName, "r") as fileObject:
#            for line in fileObject:
#               listOfRecords.append(tuple(line.rstrip('\n').split(",")))



#        mydb = mysql.connector.connect(
#                host = "localhost",
#                user = "kevin",
#                password="maria",
#                database="mydatabase"
#                )

#        mycursor = mydb.cursor()

#        mycursor.execute("SHOW TABLES LIKE '" + fileName.split(".")[0] + "'" )
#        if len(mycursor.fetchall()) == 1:
#            raise SystemExit("Table already exists.")

#        stmt = "CREATE TABLE " +fileName.split(".")[0] + " (" + listOfRecords[0][0] + " CHAR(20) PRIMARY KEY"

#        for x in range(1,len(listOfRecords[0])):
#            stmt += ", " + listOfRecords[0][x] + " CHAR(20)"
#        stmt += ")"

#        mycursor.execute(stmt)

#        for x in range(1, len(listOfRecords)):
#            stmt = "INSERT INTO " + fileName.split(".")[0] + " VALUES("
#            for tpl in listOfRecords[x]:
#                stmt += "'" +  tpl + "',"
#            stmt = stmt[0:len(stmt)-1]
#            stmt += ")"
#            mycursor.execute(stmt)
#            mydb.commit()


