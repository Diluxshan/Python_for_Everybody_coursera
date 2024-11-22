# filename = input('Enter the file name :')
filename = "file.txt"
parser = open(filename, 'r')

total_count = 0
for line in parser:
	line = line.replace('"','')
	words = line.split()
	print(words)
	print(len(words))
	total_count = total_count + len(words)
print(total_count)
print("Hello Ac")
