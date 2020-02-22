#Parth Patel
#797708
#ICS4UOA
#J2 problem 2019 - Time to Decompress
#Mr.Veera
#September 6 2019




num_of_lines = int(input("Enter the number of lines: ")) #asks the user how many lines they want and turns that into an integer


output_list = [] #creates a list which will hold the values of the message the user wants


for line in range(num_of_lines): #creates a for loop which will repeat as many times, as the user inputed in the "num_of_lines" variable


    user_input = (input("Enter the message: ")).split() #in the loop I ask the user to enter the message they want and split it by the space (turning it into a list)
    
    num_of_char = int(user_input[0]) #I create a variable which will hold the number of times the user wants their character repeated

    char = user_input[1] #i create a variable which will hold the character the user wants to be repeated

    output_list.append(char * num_of_char) #I make the program repeat the character as many times as the user wants and then append it to the final output list
    
    


for element in output_list:

    print(element)  #I print all the elements in the list
