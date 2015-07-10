import numpy


def divisble_by_20(number):
    for x in range(1,21):
        if number % x != 0:
            return False
    return True


def evenDivByTwenty():
    solved = False
    x = 20
    while(not solved):
        if divisble_by_20(x):
            solved = True
            print x
        else:
            x = x+20



def evenFibSum(number):
    total = 0
    count = 0
    fibEvenSum = 2
    value1 = 1; #odd start
    value2 = 2; #even  start
    while(total < number):
        total = value1 + value2
        if (total % 2 == 0):
            fibEvenSum += total
        value1 = value2
        value2 = total
        count+=1
    print fibEvenSum


def largestPrimeFact(number):
    largestPossible = int((number**0.5) + 1)
    smallest = 1
    currLargest = 1
    for x in range(smallest, largestPossible):
        # Limit calling of is prime
        if number % x == 0:
            print "Is it a prime number : " + str(isPrime(5))
            if (isPrime(x) and x > currLargest):
                print currLargest
                currLargest = x
    if currLargest == 1:
        currLargest == number
    print currLargest


def isPrime(number):
    largestPossible = int((number**0.5) + 1)
    smallest = 1
    for x in range(smallest, largestPossible):
        if number % x == 0 and (x != 1):
            return False
    return True

def paliCheck(pali):
    endOfString = len(pali);
    for x in range(0,(endOfString/2)):
        if pali[x] != pali[endOfString - (1 + x)]:
            return False
    return True

def largestDigitPali(digits):
    if digits == 1:
        return 9
    maxString = ""
    subString = ""
    for x in range(0,digits):
        maxString += "9"
        if x > 0:
            subString += "9"
    maxNumber = int(maxString)
    minHighBase = int(subString)
    print str(maxNumber)
    maxStart = maxNumber - minHighBase
    print str(maxStart)
    currLargestPali = 0;
    # For loops do not check last spot
    for i in range(maxStart, maxNumber + 1):
        for j in range(maxStart, maxNumber + 1):
            curr = i * j
            print "Before Loop : " + str(curr)
            if(paliCheck(str(curr))):
                currLargestPali = curr
    print str(currLargestPali)
