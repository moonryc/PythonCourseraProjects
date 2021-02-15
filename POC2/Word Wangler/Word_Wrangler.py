"""
Student code for Word Wrangler game
"""
# only runs on codeskulptor.org
import urllib2
import codeskulptor
import poc_wrangler_provided as provided
import math

WORDFILE = "assets_scrabble_words3.txt"

# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.
    Returns a new sorted list with the same elements in list1, but
    with no duplicates.
    This function can be iterative.
    """
    location = len(list1)-1
    ans = list(list1)
    if location == 0:
        return ans
    else:
        if ans[location] == ans[location - 1]:
            ans.pop(location)
            return remove_duplicates(ans)
        else:
            return remove_duplicates(ans[:location])+ans[location:]

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.
    Returns a new sorted list containing only elements that are in
    both list1 and list2.
    This function can be iterative.
    """
    my_list=[]
    if list1 == [] and list2 ==[]:
        return my_list
    elif list1 !=[] and list2 == []:
        return my_list
    elif list1 ==[] and list2 != []:
        return my_list
    if list1 != [] and list2 != []:
        if list1[0] > list2[0]:
            return intersect(list1,list2[1:])
        elif list1[0] < list2[0]:
            return intersect(list1[1:],list2)    
        elif list1[0] == list2[0]:
            my_list.append(list1[0]) 
            my_list+= intersect(list1[1:],list2[1:])
    return my_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.
    Returns a new sorted list containing those elements that are in
    either list1 or list2.
    This function can be iterative.
    """
    ans = list(list1)+list(list2)
    left_increment=0
    right_increment=0
    ans_increment=0
    while left_increment < len(list1) and right_increment < len(list2):
        if list1[left_increment] < list2[right_increment]:
            ans[ans_increment] = list1[left_increment]
            left_increment+=1
        else:
            ans[ans_increment] = list2[right_increment]
            right_increment+=1
        ans_increment+=1
    while left_increment < len(list1):
        ans[ans_increment] = list1[left_increment]
        left_increment+=1
        ans_increment+=1
    while right_increment < len(list2):
        ans[ans_increment] = list2[right_increment]
        right_increment+=1
        ans_increment+=1
    return ans
                
def merge_sort(list1):
    """
    Sort the elements of list1.
    Return a new sorted list with the same elements as list1.
    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1
    else:
        center = int(math.ceil((len(list1)-1)/2.0))
        left, right = list1[:center], list1[center:]    
        return merge(merge_sort(left),merge_sort(right))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [""]
    first = word[0]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)
    answer = []
    print rest_strings
    for item in rest_strings:
        for ind in range(len(item) + 1):
            answer.append(item[:ind] + first + item[ind:])
    return rest_strings + answer

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    word_dictionary = urllib2.urlopen(url)
    words= []
    #[words.append(line[:-1]) for line in word_dictionary.readlines()]
    return words 

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()
    
    