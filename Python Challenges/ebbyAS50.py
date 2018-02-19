import sqlite3
conn=sqlite3.connect("CPUs.sqlite")

def create_cpu():
    with conn:
        conn.execute("CREATE TABLE CPUs(Name TEXT PRIMARY KEY, Cores INT, Threads INT, Speed DECIMAL)")

def add_cpus():
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

def add_cpu():
    with conn:
        NewName=input("CPU SKU: ")
        NewCores=input("Core Count: ")
        NewThreads=input("Threads: ")
        NewSpeed=input("Frequency: ")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed)VALUES(?,?,?,?)",(NewName,NewCores,NewThreads,NewSpeed))

def del_cpu():
    with conn:
        DelCPU=input("CPU SKU to delete: ")
        cur=conn.execute("SELECT Name, Cores, Threads, Speed FROM CPUs WHERE Name = ?",(DelCPU,))
        row=cur.fetchone()
        print("Name: ",row[0],"Cores: ",row[1],"Threads: ",row[2],"Speed: ",row[3],"Ghz")
        confirm=input("Are you sure you want to delete this SKU? y/n ")
        if confirm == "y":
            conn.execute("DELETE FROM CPUs WHERE Name = ?",(DelCPU,))

#create_cpu()
#add_cpus()
#print_cpu()
#print_row()
#search_cores()
#add_cpu()
#del_cpu()
