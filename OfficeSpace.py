#  File: OfficeSpace.py

#  Description: Program sets up system that lets employees request office space;
#   calculates the unused space, contested space, and uncontested space

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/8/22

#  Date Last Modified: 2/11/22

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle

def area (rect):

    lst = list(rect)
    x1 = lst[0]
    y1 = lst[1]
    x2 = lst[2]
    y2 = lst[3]
    
    return (x2 - x1) * (y2 - y1)

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap

def overlap (rect1, rect2):
    
    # rectangles do not overlap if any of the following conditions occur:
    # 1. The top edge of one rectangle is below the bottom edge of the other rectangle
    # 2. The right edge of one rectangle is to the left of the left edge of the other rectangle
    
    if (rect1[1] > rect2[3] and rect1[3] > rect2[1]) or (rect2[1] > rect1[3] and rect2[3] > rect1[1]) or (rect1[2] > rect2[0] and rect1[0] > rect2[2]) or (rect2[2] > rect1[0] and rect2[0] > rect1[2]):
        return (0, 0, 0, 0)
    else:
        x2 = min(rect1[2], rect2[2])
        y2 = min(rect1[3], rect2[3])
        x1 = max(rect1[0], rect2[0])
        y1 = max(rect1[1], rect2[1])
    
    return (x1, y1, x2, y2)
        
        

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):

    area = 0 # instantiate area variable at 0
    
    for row in range(len(bldg)): # traverse each row of office space
        for column in range(len(bldg[row])): # traverse each column in each row of office space
            if bldg [row][column] == 0:
                area += 1 # add 1 to area if that particular coordinate is not requested
    return area   

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):

    area = 0 # instantiate area variable at 0

    for row in range(len(bldg)): # traverse each row of office space
        for column in range(len(bldg[row])): # traverse each column in each row of office space
            if not bldg [row][column] == 0 and not bldg [row][column] == 1:
                area += 1 # add 1 to area if that particular coordinate is contested

    return area

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):

    area = 0 # instantiate area variable at 0
    
    for row in range(int(rect[1]), int(rect[3])): # traverse each row of office space requested by employee
        for column in range(int(rect[0]), int(rect[2])): # traverse each column in each row of office space, as requested by employee
            if bldg [row][column] == 1:
                area += 1 # add 1 to area if that particular coordinate is only requested by this particular employee
    
    return area

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):

    officespace = []
    
    for row in range(office[3]): # create rows according to the specified height
        lst = []
        for column in range(office[2]): # create columns according to the specified width
            lst.append(0)
        officespace.append(lst)
        
    for employee in cubicles: # check all coordinates requested by employees
        for row in range(int(employee[1]), int(employee[3])): # traverse rows requested by employee
            for column in range(int(employee[0]), int(employee[2])): # traverse columns requested by employee
                officespace[row][column] += 1 # add 1 to the corresponding coordinate
    
    return officespace
    
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
    
    assert area ((0, 0, 1, 1)) == 1
    assert area ((0, 0, 0, 0)) == 0
    
    assert overlap ((2, 1, 5, 5), (3, 2, 6, 7)) == (3, 2, 5, 5)
    assert overlap ((3, 2, 6, 7), (2, 1, 5, 5)) == (3, 2, 5, 5)
    assert overlap ((1, 3, 4, 6), (3, 1, 5, 4)) == (3, 3, 4, 4)
    
    assert unallocated_space([[1, 2, 3], [3, 2, 1]]) == 0
    assert unallocated_space([[1, 0, 2], [1, 2, 0], [0, 1, 2]]) == 3
    
    assert contested_space([[1, 0, 2], [1, 2, 0], [0, 1, 2]]) == 3
    
    assert uncontested_space([[1, 2, 0], [1, 0, 2], [0, 1, 2]], (0, 1, 3, 3)) == 2
    
    
   
    
    # write your own test cases

    return "all test cases passed"

def main():
    
    import sys

    # read the data
    [width, height] = sys.stdin.readline().split()
    office = (0, 0, int(width), int(height))

    cubicles = []
    names = []
    numberofemployees = sys.stdin.readline()
    for employee in range(int(numberofemployees)):
        [name, x1, y1, x2, y2] = sys.stdin.readline().split()
        names.append(name)
        tuple = (x1, y1, x2, y2)
        cubicles.append(tuple)

    # create list of integers to represent the office and how many employees request each space
    requestedofficespots = request_space(office, cubicles)
  
    # run your test cases
    '''
    print (test_cases())
    '''

    # print the following results after computation:

    # compute the total office space
    print("Total", area(office))

    # compute the total unallocated space
    print("Unallocated", unallocated_space(requestedofficespots))

    # compute the total contested space
    print("Contested", contested_space(requestedofficespots))

    # compute the uncontested space that each employee gets

    i = 0 # instantiate counter to keep track of which name to print from list of employee names
    
    for request in cubicles:
        uncontestedspace = uncontested_space(requestedofficespots, request)
        print(names[i], uncontestedspace)
        i += 1

if __name__ == "__main__":
  main()
  

  


