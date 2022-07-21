from math import pow
from math import sqrt as square_root
import random as probability

result_1 = pow(2, 4) 
print ("result_1 is", result_1)

result_2 = square_root(16)
print ("result_2 is", result_2)

result_3 = probability.randint(0,100)
print ("result_3 is", result_3)

names = ["John", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print ("Original names: ", names)

probability.shuffle(names) 
print ("Names after shuffling: ", names)

result_4 = probability.choice(names)
print("Chosen name is: ", result_4)
