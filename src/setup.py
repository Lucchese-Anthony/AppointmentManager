import sqlite3
import os

def main():
    path = os.getcwd()
    if not os.path.isdir("database"):
        os.mkdir("database")
    os.chdir(f"{os.getcwd()}/database/")
    query = 
    """CREATE TABLE APPOINTMENTS IF NOT EXISTS(
        APPID           INT PRIMARY KEY     NOT NULL,
        USERID           TEXT                NOT NULL,
        TOPIC            TEXT                NOT NULL,
        EMAIL            TEXT                NOT NULL,
        
        );"""
    conn = sqlite3.connect('appointments.db')
    otherInputs = raw_input("would you like to add other attributes to the table? (yes/no)> ")
    while(otherInputs.lower() != "no"):
        Name = raw_input("What would you like the row value be?> ")
        Type = raw_input("What would you like the row type be? (INT / TEXT / REAL/ NONE)> ")
        nullable = raw_input("is it (NULL) or (NOT NULL)> ")
        if nullable == "NULL":
            nullable = ""
        query = query + f" {Name} {Type} {nullable}"
    conn.execute('''CREATE TABLE APPOINTMENTS IF NOT EXISTS
        (APPID           INT PRIMARY KEY     NOT NULL,
        USERID           TEXT                NOT NULL,
        TOPIC            TEXT                NOT NULL,
        EMAIL            TEXT                NOT NULL,
        );''')



if __name__ == "__main__":
    main()