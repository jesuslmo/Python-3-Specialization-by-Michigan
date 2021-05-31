"""
Again, python provides a module for doing this. The module is called json. We will be using two functions in this module, loads and dumps.
json.loads() takes a string as input and produces a python object (a dictionary or a list) as output.
Consider, for example, some data that we might get from Apple’s iTunes, in the JSON format:
"""

import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])


"""
The other function we will use is dumps. It does the inverse of loads. It takes a python object, typically a dictionary or a list, and returns a string, in JSON format.
It has a few other parameters. Two useful parameters are sort_keys and indent. When the value True is passed for the sort_keys parameter, the keys of dictionaries are output in alphabetic order with their values.
The indent parameter expects an integer. When it is provided, dumps generates a string suitable for displaying to people, with newlines and indentation for nested lists or dictionaries. 
For example, the following function uses json.dumps to make a human-readable printout of a nested data structure.
"""

import json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))


"""
For example, if you have a list of dictionaries, then each dictionary should have the same structure, meaning the same keys and the same type of value associated with a particular key in all the dictionaries.
The reason for this is because any deviation in the structure that is used will require extra code to handle those special cases.
The more the structure deviates, the more you will have to use special cases.
For example, let’s reconsider this nested iteration, but suppose not all the items in the outer list are lists.
"""

nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: {}".format(y))

"""
Now the nested iteration fails.
We can solve this with special casing, a conditional that checks the type.
"""

nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)

"""
Shallow and Deep copies
Earlier when we discussed cloning and aliasing lists we had mentioned that simply cloning a list using [:] would take care of any issues with having two lists unintentionally connected to each other.
That was definitely true for making shallow copies (copying a list at the highest level), but as we get into nested data, and nested lists in particular, the rules become a bit more complicated.
We can have second-level aliasing in these cases, which means we need to make deep copies.

When you copy a nested list, you do not also get copies of the internal lists. This means that if you perform a mutation operation on one of the original sublists, the copied version will also change.
We can see this happen in the following nested list, which only has two levels.

Assuming that you don’t want to have aliased lists inside of your nested list, then you’ll need to perform nested iteration.
"""

original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item)
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)

# Or, equivalently, you could take advantage of the slice operator to do the copying of the inner list.

original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = inner_list[:]
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)

"""
This process above works fine when there are only two layers or levels in a nested list. However,
if we want to make a copy of a nested list that has more than two levels, then we recommend using the copy module. 
In the copy module there is a method called deepcopy that will take care of the operation for you.
"""

import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)

"""
Extracting from Nested Data
Now, we may want to go back have it extract for all the items rather than only the first item in res2.
"""

import json
# print(type(res))
# print(res.keys())
res2 = res['statuses']
#print("----Level 2: a list of tweets-----")
#print(type(res2)) # it's a list!
#print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2:
   #print("----Level 3: a tweet----")
   #print(json.dumps(res3, indent=2)[:30])
   res4 = res3['user']
   #print("----Level 4: the user who wrote the tweet----")
   #print(type(res4)) # it's a dictionary
   #print(res4.keys())
   print(res4['screen_name'], res4['created_at'])

#its the same as
for res3 in res['statuses']:
    print(res3['user']['screen_name'], res3['user']['created_at'])


#Assessment

#Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary to the list US_count.

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
US_count=[]
for i in nested_d:
    US_count.append(nested_d[i]['USA'])

# Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third=[]
for i in l_of_l:
    third.append(i[2])

#Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it contains the letter “t”.
#If it does not contain the letter “t”, save the athlete name into list other.

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t=[]
other=[]
for l in athletes:
    for at in l:
        if 't' in at:
            t.append(at)
        else:
            other.append(at)
