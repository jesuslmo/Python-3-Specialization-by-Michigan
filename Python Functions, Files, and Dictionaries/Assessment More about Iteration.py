"""
Write a function, sublist, that takes in a list of numbers as the parameter. In the function,
use a while loop to return a sublist of the input list.
The sublist should contain the same values of the original
list up until it reaches the number 5 (it should not contain the number 5).
"""
def sublist(x):
    sub = []
    x = (num for num in x)
    num = next(x, 5)
    while num != 5:
        sub.append(num)
        num = next(x, 5)
    return sub

"""
Write a function called check_nums that takes a list as its parameter, 
and contains a while loop that only stops once the element of the list is the number 7.
What is returned is a list of all of the numbers up until it reaches 7.
"""
def check_nums(list):
    i=0
    New_list=[]
    while i < len(list):
        if list[i] == 7:
            break
        New_list.append(list[i])
        i=i+1
    return New_list

"""
Write a function, sublist, that takes in a list of strings as the parameter. 
In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until
 it reaches the string “STOP” (it should not contain the string “STOP”).
 """
def sublist(list):
    i=0
    list2=[]
    while i < len(list):
        if list[i]=="STOP":
            break
        list2.append(list[i])
        i+=1
    return list2

"""
Challenge: Write a function called beginning that takes a list as input
and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list
that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element,
the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
"""
def beginning(list):
    i=0
    list2=[]
    while i<len(list) :
        if list[i]=="bye":
            break
        if len(list2)<10:
            list2.append(list[i])
        i+=1
    return list2