#Parth Patel
#797708
#ICS4UOA
#J3 Problem 2019 - Cold Compress
#Mr.Veera
#September 7 2019

num_of_lines = int(input("Enter the number of lines: "))
                                        #I created two variable; one which will hold the number of lines the user wants and the other to hold the final list which will be outputed
output_final_list = []



for line in range(num_of_lines):  #I created the main for loop which will iterate as many times as the lines the user inputed


    message = list(input("Enter a message: ")) #I have 3 variables: one to store the message of the user and convert it to a list

    
    symbol_count = 1  #the second variable, to count the number of times a symbol gets repeated

                          
    output_line_message = [] #the third variable, to create a "temporary" empty list that will hold one line of the final user output

    
    for symbol in range(len(message)): #I created aother for loop that will repeat for the length of the message

            
        if symbol+1 >= len(message): #I check if the next character index in the loop will be greater than the actual message (if it is this will result in error)

            
            output_line_message.append(str(symbol_count) + " " + message[symbol] + " ")     #if it is true, i will append the following message to the temporary list and break out the loop                              
            break
        
        else:
            

            if message[symbol] == message[symbol + 1]:  #if the next character in the loop is equal to the current character, it will increment the symbol_count variable by 1

                symbol_count += 1
                                
            else:
                                    #if it isn't then it will append the following message to the temporary list and reinitlize the count variable back to 1
                                            
                output_line_message.append(str(symbol_count) + " " + message[symbol] + " ") 
                symbol_count = 1 
                
                                
    output_final_list.append(output_line_message) #Once the loop is done, it will append the temporary list message to the final list which will be outputed to the user
        


for element in range(len(output_final_list)):

    for word in output_final_list[element]:
                                                #this code is to output the information in the final list
        print(word, end ='')

    print()
