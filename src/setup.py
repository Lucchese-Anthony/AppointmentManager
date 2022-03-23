import sqlite3
import os

def main():
    path = os.getcwd()
    if not os.path.isdir("database"):
        os.mkdir("database")
    os.chdir(f"{os.getcwd()}/database/")
    query = """CREATE TABLE IF NOT EXISTS APPOINTMENTS(
        APPID           INT PRIMARY KEY     NOT NULL,
        USERID           TEXT                NOT NULL,
        TOPIC            TEXT                NOT NULL,
        EMAIL            TEXT                NOT NULL
        );"""
    conn = sqlite3.connect('appointments.db')
    print("successfully created the database")
    otherInputs = str(input("The default table contains:\n- Appointment ID\n- User ID\n- Meeting Topic\n- email address\n Is that ok? (y/n)> "))
    if otherInputs == "n":
        print("exiting program")
        exit()
    conn.execute(query)
    print("Successfully created the table...")


if __name__ == "__main__":
    main()