from itertools import combinations

# use itertools to obtain N combinations from a list 
res = combinations([1,2,3,4], 2)


# now iterate over all our 2-element combinations and check  
for item in res:
    if(item[0] + item[1] == 5):
        print("*****")
        print(item)
        break
