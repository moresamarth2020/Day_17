#!/usr/bin/env python
# coding: utf-8

# # Python Lists
# - Lists are ordered collection of data items.
# - They store multiple items in a single variable.
# - List items are separated by commas and enclosed within square brackets [].
# - Lists are changeable meaning we can alter them after creation.
# - Example 1:

# In[5]:


l = [1,2,3,4,5]
print(l)


# In[8]:


print(type(l))


# In[27]:


lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)


# In[28]:


details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
#As we can see, a single list can contain items of different data types.


# ## List Index
# - Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

# In[26]:


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors)


# ## Accessing list items
# We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...
# #### Positive Indexing:
# As we have seen that list items have index, as such we can access items using these indexes.
# - Example:

# In[29]:


marks = [25, 26, 35, 28, 30]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])


# In[31]:


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])


# ### Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.
# - Example:

# In[34]:


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])


# In[35]:


marks = [25, 26, 35, 28, 30]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3]) #Total count - 3 = 2 that is 0,1,2 so answer is 35
#or
print(marks[len(marks)-3])


# ### Check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.

# In[38]:


lis2 = [1,2,3,4,5,6,7,8,9]
if 7 in lis2:
    print("Yes")
else:
    print("No")


# In[39]:


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")


# In[43]:


lis2 = [1,2,3,4,5,6,7,8,9]
if "7" in lis2:
    print("Yes")
else:
    print("No")


# ### Range of Index:
# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.
# ### Example: printing elements within a particular range:

# In[44]:


lis2 = [1,2,3,4,5,6,7,8,9]
print(lis2) #print all the elements


# In[ ]:


#print all the elements
print(lis2[:])


# In[50]:


#printing elements within a particular range
print(lis2[1:9])


# In[51]:


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'


# ### Example: printing all element from a given index till the end

# In[64]:


lis2 = [1,2,3,4,5,6,7,8,9]
print(lis2[4:])


# In[65]:


print(lis2[-4:])
#or
print(lis2[len(lis2)-4:])


# In[66]:


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes


# ### Example: printing all elements from start to a given index

# In[72]:


li = [1,2,3,4,5,6,7,8,9]
print(li[:4])
print(li[:-4])
#or
print(li[:len(li)-4])


# In[73]:


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes


# ## jump Index

# In[75]:


lis = [1,2,3,4,5,6,7,8,9]
print(lis[0:8])


# In[76]:


print(lis[0:8:1])


# In[78]:


print(lis[0:8:2])


# In[81]:


print(lis[0:8:3])


# ### Example: Printing alternate values

# In[82]:


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes


# In[89]:


lis = [1,2,3,4,5,6,7,8,9]
print(lis[::])
print(lis[::8])#alternate values
print(lis[-8:6])
print(lis[-8:6:2])#alternate values.


# Here, we have not provided start and index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed.

# ### Example: printing every 3rd consecutive value withing a given range

# In[90]:


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])


# Here, jump index is 3. Hence it prints every 3rd element within given index.

# ### List Comprehension
# - List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
# - Syntax: List = [Expression(item) for item in iterable if Condition]
# - Expression: It is the item which is being iterated.
# - Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# - Condition: Condition checks if the item should be added to the new list or not.

# In[98]:


lst = [i for i in range(4)]
print(lst)


# In[99]:


lst = [i*i for i in range(4)]
print(lst)


# In[102]:


lst = [i*i for i in range(10) if i%2==0]
print(lst)


# #### Example 1: Accepts items with the small letter “o” in the new list

# In[103]:


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)


# In[106]:


Num = ["11","15","25","65","44","20","92","55","85","45"]
num_with_5 = [item for item in Num if "5" in item]
print(num_with_5)


# #### Example 2: Accepts items which have more than 4 letters

# In[126]:


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)


# In[124]:


num = [i for i in range(4444) if i%99==0]
num_with_6 = [item for item in num if (len(item) > 4)] 
print(num)


# In[ ]:





# In[ ]:




