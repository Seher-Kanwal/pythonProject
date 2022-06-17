d_dict = {'name': "ali", 'class': "Ninth", 'sections': "A+"}
print(d_dict.get('sections'))
print(d_dict['sections'])
"""If you do not know whether the key exists already, the best approach is to use the get(key,default)
method. This method takes two arguments, the key that you’re looking for and a default value if that key 
is not found"""
print(d_dict.get('birthday', 'not found'))

# in order to add new values
d_dict['birthday'] = "10-feb"
# in order to update the values
d_dict.update({'class': "BsCs"})
print(d_dict.items())
"""We can access the dictionary’s contents as a whole using the keys(), values(), and items()
methods, which return the keys, the values, and the key-value pairs respectively"""
d_dict.values()
# del item from dictionary
del d_dict['class']
print(d_dict)
"""# in order to make copy use copy instead of assign values to another variables, in case of simple 
case if we change values in one it will automatically get changed in other dict t"""
c_dict = d_dict.copy()
print(c_dict)
