conv_pseudocode = {"int":"INTEGER","float":"REAL","char":"CHAR","str":"STRING","bool":"BOOLEAN","list":"ARRAY",
                   "open":"OPENFILE","read()":"READFILE","write":"WRITEFILE",
                   "print":"OUTPUT","if":"IF","else":"ELSE","elif":"CASE OF",
                   "for":"FOR","while":"WHILE","def":"FUNCTION","type":"TYPE",
                   "=":"<--","==":"=","in":"IN","range":"RANGE"}

code = open("ebbyAS12.py")
lines = code.readlines()

output = open("pseudocode.txt","w")
for line in lines:
    p_line = ''
    for part in line.split(" "):
        if part in conv_pseudocode.keys():
            part = conv_pseudocode[part]
        p_line += part+" "
    output.write(p_line)
output.close()

