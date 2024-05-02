import math,sys,os,re
from datetime import datetime
############################################################################
# program to find all positive integer solutions of n = x^2 + y^2 + z^3 + w^3
############################################################################
# Validate and read parameter file supplied by command line parameter
if len(sys.argv) != 2 :
	print('Error. A single parameter needs to be supplied which is the name of a parameter file.')
	sys.exit(1)
progressfilename = sys.argv[1]
try:
	with open(progressfilename, 'r', encoding='utf-8') as progressfile: 
		data = progressfile.readlines() 
except IOError:
	print('Error. Parameter file ',progressfilename,' could not be read.')
	sys.exit(2)
progressfile.close()

# Validate parameters

initialSqrtN = 0
finalSqrtN = 0
zMax = 0
usebitarray = 0
outputlogname = "SumOf2Squaresand2Cubes.log"
A022557Filename = ""
NotSquareplus2CubesFilename=""
LookAheadLimit = 0
for i in range(len(data)):
	parmRow = data[i]
	if re.search(r'Initial square root of n:(\d+)',parmRow):
		strFloorStart = re.search(r'Initial square root of n:(\d+)',parmRow)
		initialSqrtN = int(strFloorStart.group(1))
		parmRowNo = i
	if re.search(r'Final square root of n:(\d+)',parmRow):
		strfinalSqrtN = re.search(r'Final square root of n:(\d+)',parmRow)
		finalSqrtN = int(strfinalSqrtN.group(1))
	if re.search(r'Lookahead limit:(\d+)',parmRow):
		strLookAhead = re.search(r'Lookahead limit:(\d+)',parmRow)
		LookAheadLimit = int(strLookAhead.group(1))
	if re.search(r'Maximum value of z:(\d+)',parmRow):
		strzMax = re.search(r'Maximum value of z:(\d+)',parmRow)
		zMax = int(strzMax.group(1))
	if re.search(r'Use bitarray:true',parmRow):
		usebitarray = 1
	if re.search(r'Log file name:(\S+)',parmRow):
		parsed = re.search(r'Log file name:(\S+)',parmRow)
		outputlogname = parsed.group(1)
	if re.search(r'A022557 filename:(\S+)',parmRow):
		parsed = re.search(r'A022557 filename:(\S+)',parmRow)
		A022557Filename = parsed.group(1)



if ( initialSqrtN == 0 ) :
	print('Error. There should be a row in the parameter file matching Initial square root of n:nnnn but not found')
	sys.exit(4)
if ( finalSqrtN == 0 ) :
	print('Error. There should be a row in the parameter file matching Final square root of n:nnnn but not found')
	sys.exit(5)
if ( zMax == 0 ) :
	print('Error. There should be a row in the parameter file matching Maximum value of z:nnnn but not found')
	sys.exit(6)


zmaxCubed = zMax * zMax * zMax

z = 0 
third=1./3.
print('Program to test the conjecture that 23 is the only positive integer that is not the sum of two squares and two non-negative cubes')
print('---------------------------------------------------------------------------------------------------------------------------------')
print('Logs will be printed to ', outputlogname)
##############################################################################
#sum of two cubes and a square
##############################################################################

print('Calculating list of natural numbers up to ',LookAheadLimit,' which are not the sum of a square and two cubes...')
squareShellRoot = math.floor(math.sqrt(LookAheadLimit)) + 1
squareShellCubeRoot = math.floor(LookAheadLimit ** third) + 1



if ( A022557Filename != '' ):
##############################################################################
	print('Reading ',A022557Filename , ' file of numbers which are not sum of square and two positive cubes')
##############################################################################
	NotSumOf1Squaresand2Cubes = []
	try:
		with open(A022557Filename, 'r', encoding='utf-8') as A022557File:
			for line in A022557File:
				NotSumOf1Squaresand2Cubes.append(int(line))
	except IOError:
		print('Error. Input file ',A022557Filename,' could not be read.')
		sys.exit(8)
	LookAheadLimit = int(line)
	if ( LookAheadLimit < 2 * finalSqrtN + 1 ):
		print('Error. Lookahead limit is ', LookAheadLimit ,' but needs to be over twice the square root of the largest n - ', 2 * finalSqrtN ,'. Increse lookahead limit or reduce final square root.')
		sys.exit(7)	
else:
##############################################################################
	print('Generating list of numbers which are not sum of square and two positive cubes')
##############################################################################
	if ( usebitarray == 1 ): 
##############################################################################
		print('Importing bitarray software')
		print('If this fails use pip to import bitarray.')
##############################################################################
		from bitarray import bitarray
		sumOf2CubesandSquare = bitarray(LookAheadLimit)
		sumOf2CubesandSquare.setall(0)
	else:
##############################################################################
		print('Not importing bitarray software as per parameter file')
##############################################################################
	sumOf2CubesandSquare = [0 for i in range(LookAheadLimit)] 

	if ( LookAheadLimit < 2 * finalSqrtN + 1 ):
		print('Error. Lookahead limit is ', LookAheadLimit ,' but needs to be over twice the square root of the largest n - ', 2 * finalSqrtN ,'. Increse lookahead limit or reduce final square root.')
		sys.exit(9)	

	for i in range(LookAheadLimit):
		print(i,' out of ',LookAheadLimit,end='\r' )
		i2 = i ** 2
		remainder = LookAheadLimit - i2
		squareShellCubeRoot = math.floor(remainder ** third) + 1
		for j in range(squareShellCubeRoot):
			j2 = i2 + j ** 3
			n = j2
			k = 0
			while ( k <= j + 1) and ( n < LookAheadLimit ):
				sumOf2CubesandSquare[n] = 1
				k = k + 1
				n = j2 + k ** 3
	print('Array created, now to list through it.')
	NotSumOf1Squaresand2Cubes = []
	for i in range(LookAheadLimit):
		if ( sumOf2CubesandSquare[i] == 0):
			NotSumOf1Squaresand2Cubes.append(i)
	NotSumOf1Squaresand2Cubes.append(10000000000000000)

	del sumOf2CubesandSquare

	
listlen = len(NotSumOf1Squaresand2Cubes)
print(listlen, ' such natural numbers found')
##############################################################################
print('Calculating list indicating whether numbers are sum of two cubes up to ',zmaxCubed,'...')
##############################################################################
sumOf2cubes = [0 for i in range(zmaxCubed)]
for x in range(zMax):
	xcubed = x * x * x
	for y in range(zMax):
		n =  xcubed + y * y * y
		if ( n < zmaxCubed ):
			sumOf2cubes[n]=1
##############################################################################
# Calculate n = x^2 + y^2 + z^3 + w^3
##############################################################################
outputlog = open(outputlogname,"a")
current_date = datetime.now()
datestring=current_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
outputlog.write(sys.argv[0] + " Parameter 1 " + sys.argv[1] + " " + datestring + "\n")
print('Validating values of n for main conjecture between ',initialSqrtN * initialSqrtN,' and ',finalSqrtN * finalSqrtN)
sqrtN=initialSqrtN
while ( sqrtN < finalSqrtN ):

	sqrtN2 = sqrtN * sqrtN
	nextfloor = math.floor(math.sqrt(sqrtN2 + LookAheadLimit ) )
	nextfloor2 = nextfloor * nextfloor

	print('n = ', sqrtN2,end='\r')
	outputlog.write(str(sqrtN) + "\n")
	data[parmRowNo]='Initial square root of n:' + str(sqrtN)+"\n"
	with open(progressfilename, 'w', encoding='utf-8') as progressfile: 
		progressfile.writelines(data) 

	increment = 0	
	n = sqrtN2 + NotSumOf1Squaresand2Cubes[increment]

	while ( n < nextfloor2 ):
		notFound = True
		x = math.floor(math.sqrt(n ) ) 
		nMinusxsqm = n - x * x
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
			outputlog.write(str(n) + ' is not x^2 + y^2 + z^3 + w^3\n')
		increment = increment  + 1
		n = sqrtN2 + NotSumOf1Squaresand2Cubes[increment]
	
	sqrtN = nextfloor

outputlog.close()
print('All values of n computed.')