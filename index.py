import sqlite3
import sys

def printQueryDetails(records):
    for row in records:
        print("Id: {}\nMovie Name: {}\nActor Name: {}\nActress Name: {}\nDirector Name: {}\nYear of Production: {}\nType of Movie: {}\nBudget: {} crore\nBox Office: {} crore\n\n".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

try:
    #Connecting to the database
    connection = sqlite3.connect('movie.db')

except sqlite3.Error as error:
    print("Failed to connect to database",error)

try:
    #Create a cursor to run SQL commands using execute method
    cursor = connection.cursor()

    #Creating a movies table in movie.db
    cursor.execute("""
        CREATE TABLE movies(
            id INTEGER PRIMARY KEY,
            movieName TEXT,
            actorName TEXT,
            actressName TEXT,
            directorName TEXT,
            yearOfProduction INTEGER,
            type TEXT,
            budget INTEGER,
            boxOffice INTEGER
        )""")

    #Inserting value into table movies 
    cursor.execute(" INSERT INTO movies values(1, 'KGF Chapter 1', 'Yash', 'Srinidhi Shetty', 'Prashanth Neel', 2018, 'Action', 100, 250) ")

    cursor.execute(" INSERT INTO movies values(2, 'KGF Chapter 2', 'Yash', 'Srinidhi Shetty', 'Prashanth Neel', 2022, 'Action', 150, 1200) ")

    cursor.execute(" INSERT INTO movies values(3, 'Radhe Shyam', 'Prabhas', 'Pooja Hegde', 'Radha Krishna Kumar', 2022, 'Romance', 300, 150) ")

    cursor.execute(" INSERT INTO movies values(4, 'Tagaru', 'Shiva Rajkumar', 'Manvita Kamath', 'Duniya Suri', 2018, 'Action', 10, 15) ")

    cursor.execute(" INSERT INTO movies values(5, 'Thugs of Hindostan', 'Aamir Khan', 'Katrina Kaif', 'Vijay Krishna Acharya', 2018, 'Adventure', 300, 335) ")



    #Select all movie from the table
    cursor.execute("SELECT * FROM movies")
    print(" Query #1: ")
    print("Select all movie from the table: \n")
    printQueryDetails(cursor.fetchall())

    #Select all movies which are directed by Prashanth Neel
    cursor.execute(" SELECT * FROM movies where directorName='Prashanth Neel' ")
    print("Query #2: ")
    print("Select all movies which are directed by Prashanth Neel: \n")
    printQueryDetails(cursor.fetchall())

    #Select all movies whose budget is more than 100 crores
    cursor.execute(" SELECT * FROM movies where budget >= 100 ")
    print("Query #3: ")
    print("Select all movies whose budget is more than 100 crores: \n")
    printQueryDetails(cursor.fetchall())

    #Select all movies whose budget is less than 100 crores
    cursor.execute(" SELECT * FROM movies where budget < 100 ")
    print("Query #4: ")
    print("Select all movies whose budget is less than 100 crores: \n")
    printQueryDetails(cursor.fetchall())

    #Select all movies which are blockbuster
    cursor.execute(" SELECT * FROM movies where boxOffice > (2 * budget) ")
    print("Query #5: ")
    print("Select all movies which are blockbuster: \n")
    printQueryDetails(cursor.fetchall())

    #Select all movies which couldn't earn back their budget amount
    cursor.execute(" SELECT * FROM movies where boxOffice <= budget ")
    print("Query #6: ")
    print("Select all movies which couldn't earn back their budget amount: \n")
    printQueryDetails(cursor.fetchall())
    
    #Select all movie which made more money than their budget but were flop movies
    cursor.execute(" SELECT * FROM movies where boxOffice >= budget and boxOffice < (2 * budget)  ")
    print("Query #7: ")
    print("Select all movie which made more money than their budget but were flop movies: \n")
    printQueryDetails(cursor.fetchall())

    #Commit the changes
    connection.commit()

except sqlite3.Error as error:
    print("Failed to perform query on table movies")
    print("Error is: ",error)
    print("If error is -> table movies already exists, then delete the movie.db file")

finally:
    if connection:
        #Close the connection
        connection.close()