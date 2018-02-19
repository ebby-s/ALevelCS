import sqlite3
conn=sqlite3.connect("CPUs.sqlite")

def create_cpu():
    with conn:
        conn.execute("CREATE TABLE CPUs(Name TEXT PRIMARY KEY, Cores INT, Threads INT, Speed DECIMAL)")

def add_cpu():
    with conn:
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1200',4,4,3.1)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1300X',4,4,3.4)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1400',4,8,3.2)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1500X',4,8,3.5)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1600',6,12,3.2)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1600X',6,12,3.6)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1700',8,16,3.0)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1700X',8,16,3.4)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1800X',8,16,3.6)")

def print_cpu():
    with conn:
        cur=conn.execute("SELECT Name, Cores, Threads, Speed from CPUs")
        for row in cur:
            print("")
            print("Name: ",row[0])
            print("Cores: ",row[1])
            print("Threads: ",row[2])
            print("Speed: ",row[3],"Ghz")
        print ("The End")


def print_row():
    with conn:
        PrintCPU=input("CPU SKU: ")
        cur=conn.execute("SELECT Name, Cores, Threads, Speed FROM CPUs WHERE Name = ?",(PrintCPU,))
        row=cur.fetchone()
        print("Name: ",row[0],"Cores: ",row[1],"Threads: ",row[2],"Speed: ",row[3],"Ghz")

def search_cores():
    MinCores=input("How many cores do you want?: ")
    with conn:
        cur=conn.execute("SELECT Cores, Name FROM CPUs WHERE Cores>=? ORDER BY Cores", (MinCores,))
        for row in cur:
            print(row[0],"Cores",row[1])

#create_cpu()
#add_cpu()
#print_cpu()
#print_row()
#search_cores()
