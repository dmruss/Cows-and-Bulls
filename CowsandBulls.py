import random

def cow_bull():
    counter = 0       #counter is 0
    n = str(random.randint(1000,9999))   #generate 4 digit number
    s = n                               #duplicate random number
    print 'Welcome to the Cows and Bulls Game!'
    print 'A cow is a digit in the correct place'
    print 'A bull is a digit in the wrong place'

    while True:
        
        g = str(input('Enter a four digit number: '))   #ask for a number
        cow = 0
        bull = 0     #set cow and bull to 0
        counter += 1                  #up counter by one each guess
        if n[0] == g[0]:         #checking each individual place for cow
            cow += 1        #if correct add one to cow
            g = g.replace(g[0], ".")       #remove digit so isn't counted as bull
        if n[1] == g[1]:
            cow += 1
            g = g.replace(g[1], ".")
        if n[2] == g[2]:
            cow += 1
            g = g.replace(g[2], ".")
        if n[3] == g[3]:
            cow += 1
            g = g.replace(g[3], ".")
        if cow == 4:                 #checking for winning number
            print 'You guessed it! The number was %s' %n
            print 'It took you %d tries.' %counter
            break
        for digit in g:          #checking for bulls
            if digit in n:
                bull += 1
                s = s.replace(digit, ".")           #replace digit in duplicate random number with "." so not double counted
        print "Cows: %d. Bulls: %d" %(cow, bull)
        
    
    

cow_bull()
