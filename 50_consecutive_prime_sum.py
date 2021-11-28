from EulerTools import primes, is_prime



def search(n=100):
    if n == 10**6:
        some_primes = primes()
    else:
        some_primes = [x for x in range(2, n) if is_prime(x)]

    # print(some_primes)
    
    max_count = 0
    max_prime = 0
    
    i = 0

    while some_primes[i] < 13:
        
        # print(some_primes[i])
        # print(i)
        sum_prime = 0
        count = 0
        j = i
        while sum_prime < n:
            count += 1
            # print(count)
            sum_prime += some_primes[j]
            # print(some_primes[i], sum_prime)
            # print(i, sum_prime)
            if sum_prime in some_primes:
                if count > max_count:
                    max_count = count
                    max_prime = sum_prime
                    # print(max_prime, i)
            j += 1
        i += 1
        # print()
    print(max_prime, max_count)


    
search(10**3) # == 997651








