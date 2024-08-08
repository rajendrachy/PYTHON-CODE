collection = set()
collection.add(1)
collection.add(2)
collection.add(2) #ignore the duplicate value
collection.add("apna college")

collection.remove(1)

#collection.remove(7) # key error

collection.clear() #clear all the value

print(collection)
print(len(collection))