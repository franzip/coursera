from mat import Mat
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat(({i for i in labels}, {j for j in labels}), {(i,i): 1 for i in labels})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    temp = identity()
    for (first,second,third) in temp.D:
        temp.f[(first,third)] = x
        temp.f[(second,third)] = y
    return temp
        

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    temp = identity()
    for (first,second,third) in temp.D:
        temp.f[(first,first)] = b
        temp.f[(second,second)] = a
    return temp

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    temp = identity()
    for (first,second,third) in temp.D:
        temp.f[(first,first)] = math.cos(angle)
        temp.f[(first,second)] = -1 * math.sin(angle)
        temp.f[(second,first)] = math.sin(angle)
        temp.f[(second,second)] = math.cos(angle)
    return temp

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y)*rotation(angle)*translation(-x,-y)

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    temp = identity()
    for (first,second,third) in temp.D:
        temp.f[(first,first)] = -1
    return temp

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    temp = identity()
    for (first,second,third) in temp.D:
        temp.f[(second,second)] = -1
    return temp
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    return Mat(({'r','g','b'},{'r','g','b'}),{('r','r'):scale_r,('g','g'):scale_g,('b','b'):scale_b})

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    return rowdict2mat({color:Vec({'r','g','b'},{'r':77/256,'g':151/256,'b':28/256}) for color in {'r','g','b'}})   

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


