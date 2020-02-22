#Parth Patel
#797708
#ICS4UOA
#j3 2016 problem - Hidden Palindrome
#Mr. Veera
#September 9 2019

def ispalindrome(word):
    reversed_word = word[-1::-1]
                                        #I first created a function called ispalindrome that take ones parameter, it checks if the parameter is a palindrome
                                       #it does this by reversing the word and checking if they are still equal. If so, it returns the length of the palindrome or else it returns a 0
    if(reversed_word == word):                       
        return(len(word))
    else:
        return(0)



user_word = list(input("Enter the word: "))         # getting the inputs and converting it to a list

longest_palindrome_list=[]       #creating a list to store all the palindrome lengths



for index in range(len(user_word)):                                                  #these two loops go through all the combinations of letters and sends it to my ispalindrome function

    palindrome= ''       #i created an empty string                                                         

    for index2 in range(len(user_word)):  

        palindrome = palindrome + user_word[index2]       #creates a palindrome variable that stories the combinations of letters to check if they are palindromes 

                                                                           
        longest_palindrome_list.append(ispalindrome(list(palindrome)))  #adds all the lengths of a palindrome into a list

    del user_word[0]  #deletes the first index of the original word so that it start checking the combinations of the next letters



                                                #outputs the largest palindrome length
print(max(longest_palindrome_list))

