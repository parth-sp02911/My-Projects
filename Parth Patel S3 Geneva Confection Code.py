##Parth Patel
##797708
##Python 2014 S3 - The Geneva Confection
##Mr Veera
##ICS4UOA
##December 12 2019

def is_possible(carts, length):    # i created a function that checks if the starting arrangements of carts is possible. It take two parameters; the user's list and its length
    smallest_check = 1 #i have a variable called the smallest_check which is supposed to be the first cart's number that has to arrive in the lake
    
    while smallest_check <= length: #i have a loop that will keep iterating until the smallest check gets as large as the length of the cart list
        if len(carts) > 0 and carts[-1] == smallest_check: 
            lake.append(carts[-1])
            carts.pop()             #if the last element of the carts list is equal to the smallest check it will append the lake with that cart number and pop that cart from the carts list
            smallest_check += 1 #smallest check increases by 1
            
        elif len(branch) > 0 and branch[-1] == smallest_check:  
            lake.append(branch[-1])
            branch.pop()                     #else if the last element of the branch is equal to the smallest_check it will append that to the lake
            smallest_check += 1 #smallest check increases by 1

        else:
            if len(carts) > 0:    
                branch.append(carts[-1]) #if the carts list doesn't have the next number in the arrangement it will append the current cart to the branch 
                carts.pop()
            else:   
                break   #if everything above is not true and the cart is empty it means the arrangement is invalid and will break out the loop
            
    if len(lake) == length: #if the length of the lake is equal to the length of the original list, it means the final pattern was 1,2,3,4...N so it will return True
        return True
    else:
        return False #if not it will return false
 
num_of_tests = int(input("Number of Tests: ")) #stores the number of tries the user wants
test_carts = [] #creates a list that stores all the test carts (this will be a 2d list)
branch = []
lake = [] #creates a list that will store the branch and the lake carts

for test in range(num_of_tests):
    num_of_carts = int(input("Enter the number of carts in the test: "))  #these loops take all the input from the user and stories it inside the test_carts 2d list
    test_carts.append([])

    for cart in range(num_of_carts):
        test_carts[test].append(int(input("cart's Number: ")))

for carts in test_carts:

    if is_possible(carts, len(carts)): #for each carts in test_carts it will call the function i made and print "Y" or "N" based on what the function returns
        print("Y")
    else:
        print("N")
