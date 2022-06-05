# -*- coding: utf-8 -*-

def string_to_list_of_words(my_string):
    
    my_new_list = my_string.split(" ")
    return my_new_list

my_string = string_to_list_of_words("The government is to suspend competition law to allow oil firms to target fuel deliveries at petrol stations following recent panic buying")
    
print(my_string)    


def calculate_frequencies(list_of_words):
     
    my_dict = {}
 
    for word in list_of_words:
        if word not in my_dict:
            my_dict[word] = 1
        else:   
            my_dict[word] =  my_dict[word] + 1    
    return my_dict

my_words = calculate_frequencies(my_string)
        
print(my_words)

def display_frequencies(my_frequencies):
    
    for frequence in my_frequencies.items():
        
        """
        stars = ""
        
        for n in range(frequence[1]):
            stars += "*" 
        
        print(frequence[0] + " | " + stars)
        """
        
        print(frequence[0] + " | " + ("*" * frequence[1]))
 
        
display_frequencies(my_words) 
