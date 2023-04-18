
#Question-1

import math

n = int(input("N value: "))
x = int(input("X value: "))

factorial = lambda num: 1 if num == 0 else num * factorial(num - 1)

allNumbers = []

for i in range(1, x + 1):
    term = (n ** i) / factorial(i)
    allNumbers.append(term)

result = 1 + sum(allNumbers)
print("The result is:", result)


#Question2

def calculate_sum(n):

    global total_sum
    if n == 0:
        return
    else:
        current_sum = 0
        for k in range(1, n + 1):
            current_sum += ((-1) ** (k + 1)) / k
        total_sum += current_sum

        calculate_sum(n - 1)
total_sum = 0
calculate_sum(4)

print("Total Sum:",total_sum)