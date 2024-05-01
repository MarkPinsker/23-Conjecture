import math,sys,os,re
from datetime import datetime
min = int(sys.argv[1])
max = int(sys.argv[2])
TwominminusMax = 2 * min - max

third=1./3.
i = 0
isquared = 0

sumOf2CubesandSquare = [0 for i in range(1 + max - min)] 
print('Situation 1')
while ( ( isquared < min ) and ( isquared < TwominminusMax ) ):
	Min_minus_isquared = min - isquared 
	Min_minus_isquared_over_2 = Min_minus_isquared / 2
	Max_minus_isquared = max - isquared 
	Max_minus_isquared_over_2 = Max_minus_isquared / 2

	j = math.floor( Min_minus_isquared_over_2 ** third)
	jCubed = j * j * j

#	print('i = ',i)
	while( jCubed < Max_minus_isquared_over_2 ):
#		print('      j=',j,', min-i^2=',Min_minus_isquared,', j^3=',jCubed )
		k = math.ceil(( Min_minus_isquared - jCubed ) ** third)
		kCubed = k * k * k
		while ( k <= j ):
			n = isquared + jCubed + kCubed - min 
			sumOf2CubesandSquare[n] = 1
			k = k + 1
			kCubed = k * k * k

		j = j + 1
		jCubed = j * j * j


	while( jCubed < Min_minus_isquared ):
#		print('      j=',j,', min-i^2=',Min_minus_isquared,', j^3=',jCubed )
		k = math.ceil(( Min_minus_isquared - jCubed ) ** third)
#		print('k = ',k)
		kCubed = k * k * k
		while ( kCubed <= Max_minus_isquared - jCubed ):
			n = isquared + jCubed + kCubed - min 
			sumOf2CubesandSquare[n] = 1
			k = k + 1
#			print('k = ',k)
			kCubed = k * k * k

		j = j + 1
		jCubed = j * j * j

	while( jCubed < Max_minus_isquared ):
#		print('      j=',j,', min-i^2=',Min_minus_isquared,', j^3=',jCubed )
		k = 0
		kCubed = 0
		while ( kCubed <= Max_minus_isquared - jCubed ):
			n = isquared + jCubed + kCubed - min 
			sumOf2CubesandSquare[n] = 1
			k = k + 1
			kCubed = k * k * k

		j = j + 1
		jCubed = j * j * j


	i = i + 1
	isquared = i * i

print('Situation 2')
while ( isquared < min ):
	Min_minus_isquared = min - isquared 
	Min_minus_isquared_over_2 = Min_minus_isquared / 2
	Max_minus_isquared = max - isquared 
	Max_minus_isquared_over_2 = Max_minus_isquared / 2

	j = math.floor( Min_minus_isquared_over_2 ** third)
	jCubed = j * j * j

#	print('i = ',i)

	while( jCubed < Min_minus_isquared ):
#		print('      j=',j,', min-i^2=',Min_minus_isquared,', j^3=',jCubed )
		k = math.ceil(( Min_minus_isquared - jCubed ) ** third)
		kCubed = k * k * k
		while ( k <= j ):
			n = isquared + jCubed + kCubed - min 
			sumOf2CubesandSquare[n] = 1
			k = k + 1
			kCubed = k * k * k

		j = j + 1
		jCubed = j * j * j


	while( jCubed < Max_minus_isquared_over_2 ):
#		print('      j=',j,', min-i^2=',Min_minus_isquared,', j^3=',jCubed )
		k = 0
		kCubed = 0
		while ( k <= j ):
			n = isquared + jCubed + kCubed - min 
			sumOf2CubesandSquare[n] = 1
			k = k + 1
			kCubed = k * k * k

		j = j + 1
		jCubed = j * j * j


	while( jCubed < Max_minus_isquared ):
#		print('      j=',j,', min-i^2=',Min_minus_isquared,', j^3=',jCubed )
		k = 0
		kCubed = 0
		while ( kCubed <= Max_minus_isquared - jCubed ):
			n = isquared + jCubed + kCubed - min 
			sumOf2CubesandSquare[n] = 1
			k = k + 1
			kCubed = k * k * k

		j = j + 1
		jCubed = j * j * j
	i = i + 1
	isquared = i * i

print('Situation 3')
while( isquared < max ):
	Max_minus_isquared = max - isquared 
	Max_minus_isquared_over_2 = Max_minus_isquared / 2

	j = 0
	jCubed = 0

#	print('i = ',i)

	while( jCubed < Max_minus_isquared_over_2 ):
#		print('      j=',j,', min-i^2=',Min_minus_isquared,', j^3=',jCubed )
		k = 0
		kCubed = 0
		while ( k <= j ):
			n = isquared + jCubed + kCubed - min 
			sumOf2CubesandSquare[n] = 1
			k = k + 1
			kCubed = k * k * k

		j = j + 1
		jCubed = j * j * j
	

	while( jCubed < Max_minus_isquared ):
#		print('      j=',j,', min-i^2=',Min_minus_isquared,', j^3=',jCubed )
		k = 0
		kCubed = 0
		while ( kCubed <= Max_minus_isquared - jCubed ):
			n = isquared + jCubed + kCubed - min 
			sumOf2CubesandSquare[n] = 1
			k = k + 1
			kCubed = k * k * k

		j = j + 1
		jCubed = j * j * j
	i = i + 1
	isquared = i * i

print('Array created, now to list through it.')

NotSumOf1Squaresand2Cubes = []
for i in range(max - min):
    if ( sumOf2CubesandSquare[i] == 0):
        NotSumOf1Squaresand2Cubes.append(i + min)
        #print(i + min)

A022557Filename = 'A022557.txt'
with open(A022557Filename, 'a', encoding='utf-8') as A022557File: 
	A022557File.write("\n".join([str(n) for n in NotSumOf1Squaresand2Cubes]) + "\n")