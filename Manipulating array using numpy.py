import numpy as np

a=np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]])
print(a)

# give dimmention of array

print("\n#Dimmention of the array is:" ,a.ndim)

# the structure f array
print("\n#The structure of the array is:", a.shape)

# to pick out certain elements from the array
print("\n#the element of the 2nd row 7th coulumn is:", a[1,7])

# to print a section
print("\n#I want to print the 7th coulumn ", a[:,7])

# to print a section of the array2(TAKE NOTE OF THE CODE HERE);
print("\nI want to print the even numbers of array:", a[0, 1:11:2], a[1, 1:11:2])

# to change an element

a[0,6]=333
a[1,0]=444
print("\n I have just changed the 7th element of the 1st array and the 1st element of the 2nd array of a.the new array looks like this", "\n", a)