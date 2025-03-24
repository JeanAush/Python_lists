my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#print(my_list)  # Output: [ 10, 20, 30, 40]

my_list.insert(1,15)

#print(my_list)  #Output: [10,15,20,30,40]
list_two = [50,60,70]

my_list.extend(list_two)

#print(my_list) #Output: [10,15,20,30,40,50,60,70]

del my_list[7]

#print(my_list)

my_list.sort()

#print(my_list)

old_value = 30
new_value = 35

if old_value in my_list:  
    index = my_list.index(old_value)  
    my_list[index] = new_value 

print(my_list)  