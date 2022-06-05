
"""
Helper Function Binary Search.
"""

def binary_search(lst, value):

   left_pivot = 0
   right_pivot = len(lst) - 1

   middle = (right_pivot + left_pivot) // 2


   while left_pivot <= right_pivot:
       middle = (right_pivot + left_pivot) // 2

       if lst[middle] == value:
           return True

       elif lst[middle] < value:
           left_pivot = middle + 1

       else:
           right_pivot = middle - 1

   return False



"""
Exercise 1
**(2 points) maximum value between two indices**.

Create a function called `max_between` that takes an unsorted list and two
indices and returns what's the maximum in the segment contained between those
two indices.

Can you think of a faster implementation of your algorithm if you're ensured
that the list is sorted?  Reason it in a comment after the function.
"""

# Assume that <<between those two indices>> refers to a sub-list, including the elements at the indices.

# Time complexity: 0(n)

def max_between(my_list, index_0, index_1):
    if len(my_list) < 1:
        return None
    if index_0 > index_1:
        # if index_0 happens to be greater than index_1, switch indices.
        index_0, index_1 = index_1, index_0
    if index_1 > len(my_list):
        return "Indix out of Range."

    short_list = my_list[index_0:index_1 + 1]
    
    max = - float("inf")

    for number in short_list:
        if number > max:
            max = number
        
    return max
    
my_list = [1, 12, 12]
#print(max_between(my_list, 1, 2))

# If the list was sorted, we would first have to check whether the list is ascending or descending
# Then we check if the first value in the short_list is smaller or bigger than the last value in the list,
# then we would return the bigger element.


# Implementation, without checking for correct user input, would look like:
# Time complexity: 0(1) - constant

def max_between_sorted(sorted_list, left, right):
    if sorted_list[left] > sorted_list[right]:
        return sorted_list[left]
    else:
        return sorted_list[right]

#my_sorted_test_list = [1, 2, 3, 4]
#print(max_between_sorted(my_sorted_test_list, 0, 2))



"""
Exercise 2
**(2 points) value appears in both lists**.

Create a function `appears_in_both` that receives two unsorted lists and one
integer. The function should return True if the integer appears in both lists
and False otherwise.

Create another version of the function in which the lists are sorted.

"""


# O(n)
def appears_in_both(unsorted_1, unsorted_2, my_int):
    if my_int in unsorted_1 and my_int in unsorted_2:
        return True
    else:
        return False

#unsorted_test_list_1 = []
#unsorted_test_list_2 = []

#print(appears_in_both(unsorted_test_list_1, unsorted_test_list_2, 12))
    

# O(log(n))
# binary seach logic can be found at the top of this file.

def appears_in_both_sorted(sorted_1, sorted_2, my_int):

    if binary_search(sorted_1, my_int)  and binary_search(sorted_2, my_int):
        return True
    return False

#sorted_test_list_1 = [0, 1, 2, 3, 5]
#sorted_test_list_2 = [7, 5, 4, 3]

#print(appears_in_both_sorted(sorted_test_list_1, sorted_test_list_2, 5))





"""
Exercise 3
**(2 points) intersection**.

Create a function intersection that receives two lists as parameters and
returns the intersection of them (intersection meaning a list with the elements
they have in common).

Could you find a faster implementation if you're sure that the two lists you
receive are sorted?   Reason idt in a comment after the function.
"""

# O(n^2)
# note that we define intersection as a set of unique elements. 
# thus, elements that appear multiple times in both lists appear only once in the interesction list.
def intersection(unsorted_1, unsorted_2):

    intersection = []

    for int_1 in unsorted_1:
        for int_2 in unsorted_2:
            if int_1 == int_2 and int_1 not in intersection:
                intersection.append(int_1)
    return intersection

test_list_1 = [3, 4, 1, 7, 12]
test_list_2 = []

#print(intersection(test_list_1, test_list_2))


# Faster implementation give that both lists are sorted.
# create an empty list
# loop through unsorted_list 1
# use a more efficient search algorithm, for instance binary_search, to check if element is in unsorted_2.
# if yes, append to intersection. Instead of a list, use a set to keep track of all elements in intersection.
# else, continue.
# then we get complexity of n*log(n), which is more efficient than O(n^2) which is what we had with unsorted lists.
# an implementation can be found below.

# O(nlog(n))
def intersection_sorted(sorted_1, sorted_2):
    intersection = set()

    for integer in sorted_1:
        if binary_search(sorted_2, integer):
            intersection.add(integer)
    return list(intersection)

# sorted_test_list_1 = [9, 21, 234, 2535]
# sorted_test_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]

# print(intersection_sorted(sorted_test_list_1, sorted_test_list_2))

"""
Exercise 4

**(2 points) difference**.

Create a function difference that receives two lists as parameters and returns
the difference of them (difference meaning a list with the elements they don't
have in common).

could you find a faster implementation if you're sure that the two lists you
receive are sorted?   Reason it in a comment after the function.

"""

lst1 = [1,3,5,7,9,11,13,15]
lst2 = [1,2,3,4,5,6,7,8,9,10,11]

# O(n^2)
def difference(list1, list2):
    candidate = []
    for i in list1:
        if i not in list2:
            candidate.append(i)
    for i in list2:
        if i not in list1:
            candidate.append(i)
    return candidate


# In the case that the list are known to be sorted prior to being run through 
# the function, it would be more efficent to impliment a binary search when seeing
# if a certain value of one list is shared in another. This would change the runtime from 
# n^2, to log(n) (a better big O runtime)
# algorithm using binary search can be found below.

# O(nlog(n))

def difference_sorted(sorted_list1, sorted_list2):
    differences = []

    for element in sorted_list1:
        if not binary_search(sorted_list2, element):
            differences.append(element)
    
    for element in sorted_list2:
        if not binary_search(sorted_list1, element):
            differences.append(element)

    return differences

sorted_test_list_1 = [0, 2, 4, 6, 7, 10, 132]
sorted_test_list_2 = [-200, 0, 1, 2, 4]

print(difference_sorted(sorted_test_list_1, sorted_test_list_2))

# Question 5
"""
Exercise 5

**(2 points) dictionary search**.

Imagine we implemented a dictionary (the one with word
definitions, not Python`s dictionary) using a list of dictionaries, where each
internal dictionary represents a word. I.E:

(example dictionary)

Implement the function `dictionary_lookup` that receives the whole dictionary as
an ordered list and a word and returns the word's definition in case it exists.
It should return None in case the word doesn't exist.

Given the above dictionary, the function should behave as follows:

```python
dictionary_lookup(dictionary, "A") # returns 'the 1st letter of the English alphabet'
dictionary_lookup(dictionary, "Absent") # returns 'non-existent, lacking'
dictionary_lookup(dictionary, "Potato") # returns None
```

What's the worst case runtime for your algorithm?  Why so?  Please answer these
questions in comments after your implementation.

"""

def dictionary_lookup(my_dictionary, dict_word):

    for dictionary in my_dictionary:
        if dictionary["word"] == dict_word:
            return dictionary["definition"]
        return None

dictionary = [
    {
        "word": "A",
        "definition": "the 1st letter of the English alphabet"
    },
    {
        "word": "Absent",
        "definition": "non-existent, lacking"
    },
    {
        "word": "Battlestar Galactica",
        "definition": "Battlestar Galactica is an American science fiction media franchise created by Glen A. Larson. The franchise began with the original television series in 1978 and was followed by a short-run sequel series (Galactica 1980), a line of book adaptations, original novels, comic books, a board game, and video games. A re-imagined version of Battlestar Galactica aired as a two-part, three-hour miniseries developed by Ronald D. Moore and David Eick in 2003. That miniseries led to a weekly television series, which aired until 2009. A prequel series, Caprica, aired in 2010. "
    },
    {
        "word": "Bear",
        "definition": "any of a family (Ursidae of the order Carnivora) of large heavy mammals of America and Eurasia that have long shaggy hair, rudimentary tails, and plantigrade feet and feed largely on fruit, plant matter, and insects as well as on flesh"
    },
    {
        "word": "Beet",
        "definition": "The beetroot is the taproot portion of a beet plant,[1] usually known in Canada and the USA as beets while the vegetable is referred to as beetroot in British English, and also known as the table beet, garden beet, red beet, dinner beet or golden beet. It is one of several cultivated varieties of Beta vulgaris grown for their edible taproots and leaves (called beet greens); they have been classified as B. vulgaris subsp. vulgaris 'Conditiva' Group.[2]"
    }
]

print(dictionary_lookup(dictionary,"A"))
print(dictionary_lookup(dictionary,"Absent"))
print(dictionary_lookup(dictionary,"Potato"))

#Part 2 - If Binary search is not used

#The search for a word will be done by taking into account all the "words" in the dictonary and going through each of them.
#The worst case runtime for it will be O(N) as the code will go through each "word" in the dictionary and if it is the Nth word in the dictonary, it will take N iterations.
#The alternative to this code is by using a Binary search. If we use Binary search to find the word and give the definition, the time complexity for it would have been reduced by one level to O(Log N).

#Part 2 - If Binary search is used

#The search of the "word" in the dictionary can be done using a Binary search as the dictionary is sorted.
#If we use Binary search to find the word and give the definition, the time complexity for it is O(Log N).
#The reason for it because at each iteration of searching the "word" in the dictionary, the search efforts are divided by 2 / making it half and that makes the maximum number of iterations required to search the "word" become Log(N).



