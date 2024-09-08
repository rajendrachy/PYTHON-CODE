# search the number x in the tuples using a loop
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x=36

i=0
while i < len(nums):
    if(nums[i] == x) :
        print("Found at index : ", i)
        break
    else:
        print("finding..")
    i += 1
    print("End of loop")
