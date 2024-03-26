import math,sys
from datetime import datetime
############################################################################
# program to find all positive integer solutions of n = x^2 + y^2 + z^3 + w^3
############################################################################
# read two commanmd line parameters for start and end
progressfilename = sys.argv[1]
with open(progressfilename, 'r', encoding='utf-8') as progressfile: 
    data = progressfile.readlines() 
xfloorstart = int(data[0])
xfloorend = int(data[1])
progressfile.close()
z = 0 
##############################################################################
#sum of two cubes and a square
##############################################################################
squareShell = 2 * xfloorend -1 
squareShellRoot = math.floor(math.sqrt(squareShell))
squareShellCubeRoot = math.floor(squareShell ** ( 1/3))
sumOf2CubesandSquare = [0 for i in range(squareShell)] 

for i in range(squareShellRoot):
    i2 = i ** 2
    for j in range(squareShellCubeRoot):
        j2 = i2 + j ** 3
        for k in range(squareShellCubeRoot):
            n = j2 + k ** 3
            if ( n < squareShell ):  
                sumOf2CubesandSquare[n] = 1

NotSumOf1Squaresand2Cubes = []
NotSumOf1Squaresand2CubesNo = -1
for i in range(squareShell):
    if ( sumOf2CubesandSquare[i] == 0):
        NotSumOf1Squaresand2CubesNo = NotSumOf1Squaresand2CubesNo + 1
        NotSumOf1Squaresand2Cubes.append(i)
##############################################################################
# Calculate all sums of two cubes modulo 63 ( should be 25 of them )
##############################################################################
sumOfCubesMod63 = [[0 for i in range(64)] for j in range(64)]
zMod63Generator = [[[-1 for i in range(64)] for j in range(64)] for k in range(64)]

base63=63
for x in range(base63):
	x3 = (x ** 3) % base63

	for y in range(base63):

		y3 = ( x3 + ( y ** 3 ) ) % base63 
# this relation zRa is true if z cubed plus some number cubed can sum to a mod 63
# For example sumOfCubesMod63[2][7] =1 becasue 2^3 + 5^3 = 7 (mod 63)
		sumOfCubesMod63[y][y3]=1


for nMinusxsqmMod63 in range(base63):
	for y in range(base63):
		a = ( nMinusxsqmMod63 - (y * y) ) % 63
		n = 0
		zMod63Generator[nMinusxsqmMod63][y][0] = n
		for z in range(base63):
			if ( sumOfCubesMod63[z][a] == 1 ):
				n = n + 1
				zMod63Generator[nMinusxsqmMod63][y][0] = n
				zMod63Generator[nMinusxsqmMod63][y][n] = z
##############################################################################
# Calculate n = x^2 + y^2 + z^3 + w^3
##############################################################################
n=0
f = open("SumOf2Squaresand2Cubes.log","a")
current_date = datetime.now()
datestring=current_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
f.write(sys.argv[0] + " Parameter 1 " + sys.argv[1] + " " + datestring + "\n")
nextfloor2=xfloorstart*xfloorstart
xfloorstart=xfloorstart+1
third=1./3.
for xfloor in range(xfloorstart,xfloorend):

	xfloor2 = nextfloor2
	nextfloor2 = xfloor * xfloor
	if ( xfloor > 1 ):
		print(xfloor2)
		f.write(str(xfloor2) + "\n")
		data[0]=str(xfloor)+"\n"
		with open(progressfilename, 'w', encoding='utf-8') as progressfile: 
			progressfile.writelines(data) 
	increment = 0	
	n = xfloor2 + NotSumOf1Squaresand2Cubes[increment]
	#for n in range(xfloor2 , nextfloor2): 
	while ( n < nextfloor2 ):

		notFound = True
		x = xfloor - 1
		nMinusxsqm = n - xfloor2
# n = x ^ 2
		if ( nMinusxsqm == 0 ):
			notFound = False
			#print(n,' = ',x,'^2')
		nMinusxsqmMod63 = nMinusxsqm % base63
		while x >= 0 and nMinusxsqm  >=0 and notFound:
			y = math.floor(math.sqrt(nMinusxsqm) )
			ymod63 = y % base63
			noSumof2cubesin63 = zMod63Generator[nMinusxsqmMod63][ymod63][0]
			nMinusx2Minusy2 = nMinusxsqm - y * y
# Loop downwards through possible y values if there are any
			while ( ( y > 0 ) and ( nMinusx2Minusy2  >= 0 ) and notFound):
				if ( noSumof2cubesin63 == 0 ): 
					y = y - 1
					ymod63 = y % base63
					noSumof2cubesin63 = zMod63Generator[nMinusxsqmMod63][ymod63][0]
					nMinusx2Minusy2 = nMinusxsqm - y * y
				else:

					nMinusx2Minusy2Minusz3 = nMinusx2Minusy2
					zdiv63 = 0
					m = 0
					while ( notFound and ( nMinusx2Minusy2Minusz3 > 0 ) ):
						m = m + 1
						if ( m  > noSumof2cubesin63 ):
							m = 1
							zdiv63 = zdiv63 + base63
						z = zMod63Generator[nMinusxsqmMod63][ymod63][m] + zdiv63

# Maximum possible value of z
#					z = math.floor(nMinusx2Minusy2 ** third)
# n = x^2 + y^2 + z^3
						nMinusx2Minusy2Minusz3 = nMinusx2Minusy2 - z * z * z

						if ( nMinusx2Minusy2Minusz3 > 0 ):
							w = math.floor(nMinusx2Minusy2Minusz3 ** third)
							if ( w ** 3 == nMinusx2Minusy2Minusz3 ):
								#print(n,' = ',x,'^2 + ',y,'^2 + ',z,'^3 + ',w,'^3')
								notFound = False
						elif ( nMinusx2Minusy2Minusz3 == 0 ):
							notFound = False
							#print(n,' = ',x,'^2 + ',y,'^2 + ',z,'^3')
				y = y - 1
				ymod63 = y % base63
				noSumof2cubesin63 = zMod63Generator[nMinusxsqmMod63][ymod63][0]
				nMinusx2Minusy2 = nMinusxsqm - y * y
# Move to next smaller x
			x = x - 1
			nMinusxsqm = n - x * x
			nMinusxsqmMod63 = nMinusxsqm % base63
		if ( notFound ):
			print(n,' is not x^2 + y^2 + z^3 + w^3')
			f.write(str(n) + ' is not x^2 + y^2 + z^3 + w^3\n')
		increment = increment  + 1
		n = xfloor2 + NotSumOf1Squaresand2Cubes[increment]
f.close()
