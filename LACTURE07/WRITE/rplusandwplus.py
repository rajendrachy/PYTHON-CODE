#1.
# f = open("demo.txt", "r+") # r + ---> read + write
#                            # r+ -->> overwrite at beginning of the text not cut the original content
# f.write("abc")
# f.close()


# 2. w+ -->> write + read--->> but cut the original txt and write another which we can write

# f = open("demo.txt", "w+") # r + ---> read + write
#                            # r+ -->> overwrite at beginning of the text not cut the original content
# f.write("chaudhary")
# f.close()



# 3. a+ -->> append + read
# f = open("demo.txt", "a+") # r + ---> read + write
#                            # r+ -->> overwrite at beginning of the text not cut the original content
# f.write("rajendra")
# f.close()

#4))))-->>>>
# r+ -->> no truncate -> data not delete
# w+ -->> truncate -> DATA delete
