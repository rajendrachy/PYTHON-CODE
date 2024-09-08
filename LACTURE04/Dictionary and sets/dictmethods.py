# # 1. dict.keys()

# # student = {
# #     "name" : "Rajendra",

# #     "subject" : {
# #         "phy" : 97,
# #         "che" : 98,
# #         "math" : 95
# #     }
# # }

# # print(len(student)) # 2 -->>> total keys only
# # print(student.keys())
# # #type casting
# # print(list(student.keys()))



# # 2. ..........values..........


# student = {
#     "name" : "Rajendra",
#      "course" : "BE CSE",

#     "subject" : {
#         "phy" : 97,
#         "che" : 98,
#         "math" : 95
#     }
# }

# print(len(student["subject"])) # 3 -> length of the key only
# print(student.values())
# #type conversion
# print(list(student.values()))


# 3. .........Items..........
# student = {
#     "name" : "Rajendra",
#      "course" : "BE CSE",

#     "subject" : {
#         "phy" : 97,
#         "che" : 98,
#         "math" : 95
#     }
# }

# print(student.items()) # in the form o the tuples
# print(type(student.items())) # dict
# #type conversion
# print(list(student.items()))
# print(type(list(student.items()))) # list



# #4. .........get -->>> dict.grt("key")..........
# student = {
#     "name" : "Rajendra",
#      "course" : "BE CSE",

#     "subject" : {
#         "phy" : 97,
#         "che" : 98,
#         "math" : 95
#     }
# }

# #same output
# print(student["name"]) 
# print(student.get("name"))

# #print(student["name2"]) # error 
# print(student.get("name2")) # None







#5. .........update -->>> dict.update("newDict")..........
student = {
    "name" : "Rajendra",
     "course" : "BE CSE",

    "subject" : {
        "phy" : 97,
        "che" : 98,
        "math" : 95
    }
}


student.update({"city": "delhi", "name" : "Chaudhary"}) # same key is not added in the last they are updated in the same
print(student)






