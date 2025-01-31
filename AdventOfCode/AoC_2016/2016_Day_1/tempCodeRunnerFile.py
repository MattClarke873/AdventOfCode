 if (current_x,current_y) in visited: 
            print (abs(current_x) + abs(current_y))
        else:
            visited.add((current_x,current_y))