import random

def cow_bull():
    counter = 0       #counter is 0
    n = str(random.randint(1000,9999))   #generate 4 digit number
                              #duplicate random number
    print ('Welcome to the Cows and Bulls Game!')
    print ('A cow is a digit in the correct place')
    print ('A bull is a digit in the wrong place')
    print (n)
    while True:
      
        s = n    
        g = str(input('Enter a four digit number: '))   #ask for a number
        cow = 0
        bull = 0     #set cow and bull to 0
        counter += 1                  #up counter by one each guess
       
        for x in range(4):
          if n[x] == g[x]:
            cow += 1
            g = g.replace(g[x], ",")
       
        if cow == 4:                 #checking for winning number
            print ('You guessed it! The number was %s' %n)
            print ('It took you %d tries.' %counter)
            break
        for digit in n:          #checking for bulls
            if digit in g:
                bull += 1
                s = s.replace(digit, ".") 
                g = g.replace(digit, ",")          #replace digit in duplicate random number with "." so not double counted
        print ("Cows: %d. Bulls: %d" %(cow, bull))
        
    
    

cow_bull()
