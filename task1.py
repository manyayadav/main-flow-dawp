Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
  
#Creating a list
my_list = [10,20,30,40,50]
print("List:",my_list)
List: [10, 20, 30, 40, 50]
#Adding elements to the list
my_list.append(60)
print("List after adding new element:",my_list)
List after adding new element: [10, 20, 30, 40, 50, 60]
my_list.remove(30)
print("List after removing an element:",my_list)
List after removing an element: [10, 20, 40, 50, 60]
#Modifying an element in the list
my_list[0]=15
print("List after modifying an element:",my_list)
List after modifying an element: [15, 20, 40, 50, 60]
#Additionally , we can also use pop operation to remove an element at a particular index
my_list.pop(1)
20
print("List after popping the element at index 1:", my_list)
List after popping the element at index 1: [15, 40, 50, 60]

# Creating a dictionary
my_dict = {'Name': 'Manya' , 'Branch' : 'CSE'}
print("Dictionary:", my_dict)
Dictionary: {'Name': 'Manya', 'Branch': 'CSE'}
#Adding elements to the dictionary
my_dict['Domain'] = 'Data Analytics'
print("Dictionary after adding key 'Domain' with value 'Data Analytics':", my_dict)
Dictionary after adding key 'Domain' with value 'Data Analytics': {'Name': 'Manya', 'Branch': 'CSE', 'Domain': 'Data Analytics'}
#Removing elements from the dictionary
del my_dict['Branch']
print("Dictionary after removing key 'Branch' :", my_dict)
Dictionary after removing key 'Branch' : {'Name': 'Manya', 'Domain': 'Data Analytics'}
# Modifying an element in the dictionary
my_dict['Domain'] = 'Data Science'
print("Dictionary after modifying the value of key 'Domain' to 'Data Science:", my_dict)
Dictionary after modifying the value of key 'Domain' to 'Data Science: {'Name': 'Manya', 'Domain': 'Data Science'}

#Creating a set
my_set = {1,2,3,4,5}
print("Set:", my_set)
Set: {1, 2, 3, 4, 5}
#Adding elements to the set
my_set.add(7)
print("Set after adding new element: ", my_set)
Set after adding new element:  {1, 2, 3, 4, 5, 7}
#Removing an element from the set
my_set.remove(7)
print("Set after removing an element: ", my_set)
Set after removing an element:  {1, 2, 3, 4, 5}
#Modifying elements in a set
my_set.discard(3)
my_set.add(8)
print("Set after modification: ", my_set)
Set after modification:  {1, 2, 4, 5, 8}
