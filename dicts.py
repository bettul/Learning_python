person = {
    'first_name':'Zeynep',
    'last_name':'Celik',
    'age':21,
    'country':'Turkiye',
    'is_marred':True,
    'skills':['Java', 'C', 'Codeigniter', 'MySql', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) 
print(person['country'])    
print(person['skills'])     
print(person['skills'][0])  
print(person['address']['street']) 
#print(person['city'])       # Error
#Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key
#  exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.
print(person.get('city'))   #its output is none
#adding item to dictionary

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
print('key2' in person) #false
print('last_name' in person) #true

#Removing Key and Value Pairs from a Dictionary
 
person.pop('last_name')
print(person)
person.popitem()
print(person)
del person['first_name']
print(person)

