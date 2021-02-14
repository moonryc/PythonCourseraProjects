"""
Student code for Word Wrangler game
"""

import urllib2
import simpleguitk as simplegui
import poc_wrangler_provided as provided
import math

#WORDFILE = "assets_scrabble_words3.txt"
WORDFILE = 'http://codeskulptor-assets.commondatastorage.googleapis.com/assets_scrabble_words3.txt'


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.
    Returns a new sorted list with the same elements in list1, but
    with no duplicates.
    This function can be iterative.
    """

    #first is a test to get it working in the most simple fashion

    return set(list1)

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.
    Returns a new sorted list containing only elements that are in
    both list1 and list2.
    This function can be iterative.
    """



    return []

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.
    Returns a new sorted list containing those elements that are in
    either list1 or list2.
    This function can be iterative.
    """
    ans = list(list1)+list(list2)
    i=0
    j=0
    k=0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            ans[k] = list1[i]
            i+=1
        else:
            ans[k] = list2[j]
            j+=1
        k+=1
    while i < len(list1):
        ans[k] = list1[i]
        i+=1
        k+=1
    while j < len(list2):
        ans[k] = list2[j]
        j+=1
        k+=1
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
    ans=[]
    blank = [()]
    for index in range(len(list(word))):
        for x in x:
            ans = blank +[]
    return []

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

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
# run()

    
#make sure it is alphabetical order
#add all strings that include first at any position in the generated strings
