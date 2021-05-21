def is_prime(n):
    assert n > 1
    if n == 2:
        print('T')
        return True
    elif n % 2 == 0:
        print('F')
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                print('F')
                return False
        print('T')
        return True

def main():

    is_prime(49)

main()