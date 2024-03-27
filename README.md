# Warings
Waring's solutions to \$n = x^2 + y^2 + z^3 + w^3$

## Why
It is a well know result proven by <a href="https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem">Lagrange</a> in 1770 that \$n = x^2 + y^2 + z^2 + w^2$ always has integer solutions for all positive n.
It is also true that \$n = x^2 + y^2 + z^2 + w^3$ also always has integer solutions.
But what about \$n = x^2 + y^2 + z^3 + w^3$ ?
My conjecture is that the only value of n where this cannot be true is for n=23.
To my knowledge this has never been proven.
The attached Python program attempts to give a lower limit on n up to which this conjecture is true.

## How to run
1. Download the file SumOf2SquaresAnd2Cubesv3.py into a windows file.
2. Create a parameter file in notepad with two rows:-
   2.1. First square root of n to be calculated
   2.2. Last square root of n to be calculated
3. In command prompt
   py SumOf2SquaresAnd2Cubesv3.py parameterfile.txt 
