"""
This is a docstring for the method:

Line to Merge the bottom row from left to right.
"""

def merge(line):
    """
    This is for combinding the number in the array from right to left 2048
    """
    new_line = list(line)
    answer_line = []
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
    print answer_line
    return answer_line
    

merge([2,2,0,4,0,4,8])
