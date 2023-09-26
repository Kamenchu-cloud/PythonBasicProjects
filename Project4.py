List_one = [[1,2,3,4],[5,6,7,8],[9,1,3,3]]
List_two = [[4,3,2,1], [9,7,6,5],[9,2,3,5]]
List_three = [[1,3,5,7],[9,1,3,5],[7,9,1,3]]

def main():
    # Print row [5,6,7,8]
    print(List_one[1], " :row [5, 6, 7, 8]")
    
    # Print value 9 
    print(List_one[2][0], " :Value on the 3rd row, first column")
    
    # Insert a new row on 3rd index. [3,5,6,4]
    List_one.insert(2, [3,5,6,4])
    
    # Insert the value 5 on the row on index 0
    List_one[0].append(5)
    
    # Update the value 8 to 0
    List_one[1][3] = 0
    
    # Delete the row on index 1
    del(List_one[1])
    
    # Find the sum of list_two and list_three using a nested loop
    for x in List_two:
        for y in List_three:
            result = List_two + List_three
            print (result)
    
    
if __name__ == "__main__":
    main()
