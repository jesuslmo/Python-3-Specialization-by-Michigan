"""
Remember that the key function always takes as input one item from the sequence and returns a property of the item.
In our case, the items to be sorted are the dictionary’s keys, so each item is one key from the dictionary.
To remind ourselves of that, we’ve named the parameter in tha lambda expression k.
The property of key k that is supposed to be returned is its associated value in the dictionary. Hence, we have the lambda expression lambda k: d[k].
"""

L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

y = sorted(d.keys(), key=lambda k: d[k], reverse=True)
for k in y:
    print("{} appears {} times".format(k, d[k]))


"""
Here, each word is evaluated first on it’s length, then by its alphabetical order.
Note that we could continue to specify other conditions by including more elements in the tuple.
What would happen though if we wanted to sort it by largest to smallest, and then by alphabetical order?
"""

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name), reverse=True)
for fruit in new_order:
    print(fruit)

"""
Here, we’ve done the lookup right in the lambda expression, which makes it a little bit clearer that we’re just sorting the keys of the states dictionary based on a property oftheir values.
It also makes it easier to reuse the counting function on other city lists, even if they aren’t embedded in that particular states dictionary.
"""

def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))

"""
Sorting by the first item in the value of the keys in states
"""

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: len(states[state][0])))

#Assessment
"""
Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
"""

letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters=[]
def sorted_letter(x):
    for i in x:
        sorted_letters.append(i)
    return sorted_letters.sort(reverse=True)
sorted_letter(letters)

"""
Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.
"""

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

top_all=sorted(medals,key=lambda x:medals[x],reverse=True)
top_three=top_all[:3]

"""
We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.
"""

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed=sorted(groceries,key=lambda x:groceries[x],reverse=True)

"""
Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. 
Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
"""

idsl=[]
def last_four(x):
    return str(x)[-4::]
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids=sorted(ids,key=lambda x:last_four(x))


"""
Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.
"""

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id=sorted(ids,key=lambda id:str(id)[-4::])

"""
Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.
"""

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort=sorted(ex_lst, key=lambda word:word[1])

"""
Final assessment
Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet).
Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. 
Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), 
Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. 
The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets
"""

def strip_punctuation(x):
    for i in x:
        if i in punctuation_chars:
            x=x.replace(i,"")
    return x
def get_pos(x):
    pos=0
    x=strip_punctuation(x)
    words=x.split()
    for i in words:
        if i.lower() in positive_words:
            pos+=1
    return pos
def get_neg(x):
    pos=0
    x=strip_punctuation(x)
    words=x.split()
    for i in words:
        if i.lower() in negative_words:
            pos+=1
    return pos
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
outfile = open("resulting_data.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
outfile2 = open("project_twitter_data.csv", "r")
row=outfile2.readlines()[1::]
for line in row:
    text=line.split()
    numbr=line.split()[-1]
    rettwts=numbr.split(",")[1]
    replies=numbr.split(",")[2]
    neg=0
    pos=0
    for i in text:
        i=strip_punctuation(i)
        if i in negative_words:
            neg+=1
        if i in positive_words:
            pos+=1
    net_sco=pos-neg
    data="{}, {}, {}, {}, {}".format(rettwts,replies,pos,neg,net_sco)
    outfile.write(data)
    outfile.write('\n')