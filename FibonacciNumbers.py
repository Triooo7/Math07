# Defining the fibonacci series.
fibonacci_numbers = [1,2]
# Loop for less than 4 million.
while fibonacci_numbers[-1] < 4000000:
    fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

del fibonacci_numbers[-1]
print(fibonacci_numbers)
# Getting the even logic.
evenFibNum = []
for fib_numbers in fibonacci_numbers:
    if fib_numbers % 2 == 0:
        evenFibNum.append(fib_numbers)
print(evenFibNum)
# finding the sum.
total_Sum = 0
for even_num in evenFibNum:
    total_Sum += even_num

print(total_Sum)




