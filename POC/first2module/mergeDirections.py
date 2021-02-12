"""
THIS IS LIKLY GO UNUSED
"""


def right_or_left(line,direction):
    """
    This is for combinding the number in the array for left or right 2048
    """
    new_line = list(line)
    answer_line = []
    if direction == 'right':
        new_line.reverse()
    for zero_check in line:
        if zero_check == 0:
            new_line.remove(0)
    value = 0
    while value <= len(new_line):
        if value == len(new_line)-1:
            answer_line.append(new_line[value])
            break
        if value == len(new_line):
                break
        elif new_line[value] == new_line[value+1]:
            answer_line.append(new_line[value]*2)
            value += 2
        else:
            answer_line.append(new_line[value])
            value+=1

    for dummy_zero in range(len(line) - len(answer_line)):
        answer_line.append(0)
    if direction == 'right':
        answer_line.reverse()
    print (answer_line)
    return answer_line
    

#right_or_left([2,2,0,4,0,4,8],'left')


def up_or_down(line,direction):
    """
    This is for combinding the number in the array for left or right 2048
    """
    new_line = []
    answer_line=[]
    for dummy_index in range(len(line)):
        new_line.append(line[dummy_index][0])
    if direction == 'right':
        new_line.reverse()
    for zero_check in line:
        if zero_check == 0:
            new_line.remove(0)
    value = 0
    while value <= len(new_line):
        if value == len(new_line)-1:
            answer_line.append(new_line[value])
            break
        if value == len(new_line):
                break
        elif new_line[value] == new_line[value+1]:
            answer_line.append(new_line[value]*2)
            value += 2
        else:
            answer_line.append(new_line[value])
            value+=1

    for dummy_zero in range(len(line) - len(answer_line)):
        answer_line.append(0)
    if direction == 'down':
        answer_line.reverse()
    print (answer_line)
    
up_or_down([[2,1,3],
            [2,5,6],
            [4,8,9]],'right')


# def direction(the_array):
#     temp_line=[]
#     for value in line:
#         if value != 0:
#             temp_line.append(value)
            

myArray = [0,1,2,3]

# while i < len(myArray):
#     pass
    

