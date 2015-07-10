from questionsOneToFive import isPrime

# Question 6
def question_six(number):
    sumOfSquares = 0
    squareOfTotalSum = 0
    sumOfRange = 0
    for x in range(1,number + 1):
        sumOfRange += x
        sumOfSquares += x*x
    squareOfTotalSum = sumOfRange * sumOfRange
    return squareOfTotalSum - sumOfSquares

def question_seven(nthPrime):
    count = 0
    start = 1
    final = 0
    while count < nthPrime:
        if isPrime(start):
            count+=1
            final = start
        if(start == 2 or start == 1):
            start+=1
        else: start+=2
    return final

# Question 8

testString = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866" + \
"70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"

def sequenceLargestPro(digNumber, seqLen):
    length = len(digNumber)
    largestProduct = 0
    for i in range(0, int(length/2) + seqLen):
        frontPrevProduct = int(digNumber[i])
        backPrevProduct = int(digNumber[seqLen - 1 - i])
        for j in range(i+1, i + seqLen):
            frontPrevProduct = frontPrevProduct * int(digNumber[j])
            backPrevProduct = backPrevProduct * int(digNumber[seqLen - 1 - j])
        if largestProduct < frontPrevProduct:
            largestProduct = frontPrevProduct
        if largestProduct < backPrevProduct:
            largestProduct = backPrevProduct
    return largestProduct

# Question 9


def question_nine(goal):
    for a in range(1,goal/3):
        for b in range(1,goal/2):
            for c in range(1,goal):
                if((a + b + c) == goal):
                    # print "a:{},b:{},c:{}".format(a,b,c)
                    if ((a**2 + b**2) == c**2):
                        return (a*b*c)

# Question 10

def sum_primes(number):
    total = 2
    # Skip 2 in order to just skip evens completely
    for x in range(3, number,2):
            if(isPrime(x)):
                total += x
    return total
