def is_fibonacci(num: int):
    # return True if num is in fibonacci, otherwise return False

    n1, n2 = 0, 1
    count = 0
    fibo_list = []

    if (num < 0):
        print('Your number is negative!')

    else:
        while (count < num + 3):
            fibo_list.append(n1)
            n = n1 + n2
            n1 = n2
            n2 = n
            count += 1

    if num in fibo_list:
        print(num, 'is fibonacci')
        return True
    else:
        print(num, 'is not fibonacci')
        return False


is_fibonacci(6)