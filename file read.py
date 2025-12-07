with open("pranav.txt","r")as file:
    #print(file.read())
    #print(file.readlines())
    """in the file read() reads te full data of the file 
    while the readline()reads the only one line of the file
    but if you give the command file.read() before the 
    file.readline() then file .readline()will not show the output
     because all the data were read by the file.read  2.condition
     if you give the number in the command of file.read() like file.read(4) 
     then it will print only the four char of that line and remaining line will read file.readline()"""
    print(file.read())
    file.seek(0)
    list=file.readlines()
    print(list)
    file.seek(0)
    print(file.readline())