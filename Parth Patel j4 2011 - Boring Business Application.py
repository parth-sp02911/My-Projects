def create_coordinate(x, y):
    
    return ("(" + str(x) + "," + str(y) + ")")

def allowed_to_drill(drill_point):

    return_value = True
    for point in danger_list:
       
        if drill_point == point:      
            return_value = False
            break

    return return_value

danger_list = ["(0,-1)","(0,-2)","(0,-3)","(1,-3)",
               "(2,-3)","(3,-3)","(3,-4)","(3,-5)",
               "(4,-5)","(5,-5)","(5,-4)","(5,-3)","(6,-3)",
               "(7,-3)","(7,-4)","(7,-5)","(7,-6)","(7,-7)",
               "(6,-7)","(5,-7)","(4,-7)","(3,-7)","(2,-7)",
               "(1,-7)","(0,-7)","(-1,-7)","(-1,-6)","(-1,-5)"]
user_point_list = []
drill_x = -1
drill_y = -5

while True:
    user_input = (input("Enter the direction followed by the positive length: ")).split()
    direction = user_input[0]
    length = int(user_input[1])
    not_danger = True
    original_drillx = drill_x
    original_drilly = drill_y
    
    if direction.lower() == 'q':
        break
    else:
        
        if direction.lower() == "u":

            for count in range(length):
                
                if allowed_to_drill( create_coordinate(drill_x, drill_y+1) ):                            

                    danger_list.append( create_coordinate(drill_x, drill_y+1) )
                    drill_y += 1
                else:
                    not_danger = False
                    break
                    
            if not_danger:
                user_point_list.append(create_coordinate(drill_x,drill_y) + " Safe")
            else:
                user_point_list.append( create_coordinate(drill_x, original_drilly + length) + " Danger!")
                break

        if direction.lower() == "d":

            for count in range(length):

                if allowed_to_drill(  create_coordinate(drill_x, drill_y-1) ):                                          
                    danger_list.append( create_coordinate(drill_x, drill_y-1) )
                    drill_y -= 1
                else:
                    not_danger = False
                    break
                    
            if not_danger:
                user_point_list.append(create_coordinate(drill_x,drill_y) + " Safe")
            else:
                user_point_list.append( create_coordinate(drill_x, original_drilly - length) + " DANGER!!!" )
                break
            
        if direction.lower() == "r":

            original_drillx = drill_x
            for count in range(length):
                
                if allowed_to_drill(  create_coordinate(drill_x + 1, drill_y) ):                                          
                    drill_x += 1
                    danger_list.append( create_coordinate(drill_x, drill_y) )   
                else:
                    not_danger = False
                    break
                    
            if not_danger:
                user_point_list.append(create_coordinate(drill_x, drill_y) + " Safe")

            else:
                user_point_list.append( create_coordinate(original_drillx + length, drill_y) + " DANGER!!!" )
                break
            
        if direction.lower() == "l":
            
            for count in range(length):
                
                if allowed_to_drill(  create_coordinate(drill_x - 1, drill_y) ):                                          

                    danger_list.append( create_coordinate(drill_x - 1, drill_y) )
                    drill_x -= 1
                else:
                    not_danger = False
                    break
                    
            if not_danger:
                user_point_list.append(create_coordinate(drill_x,drill_y) + " Safe")
            else:
                user_point_list.append( create_coordinate(original_drillx - length, drill_y) + " DANGER!!!" )
                break
            
for index in user_point_list:
    print(index)

