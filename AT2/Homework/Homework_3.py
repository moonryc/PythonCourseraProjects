import math


#Question 1
A = [5,4,3,6,7]
count = 0
for i in range(len(A)):
    for j in range(len(A)):
        if i != j and i < j:
            if A[i]> A[j]:
                count+=1
print 'Question 1: ',count

#question 2
B = [5,4,3,2,1]
count = 0
for i in range(len(B)):
    for j in range(len(B)):
        if i != j and i < j:
            if B[i]> B[j]:
                count+=1
print 'Question 2: n/2*(n-1)',count

#Question 3
print 'Question 3: n^2'

#question 4

def count_inversion(array):
    if len(array) <= 1:
        return 0
    else:
        array_one = array[0:(len(array)/2)]
        array_two = array[len(array)/2:]
        il= count_inversion(array_one)
        ir= count_inversion(array_two)
        im = merge(array_one,array_two,array)
    return il+ir+im


def merge(array_one, array_two,original_array):
    count = 0
    i, j, k = 0,0,0
    p = len(array_one)
    q = len(array_two)
    while i < p and j < q:
        if array_one[i] <= array_two[j]:
            original_array[k] = array_one[i]
            i+=1
        else:
            original_array[k] = array_two[j]
            j+=1
            count += p - i
        k+=1
    if i == p:
        A[k:] = array_two[j:]
    else:
        A[k:] = array_two[i:]
    
    return count

print 'Question 4: ', count_inversion(B)

#Question 5
print 'Question 5: T(n)=2T(n/2)+O(n)'

#Question 6
a_q6 = 4
b_q6 = 2
c_q6 = 1

d_q6 = 1
answer_6 = ''

if a_q6<b_q6**d_q6:
    answer_6 = 'O(n^{}'.format(d_q6)
elif a_q6 == b_q6**d_q6:
    answer_6 = 'O(n^{}log(n)'.format(d_q6)
else:
    answer_6 = 'O(n^log_{}({}))'.format(b_q6,a_q6)

print 'Question 6 = {}'.format(answer_6), 'evaluates to O(n^2) '

#question 7
a_q7 = 4
b_q7 = 2
c_q7 = 1

d_q7 = 3
answer_7 = ''

if a_q7<b_q7**d_q7:
    answer_7 = 'O(n^{})'.format(d_q7)
elif a_q7 == b_q7**d_q7:
    answer_7 = 'O(n^{}log(n)'.format(d_q7)
else:
    answer_7 = 'O(n^log_{}({}))'.format(b_q7,a_q7)

print 'Question 7 = {}'.format(answer_7), ''

#Question 8
def mystery_function(sorted_array, left, right):
    if left > right:
        return -1
    m = int(math.floor((left+right)/2))
    if sorted_array[m] == m:
        return m
    else:
        if A[m] < m:
            return mystery_function(sorted_array, m+1, right)
        else:
            return mystery_function(sorted_array, left, m-1)

print 'Question 8:',mystery_function([-2,0,1,3,7,12,15],0,6)

#Question 9
print 'Question 9: Returns i if there exists an i such that A[i]=i, and -1 otherwise.'

#Question 10
#I think this is correct
print 'Question 10: semi guess on the best case to be O(1) and worst case to be O(log(n))'

#question 11
#need to ask for help on this one
print 'Question 11: TBD'

#Question 12

print 'Question 12: 2^(n-1)-1'

#Question 13
#need to come back to this
print 'Question 13: O(n^2 +h(n)*n)'

#Question 14
# need to revisit
print 'Question 14: O(q*(n)*k)'

#Question 15
#fairly certain that this is the answer
print 'Question 15: TBD'

#Question 16
#fairly certain that this is the answer because n*n for the 2 for loops no reason to have n^3
print 'Question 16: O(n^2)'

#Question 17
#gonna come back to this but I feel like this is right
print 'Question 17: T(n)=2T(n/2)+f(n)' +'\n' + '             T(2)=d'

#Question 18
#This is not the answer
print 'Question 18: TBD'

#Question 19
#somehow this is not the answer
a_q19 = 2
b_q19 = 2


d_q19 = 1
answer_19 = ''

if a_q19<b_q19**d_q19:
    answer_19 = 'O(n^{})'.format(d_q19)
elif a_q19 == b_q19**d_q19:
    answer_19 = 'O(n^{}log(n)'.format(d_q19)
else:
    answer_19 = 'O(n^(log_{}({})))'.format(b_q19,a_q19)

print 'Question 19: {}'.format('TBD')


#Question 20
#Correct
a_q20 = 2
b_q20 = 2


d_q20 = 1
answer_20 = ''

if a_q20<b_q20**d_q20:
    answer_20 = 'O(n^{})'.format(d_q20)
elif a_q20 == b_q20**d_q20:
    answer_20 = 'O(n^{}log(n)'.format(d_q20)
elif a_q20> b_q20**d_q20:
    answer_20 = 'O(n^(log_{}({})))'.format(b_q20,a_q20)

print 'Question 20: {}'.format(answer_20)
