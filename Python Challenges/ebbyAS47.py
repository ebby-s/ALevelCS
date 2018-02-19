import sqlite3

conn = sqlite3.connect("CPUs.sqlite")

def create_ryzen_db():
    with conn:
        conn.execute("CREATE TABLE CPUs(id INTEGER PRIMARY KEY, Name TEXT, Cores INT, Threads INT, Speed DECIMAL)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1200',4,4,3.1)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1300X',4,4,3.4)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1400',4,8,3.2)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1500X',4,8,3.5)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1600',6,12,3.2)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1600X',6,12,3.6)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1700',8,16,3.0)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1700X',8,16,3.4)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1800X',8,16,3.6)")
