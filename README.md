# Warings
Waring's solutions to \$n = x^2 + y^2 + z^3 + w^3$

## Why
It is a well know result proven by <a href="https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem">Lagrange</a> in 1770 that \$n = x^2 + y^2 + z^2 + w^2$ always has integer solutions for all positive n.
It is also true that \$n = x^2 + y^2 + z^2 + w^3$ also always has integer solutions.
But what about \$n = x^2 + y^2 + z^3 + w^3$ ?
If the cubes are positive then there is a conjecture that they can be any natural number except 23. So far this program has checked this conjecture up to n equals 36 billion and not found any counter examples.

Professor Trevor Wooley of Bristol university replied to my email on the subject on 11th April 2011:-

>“Your conjecture seems quite plausible, although we do not know how to prove it at this point! It is known that all large enough integers are the sum of two squares and three cubes of natural numbers ( see Hooley, Christopher on Waring’s problem for two squares and three cubes. J. Reine Angew. Math. 328 (1981), 161–207. ) for more on this.

>“One can also prove, subject to the proof of the Generalised Riemann hypothesis, that all large enough integers are the sum of two squares, two cubes and 2 sixth powers of natural numbers.( that’s an unpublished result of mine with Elena Golubeva). But two squares and two cubes is just too far beyond our current methods. The best approach we have is to replace the two cubes by something of the shape \$(h+z)^3+(h−z)^3$  , which has a \$6hz^2$ term, so that the problem becomes ternary quadratic form problem with a large coefficient. But we know too little about the associated cusp form coefficients to prove anything from here.

>“So ….your conjecture is likely true, but a proof will need ideas beyond what are currently available.”

The attached Python program attempts to give a lower limit on n up to which this conjecture is true.

## How to run
1. Download the file SumOf2SquaresAnd2Cubesv2.py into a windows file.
2. Create a parameter file in notepad with two rows:-
   
   2.1. First square root of n to be calculated.
   
   2.2. Last square root of n to be calculated.
   
3. In command prompt
   py SumOf2SquaresAnd2Cubesv2.py parameterfile.txt

There is a jit compiler called [pypy](https://www.pypy.org/download.html)  which on my machine runs 7 times faster than standard windows Python.

## How does it work

The program splits into four main parts, the first three precalculate arrays which are used to optimise the fourth part. 
The fourth part loops through values of n and finds candidate values of x, y, z and w which rule n out as a sum of two squares and two positive cubes.

### 1. Calculate all positive integers which can not be written as \$y^2 + z^3 +w^3$
See [OEIS A022557](https://oeis.org/A022557)

### 2. Calculate for every positive integer up to 8,000,000 if sum of two cubes

### 3. Calculate all possible mod 63 values of the residual r for which \$r = z^3 + w^3$

### 4. Loop through values of n finding values of x,y,z,w such that \$n = x^2 + y^2 + z^3 + w^3$
This section has 4 nested loops:-
1. Loop through m. For a given n, m will be given by \$m=\left\lfloor\sqrt{n}\right\rfloor$
2. Loop through n from \$m^2$ to \$(m+1)^2-1$ but only using increments which can not be written as \$y^2 + z^3 +w^3$ 
3. Loop through x from \$x = m$ ( Highest ) downwards.
4. Loop though y ( Highest to lowest ). For each y calculate residual \$r = n - x^2 - y^2$ and check to see if residual is listed as sum of two cubes. Only use values of y for which \$n - x^2 - y^2 = z^3 + w^3$ is possible mod 63.


## Results
   
| Start Date(UTC)  | End Date(UTC) | Maximum n | Posted by | System | Software |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 2024-03-26 19:32  | 2024-03-29 10:00  | 1,226,540,484 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 |
| 2024-03-26 19:32  | 2024-03-30 20:58 | 1,688,059,396 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 |
| 2024-03-31 20:35  | 2024-04-02 16:52 | 83,970,709,729 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 |

