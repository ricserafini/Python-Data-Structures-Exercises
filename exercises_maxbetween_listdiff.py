#%% EXERCISE 1

def max_between (list, index1, index2):

    chunk = []
    chunk = list[index1:index2+1]
    maximum = chunk[0] 
    for elem in chunk:
        if elem > maximum:
            maximum = elem

    return "The biggest number between the indices is " + str(maximum)

test = [3,4,8,2,6,0,9]
max_between(test,1,4)

#Initially we had used the max function to find the element, but now we use
#a loop to parse each element.
#The way to make it a faster implementation - would be to just access the
#last element in the chunk as the list will be sorted. They will not be a 
#need for a loop to parse each element.

#%% EXERCISE 3

def intersection(a, b):
    inter = []
    for element in a:
        if element in b:
            if element not in inter:
                inter.append(element)
    return inter    

print(intersection([1,2,3,4,1,2,3,4], [3,4,5,6]))

#  
#
#
#%% EXERCISE 5
def dictionary_lookup(my_dict, my_word):
    for defn in my_dict:
        if defn["word"] == my_word:
            return defn["definition"]
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

#The worst case runtime for the algorithm would be O(n)
#as there is 1 for-loop in the function definition. 
#If the dictionary element is the last one present in the list, 
# it would take n iterations to retrieve its definition or n iterations 
# to find that the element does not exist in the list.

#%% Exercise 4 Difference

list_1 = [1, 2, 4]
list_2 = [4, 5, 6]

def list_diff(list_1, list_2):
    difference = list_1
    for element in list_2:
        if element in difference:
            difference.remove(element)
        else:
            difference.append(element)

    return difference

print(list_diff(list_1,list_2))

#%%

# The code we proposed to solv ex.4 is using a linear search;
# In particular, Python uses a linear search each time we 
# input a "in" statement. 
# As we know, linear search has a complexity of O(n), 
# Which in our case can be considered slow. 
# To implement a faster and more efficient algorithm, 
# We could implement a binary search, having a 
# complexity of O(logn) when the list is sorted.



