# f = open("d.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()



# f = open("d.txt", "r")
# data = f.read(5) # only read 5 word in the content we wrote
# print(data)
# f.close



f = open("d.txt", "r")
line1 = f.readline() # only read 5 word in the content we wrote
print(line1)

line2 = f.readline()
print(line2)
f.close
