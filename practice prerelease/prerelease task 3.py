filename = str(input("Enter a filename: "))    # Asks user for file name

while True:
    try:
        file_len = int(input("Enter number of lines: "))  # Asks user for file length
        if file_len <= 0:
            print("File length has to be a positive integer.")
        else:
            break
    except :
        print("File length has to be an integer.")


file = open(filename+".txt","w")               # Creates file

for i in range(file_len):                           # Adds lines
    file.write("This is line " + str(i+1)+"\n")

file.close()                                     # Saves file

def read_file(filename):      # Reads and prints out whole file
    try:
        file = open(filename+".txt","r")
        print(file.read())
    except:
        print("File not found")

def read_lines(filename,line_range):    # Reads and prints out a range of lines
    try:
        file = open(filename+".txt","r")
        lines = file.readlines()
        for i in line_range:
            print(lines[i])
    except:
        print("File not found")

read_file(filename)
read_lines(filename,range(3,7))

