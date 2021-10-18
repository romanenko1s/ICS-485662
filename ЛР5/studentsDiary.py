file1 = open("studentListData.txt", "r")
file2 = file1.readlines()

for line in file2:
    print("#  "+line)