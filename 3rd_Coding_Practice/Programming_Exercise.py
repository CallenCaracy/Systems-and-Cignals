import numpy as np
import matplotlib.pyplot as plt

# fisrt array is the impulse reponse 
# flip then multople element by element
#

impulseArr = [0, 0, 5, 0.5, 0]
otherArr = [0, 0, 0.5, 0.5, 0]
# otherArr = impulseArr[:]
impulseArr.reverse()

product = []
sum = 0
for i in range(len(impulseArr)):
    product.append(impulseArr[i]*otherArr[i])
    sum += product[i]    

print("Element-wise product:", product)
print("Sum:", sum)



# testing 
result = np.convolve([0, 0, 1, 0.5, 0], [0,0,1,0.5,0])
print(result)