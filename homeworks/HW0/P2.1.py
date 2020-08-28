def numbers(type,N):
    #ASSERITING TO MAKE SURE THAT N IS ALWAY GRATER THAN 0 BEFORE RUNNING FUNCTION
    assert N>0, 'N has to be greater than 0'
    #COMPUTING PI BASED ON INFINITE SUM
    if type == 'pi':
        pi=0
        #COMPUTING THE SUM OF RHS TERM
        for n in range(1,N+1):
            pi+=1/(n**2)
        #MOVING THINGS FROM LHS TERM TO GET PI BY ITSELF
        pi=pi*6
        pi=pi**(1/2)
        return pi
    
    #COMPUTING THE GOLDEN RATIO SECTION
    elif type == 'goldenratio':
        #INITIALIZING THE SEQUENCE FOR FIRST TWO CASES
        F=[1,1]
        #FOR CASE OF N=1
        if N==1:
            fib=F[0]
        #FOR CASE OF N=2
        elif N==2:
            fib=F[1]
        #FOR ANY CASE PF n>2
        else:
            #LOOP TO CREATE THE SEQUENCE
            for n in range(2,N):
                F.append(F[-1]+F[-2])
            #COMPUTING THE RATIO BASED ON THE LAST TWO ENTRIES OF THE SEQUENCE
            fib=F[-1]/F[-2]
        return fib
    #DEALING WITH CASE OF PASSING A STRING THAT IS UNACCOUNTED FOR    
    else:
        print("Type not programmed in! Please check the series in question.")


#RUNNING THE FUNCTION ABOVE FOR PI
print('Pi series with n=7 is {}'.format(numbers('pi',7)))
print('Pi series with n=100000 is {}'.format(numbers('pi',100000)))

#RUNNING THE FUNCTION ABOVE FOR THE GOLDEN RATIO
print('Golden Ratio with n=7 is {}'.format(numbers('goldenratio',7)))
print('Golden Ratio with n=100000 is {}'.format(numbers('goldenratio',100000)))
