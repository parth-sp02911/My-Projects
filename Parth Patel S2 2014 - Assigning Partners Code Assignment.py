#Parth Patel
#797708
#CCC S2 Problem - Assigning Partners
#ICS4UOA
#Mr. Veera
#Decemember 11 2019

num_of_students = int(input("Enter the number of students: "))  #gets the user's input
partners_a = input("Enter the first set of students' name (seperated by a space): ").split()    
partners_b = input("Enter the names, in a different order (seperated by a space): ").split()  #Splits the partners name by space and sets them to two lists
flag = True #sentintel value which represents if the partner assignment is consistent or not
partners_dict = {}  #creates a dictionary

for student_index in range(num_of_students):
    partners_dict[partners_a[student_index]] = partners_b[student_index]   #assigns the value in the

for key in partners_dict:    
  value = partners_dict[key]

  if key == value:
      flag = False
      break
  elif key == partners_dict[value]:
      flag = True
  else:      
      flag = False
      break

if flag:
    print("Good")
else:
    print("Bad")



