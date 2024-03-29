import sqlite3
#backends


def studentData():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY key, StdID text, Firstname text, Lastname text, DoB text, Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()


def addStdRec(StdID, Firstname, Lastname, DoB, Age, Gender, Address, Mobile):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (StdID, Firstname, Lastname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    con.close
    return rows

def deleteRec(id):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close

def searchData(StdID="", Firstname="", Lastname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Lastname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?", (StdID, Firstname, Lastname, DoB, Age, Gender, Address, Mobile))
    rows=cur.fetchall()
    con.close()
    return rows

def dataUpdate(StdID="", Firstname="", Lastname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, Lastname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=?, WHERE id=?", (StdID, Firstname, Lastname, DoB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()
