# M8p2.py         10/21     nick

#starting with the first two numbers of the sequence.

a=1
b=1

print("First 20 Fibonacci Numbers: ")

#running the loop

for i in range(20):
    print(a, end=", ")


    a, b = b, a+b
