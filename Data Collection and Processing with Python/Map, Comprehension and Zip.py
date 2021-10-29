"""
MAP
You previously were introduced to accumulating a list by transforming each of the elements. Here we revisit that pattern.
The following function produces a new list with each item in the original list doubled.
It is an example of a mapping, from the original list to a new list of the same length, where each element is doubled.
"""

def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)


"""
As we did when passing a function as a parameter to the sorted function, we can specify a function to pass to map either
by referring to a function by name, or by providing a lambda expression.
"""
def triple(value):
    return value*3

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)


#Of course, once we get used to using the map function, it’s no longer necessary to define functions like tripleStuff and quadrupleStuff.

things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))

#Use map to produce a new list called abbrevs_upper.

abbrevs=["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
def f(st):
    return st.upper()
abbrevs_upper=map(lambda value:value.upper(),abbrevs)
print(list(abbrevs_upper))

#Filter

#The map method is used to convert each item of an array,
# while the filter method is used to select certain items of an array.
print(list(filter(lambda num:num%2==0, [2,3,4,5,6,7,8])))
print(list(filter(lambda word:'o' in word, ["witch", "halloween", "dragon", "moon"])))


#List Comprehensions

thing=[2,5,9]
lis1=[value * 2 for value in things]
print(lis1)

## keep even function with list comprehension
def keep_evens(nums):
    new_list=[num for num in nums if num%2==0]
    return new_list

print(keep_evens([1,2,3,4,5,6]))

# function tthat return the words with 4 characters

def lengt(string):
    new_list=[word for word in string if len(word)>=4]
    return new_list
print(lengt(['a','holaa','jesus','python']))

#ZIP FUNCTION

#  Combines the elements of the same position

L1=[1,2,3]
L2=[4,5,6]
#L3=[x1+x2 for (x1, x2) in list(zip(L1,L2))]
L3=list(x1+x2 for (x1,x2) in list(zip(L1,L2)))
print(L3)

#Assesment
'''
Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element using mapping.
'''


lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing=map((lambda word:"Fruit: "+word),lst_check)
print(map_testing)


'''
Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.
'''

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries=list(filter(lambda word:word[0]=='B',countries))
print(b_countries)


'''
Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.
'''

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names=[name[1] for name in people]

print(first_names)


'''
Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.
'''

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

l3 = zip(l1, l2)
opposites = list(filter(lambda s: len(s[0])>3 and len(s[1])>3, l3))


'''
Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.
'''

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info=zip(species,population)
endangered=[l[0] for l in pop_info if l[1]<2500]
