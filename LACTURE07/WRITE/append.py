#append --> a -> add content 


f = open("de.txt", "a") # if file is not existe the file will automatically create
                        # in case of the  'a' & 'w'
f.write("I want to learn javascript tomorrow. 123")
f.close()