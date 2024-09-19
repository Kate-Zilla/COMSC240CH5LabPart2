def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return False
        
    return True


def print_primes(n):
    for num in range (2,n):
        if is_prime(num):
            print(num, end = '  ')

def get_primes(n):
    prime_lst = []
    for num in range (2,n):
        if is_prime(num):
            meh = str(num)
            prime_lst.append(meh)
    return prime_lst
