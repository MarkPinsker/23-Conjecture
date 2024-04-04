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
zMax = int(data[2])
zmaxCubed = zMax * zMax * zMax
progressfile.close()
z = 0 
third=1./3.
##############################################################################
#sum of two cubes and a square
##############################################################################
squareShell = 2 * xfloorend + 1
squareShellRoot = math.floor(math.sqrt(squareShell)) + 1
squareShellCubeRoot = math.floor(squareShell ** third) + 1
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
NotSumOf1Squaresand2Cubes.append(10000000000000000)

sumOf2cubes = [0 for i in range(zmaxCubed)]
for x in range(zMax):
	xcubed = x * x * x
	for y in range(zMax):
		n =  xcubed + y * y * y
		if ( n < zmaxCubed ):
			sumOf2cubes[n]=10000*x+y
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

for xfloor in range(xfloorstart,xfloorend):

	xfloor2 = nextfloor2
	nextfloor2 = xfloor * xfloor
	if ( xfloor > 1 ):
		print('xfloor2 = ', xfloor2)
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
		while x >= 0 and nMinusxsqm  >=0 and notFound:
			y = math.floor(math.sqrt(nMinusxsqm) )
			nMinusx2Minusy2 = nMinusxsqm - y * y
# Loop downwards through possible y values if there are any
			while ( ( y > 0 ) and ( nMinusx2Minusy2  >= 0 ) and notFound):
				if ( sumOf2cubes[nMinusx2Minusy2] > 0 ):
					notFound = False
#					print('n= ',n,',x=',x,',y= ',y,',z,w =',sumOf2cubes[nMinusx2Minusy2] )
				y = y - 1
				nMinusx2Minusy2 = nMinusxsqm - y * y
# Move to next smaller x
			x = x - 1
			nMinusxsqm = n - x * x
		if ( notFound ):
			print(n,' is not x^2 + y^2 + z^3 + w^3')
			f.write(str(n) + ' is not x^2 + y^2 + z^3 + w^3\n')
		increment = increment  + 1
		n = xfloor2 + NotSumOf1Squaresand2Cubes[increment]
f.close()
