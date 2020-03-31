
fibonacci_numbers = [1,2]

while fibonacci_numbers[-1] <= 400000:
    fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

del fibonacci_numbers[-1]

evenFibNum = []
for fib_numbers in fibonacci_numbers:
    if fib_numbers % 2 == 0:
        totalSum = 0
        evenFibNum.append(fib_numbers)
print(evenFibNum)
for evennum in evenFibNum:
        totalSum += evennum

print(totalSum)




