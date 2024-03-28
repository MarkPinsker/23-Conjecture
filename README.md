# Warings
Waring's solutions to \$n = x^2 + y^2 + z^3 + w^3$

## Why
It is a well know result proven by <a href="https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem">Lagrange</a> in 1770 that \$n = x^2 + y^2 + z^2 + w^2$ always has integer solutions for all positive n.
It is also true that \$n = x^2 + y^2 + z^2 + w^3$ also always has integer solutions.
But what about \$n = x^2 + y^2 + z^3 + w^3$ ?
If the cubes are positive then there is a conjecture that they can be any natural number except 23. I have checked this conjecture up to a trillion and not found any counter examples.

Professor Trevor Wooley of Bristol university replied to my email on the subject on 11th April 2011:-

“Your conjecture seems quite plausible, although we do not know how to prove it at this point! It is known that all large enough integers are the sum of two squares and three cubes of natural numbers ( see Hooley, Christopher on Waring’s problem for two squares and three cubes. J. Reine Angew. Math. 328 (1981), 161–207. ) for more on this.

“One can also prove, subject to the proof of the Generalised Riemann hypothesis, that all large enough integers are the sum of two squares, two cubes and 2 sixth powers of natural numbers.( that’s an unpublished result of mine with Elena Golubeva). But two squares and two cubes is just too far beyond our current methods. The best approach we have is to replace the two cubes by something of the shape \$(h+z)^3+(h−z)^3$  , which has a \$6hz^2$ term, so that the problem becomes ternary quadratic form problem with a large coefficient. But we know too little about the associated cusp form coefficients to prove anything from here.

“So ….your conjecture is likely true, but a proof will need ideas beyond what are currently available.”

The attached Python program attempts to give a lower limit on n up to which this conjecture is true.

## How to run
1. Download the file SumOf2SquaresAnd2Cubesv3.py into a windows file.
2. Create a parameter file in notepad with two rows:-
   
   2.1. First square root of n to be calculated.
   
   2.2. Last square root of n to be calculated.
   
3. In command prompt
   py SumOf2SquaresAnd2Cubesv3.py parameterfile.txt 
