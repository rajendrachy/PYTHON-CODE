#1. read

# with open("demo.txt", "r") as f:  # f -->> alias
#     data = f.read()
#     print(data)
    
#2. write ---> cut the data and overwrite
with open("demo.txt", "w") as f:  # f -->> alias
    f.write("New data")
    f.close()
    