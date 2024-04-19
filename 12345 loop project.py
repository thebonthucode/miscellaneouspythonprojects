list = [1, 2, 3, 4, 5] #the list of the numbers
sum = sum(list)        #the sum of all the numbers in the list
x = 0                  #the variable set for the loop
while x < sum:         #while x is lower than the sum of the list:
  x = (x + 1)          #it will add 1 to the variable
while (x >= sum):      #once the variable is equal or greater than the sum of the list:
  x = (x - 1)          #this stablizes the loop from repeating to infinity
  print(x + 1)         #print the variable (add one, to make line 7 not one less.)
#line 7 can be taken away along with the +1 in line 8.
#however, the loop will be active until inifity, so I added the extension.

#list = [1, 2, 3, 4, 5] 
#sum = sum(list)     
#x = 0                  
#while x < sum:       
#  x = (x + 1)         
#while (x >= sum):      
#  print(x)         

#The code is the original code, but this goes on until inifity, so I modified it, but both work. 