first_name = 'Zeynep'    
last_name = 'Celik'       
country = 'Turkey'         
city= 'Corum'            
age = 20                  

print(type(first_name))        
print(type(10))           
print(type(3.14))           
print(type(1 + 1j))       
print(type(True))           
print(type([1, 2,3,4]))     
print(type({'name':'Zeynep','age':21}))    # dict
print(type((1,2)))                                            
print(type(zip([1,2],[3,4])))  


fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]
print(orange_and_mango)
orange_mango_lemon = fruits[1:]
print(orange_mango_lemon)