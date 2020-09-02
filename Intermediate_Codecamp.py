#Strings : join
#format method. f-string 
from timeit  import default_timer as  timer
my_list = ['a'] *60000

#bad
start = timer()
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)     

#good
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)     

#format methods
#Old method
var = "Ioannis"
my_string = "the variable is %s" % var
print(my_string)

#If var is a number
var = 3.01  
my_string = "the variable is %.3f" % var
print(my_string)

#more new method
var = 3.01565  
my_string = "the variable is {:.2f}".format(var + 1)
print(my_string)

#Newest method
var = 3.01565  
my_string = f"the variable is {var:.4}"
print(my_string)

