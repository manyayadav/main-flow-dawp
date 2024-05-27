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





