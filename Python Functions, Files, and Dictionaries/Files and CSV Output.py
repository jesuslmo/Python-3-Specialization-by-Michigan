# Reading a file
fileref = open("file.txt")
contents = fileref.read()
print(contents[:100])
lines = fileref.readlines()  # read only lines of the files with new line character
for line in lines:
    print(line.strip())
fileref.close()

# Write a file
file_obj = open("file.txt", "w")
for number in range(13):
    square = number * number
    file_obj.write(str(square) + '\n')
file_obj.close()

# Using of with
file_obj = open("file.txt", "w")
for number in range(13):
    square = number * number
    file_obj.write(str(square) + '\n')
file_obj.close()

# CSV files
fileconnection = open("olympics.txt", 'r')
 lines = fileconnection.readlines()
 header = lines[0]
 field_names = header.strip().split(',')
 print(field_names)
 for row in lines[1:]:
     vals = row.strip().split(',')
     if vals[5] != "NA":
         print("{}: {}; {}".format(
                 vals[0],
                 vals[4],
                 vals[5]))

# Writing Data to a csv file:
olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()