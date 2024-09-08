#search for the no X

nums = (1,2, 4, 5, 6, 7, 8, 4, 5, 6)
x = 7
idx = 0
for el in nums:
    if(el == x):
        print("number found at index", idx)
        break
    idx = idx + 1
        