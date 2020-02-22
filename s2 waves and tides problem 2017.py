num_of_measurements = int(input("Enter the number of measurements: "))
measurement = list(map(int, input("Enter your measurements (seperated by space): ").split())) 
correct_measure = []

for i in range(num_of_measurements):
    if len(measurement) == 0:
        break

    elif len(measurement) % 2 != 0 and len(measurement) == 1:
        correct_measure.append(max(measurement))
        break
        
    correct_measure.append(max(measurement))
    correct_measure.append(min(measurement))
    measurement.remove(min(measurement))
    measurement.remove(max(measurement))

for i in correct_measure[::-1]:
    print(i, end=" ")
                       

##N = int(input())
##heights = list(map(int, input().split()))
##heights.sort()
##
##lowtide = heights[:int((N+1)/2)]
##hightide = heights[int((N+1)/2):]
##
##lowtide.reverse()
##answer = []
##for a in range(N//2):
##  answer.append(str(lowtide[a]))
##  answer.append(str(hightide[a]))
##
##print(answer)
##if N % 2 == 1:
##  answer.append(str(lowtide[-1]))
##print(" ".join(answer))

              
#the map function works like this:  map( *performs a function*, *to each element in a list/tuple*) ---> it returns a map object which we turn into a list.
#in my code the 'int' funcition is the operator which is applied to each element in the list so i can turn every string of that list into an integer *super useful*
