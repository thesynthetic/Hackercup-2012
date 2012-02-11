####################
# MaxPatternLength #
####################
def maxPatternLength(P1,N,M,A,B):
    Plast = ((A*P1+B) % M) + 1
    Pfirst = Plast
    patternLength = -1
    i = 2
    while i < N:
        Plast = ((A*Plast+B) % M) + 1

        if Pfirst == Plast:
            patternLength = i
            break
        if i == M:
            Pfirst = Plast
        i = i + 1
    print patternLength

#################
# Bargain Count #
#################
def bargain(N,P1,W1,M,K,A,B,C,D):
    bargainCount = 0
    i = 1
    while i <= N:
        j = 1
        bargain = 1
        if i == 1:
            PlastA = P1
            WlastA = W1
        else:
            PlastA = ((A*PlastA+B) % M) + 1
            WlastA = ((C*WlastA+D) % K) + 1
        
        while j <= N:
        
            if j == 1:
                PlastB = P1
                WlastB = W1
            else:
                PlastB = ((A*PlastB+B) % M) + 1
                WlastB = ((C*WlastB+D) % K) + 1
            	#test
                #print PlastA, PlastB, WlastA, WlastB
            if (PlastB < PlastA and WlastB <= WlastA) or (PlastB <= PlastA and WlastB < WlastA):
                #fail!
                if i != j:
                    bargain = 0
            else:
                pass
            j = j + 1
        if bargain == 1:
            bargainCount = bargainCount + 1
        i = i + 1
    return bargainCount


##################
# Terrible Count #
##################
def terrible(N,P1,W1,M,K,A,B,C,D):
    terribleCount = 0
    i = 1
    while i <= N:
        j = 1
        terrible = 1
        if i == 1:
            PlastA = P1
            WlastA = W1
        else:
            PlastA = ((A*PlastA+B) % M) + 1
            WlastA = ((C*WlastA+D) % K) + 1
            
        while j <= N:
            if j == 1:
                PlastB = P1
                WlastB = W1
            else:
                PlastB = ((A*PlastB+B) % M) + 1
                WlastB = ((C*WlastB+D) % K) + 1
            if (PlastA < PlastB and WlastA <= WlastB) or (PlastA <= PlastB and WlastA < WlastB):
                if i != j:
                	terrible = 0
            j = j + 1
        if terrible == 1:
            terribleCount = terribleCount + 1
        i = i + 1
    return terribleCount

def algo(N,P1,W1,M,K,A,B,C,D):
	pass


f = open('input.txt', 'r')
numOfLines = int(f.readline())
#for i in range(0,numOfLines):
for i in range(0,numOfLines):
	line = f.readline()
	x = line.split(' ')
	x = map(int,x)
	print terrible(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]), bargain(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])