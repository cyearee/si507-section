import csv

file = open('comic_characters.csv','r')
file_iter = csv.reader(file)

print(type(file_iter))
print(dir(file_iter))

# print(next(file_iter))
print(next(file_iter))
print(next(file_iter))
print(next(file_iter))

 
# for row in file_iter:
# 	if 'Female' in row[7]:
# 		print(row[2] + ' is ' +row[4])

file.close()