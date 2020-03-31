def mutipleof3and5():
    total = 0
    for num in range(1000):
        if(num % 3 == 0 or num % 5 == 0):
            total += num

    print(total)


if __name__ == '__main__':
    mutipleof3and5()