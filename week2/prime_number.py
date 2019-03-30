def prime(*args): #accepting list as arguments
    for n in args:
        c=0 #we keep reinitializing for each data in the list
        for j in range(1, n+1): #we run loop from 1 to n times. we are doing +1 because we want the number itself also
            if n%j==0:
                c+=1
        if c==2: #if the number is divisible exactly only two times it becomes prime number
            print(n)
    
prime(3, 4, 7, 19, 24, 6, 31)
