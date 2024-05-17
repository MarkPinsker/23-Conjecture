# 23 Conjecture
Conjecture: 23 is the only positive integer for which \$n = x^2 + y^2 + z^3 + w^3$ has no solution with non-negative x,y,z,w.

## Why
It is a well know result proven by <a href="https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem">Lagrange</a> in 1770 that \$n = x^2 + y^2 + z^2 + w^2$ always has integer solutions for all positive n.
It is also proven that \$n = x^2 + y^2 + z^2 + w^3$ also always has integer solutions.
But what about \$n = x^2 + y^2 + z^3 + w^3$ ?
If the cubes are positive then there is a conjecture that they can be any natural number except 23. So far this program has checked this conjecture up to n equals 95 trillion and not found any counter examples.

Professor Trevor Wooley of Bristol university replied to my email on the subject on 11th April 2011:-

>“Your conjecture seems quite plausible, although we do not know how to prove it at this point! It is known that all large enough integers are the sum of two squares and three cubes of natural numbers ( see Hooley, Christopher on Waring’s problem for two squares and three cubes. J. Reine Angew. Math. 328 (1981), 161–207. ) for more on this.

>“One can also prove, subject to the proof of the Generalised Riemann hypothesis, that all large enough integers are the sum of two squares, two cubes and 2 sixth powers of natural numbers.( that’s an unpublished result of mine with Elena Golubeva). But two squares and two cubes is just too far beyond our current methods. The best approach we have is to replace the two cubes by something of the shape \$(h+z)^3+(h−z)^3$  , which has a \$6hz^2$ term, so that the problem becomes ternary quadratic form problem with a large coefficient. But we know too little about the associated cusp form coefficients to prove anything from here.

>“So ….your conjecture is likely true, but a proof will need ideas beyond what are currently available.”

The attached Python program attempts to give a lower limit on n up to which this conjecture is true.

## How to run
### 1. Download the files in [23-con](https://github.com/MarkPinsker/23-Conjecture) into a windows folder.

### 2. Edit Config-readfile.txt file in notepad. The first three parameters are mandatory:-
   
#### 2.1. First square root of n to be calculated. 
        Required: Yes
        Syntax:- "Initial square root of n:{n}"
   
#### 2.2. Last square root of n to be calculated. 
        Required: Yes
        Syntax:- "Final square root of n:{n}"

#### 2.3. Maximum value of z that is checked. 
        Required: Yes
        
        Syntax:- "Maximum value of z:{n}"
        
      Note that this uses memory in proportion to the cube of this value:- 
      30 is sufficient for n up to a million 
      200 up to 83 billion. 
      300 up to 3,209,056,635,456. 
      350 up to 9,761,900,355,216, 
      400 up to 23,336,783,225,856.
      450 up to 48,851,530,635,769

#### 2.4. Use of bitarray. If this parameter is set to true then the program will import bitarray which will reduce the memory usage of the program but will only work if bitarray has been downloaded. 
          Required: No
        
         Syntax: "Use bitarray:true"
           
In order to use this you need to make the bitarray module available to Python.
See the section [Download bitarray](Download%20bitarray.md)

#### 2.5. Log file name
          Required: No
        
         Syntax: Log file name:{filename}"

#### 2.6. A022557 filename
          Required: Either this or lookahead limit
        
         Syntax: "A022557 filename:{filename}"

#### 2.7. Lookahead limit
Note that this value is limited by the amount of memory available to the program.

      Required: Either this or A022557 filename
      Syntax: "Lookahead limit:{n}"
   
### 3. Run the program

Start up command prompt and if you using standard Python enter:-

   py 23Conjecture.py Config-readfile.txt

There is a jit compiler called [pypy](https://www.pypy.org/download.html)  which on my machine runs 7 times faster than standard windows Python.
If you have this installed run:-

   pypy 23Conjecture.py Config-readfile.txt

 
## How does it work

The program splits into three main parts: the first two precalculate arrays which are used to optimise the third part. 
The third part loops through values of n and finds candidate values of x, y, z and w which rule n out as a sum of two squares and two positive cubes.

### 1. Calculate all positive integers up to a specified limit which cannot be written as \$y^2 + z^3 +w^3$
See [OEIS A022557](https://oeis.org/A022557).
It is faster to read this sequence from a file than to calculate it from scratch every time you run the program. If you wish to read the sequence from a preprepared file specify the filename in the configuration file by specifying "A022557 filename".
If you don't specify a filename then the 23Conjecture.py program will use the value of "Lookahead limit" you specify and calculate the A022557 sequence up to that. 

The file A022557.txt is an example which lists the sequence up to 10,000,000, but Github has a filesize limit so I can't supply a bigger file.
If you can generate a bigger file it will speed up the search for counterexamples.
The program called [writeA022557.py](https://github.com/MarkPinsker/23-Conjecture/blob/main/writeA022557.py) allows you to append more elements in the sequence to the file.
For example if the A022557 file goes up to 50 billion then it will have 88,579,424 rows (less than 0.2%), so the counterexample search would be over 564 times faster than if this file wasn't used.

### 2. Calculate for every positive integer up to cube of maximum z parameter if sum of two cubes

### 3. Loop through values of n finding values of x,y,z,w such that \$n = x^2 + y^2 + z^3 + w^3$
This section has 4 nested loops:-
1. Loop through square root of n by "lookahead limit". The next n will be the highest square less than previous n plus lookahead.

      Example: if you start on 1 and the lookahead limit is 100, then  square root of n will be 1, 10 ( because \$10^2 < 1 + 100$ ), 14 ( because \$14^2 < 10^2 + 100$ ) , 17 ( because \$17^2 < 14^2 + 100$ ) , etc.
2. Loop through "possible" values of n using increments which can not be written as \$y^2 + z^3 +w^3$


      Example: if square root of n is 14 and the lookahead limit is 100, then values of n which might generate a counterexample are \$14^2 +7 , 14^2+14 , 14^2 + 15, 14^2 + 19,\ldots, 14^2 + 98$.
   
3. Loop through x from square root of n downwards.

      Example: if \$n=14^2+40=236$ then values which might generate a counterexample are \$x<=\sqrt{236}$ or \$x \in \\{ 15,14,13,\ldots, 0 \\} $.   
4. Loop though y ( Highest to lowest ). For each y calculate residual \$r = n - x^2 - y^2$ and check to see if residual is listed as sum of two cubes.

      Example: if n is 236 and x = 15 then values of y would be which might generate a counterexample are \$3,2,1,0$, and the corresponding values of r are  \$236-15^2-3^2=2$ , \$236-15^2-2^2=7$ , \$236-15^2-1^2=10$ , and \$236-15^2-0^2=11.$
   As the first residual r=2 is the sum of two cubes then 236 is not a counterexample so only y = 3 needs to be processed.    

## Results
   
| Start Date(UTC)  | End Date(UTC) | Maximum n | Posted by | System | Software | Program |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 2024-03-26 19:32  | 2024-03-29 10:00  |  1,226,540,484 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 | SumOf2SquaresAnd2Cubes.py |
| 2024-03-26 19:32  | 2024-03-30 20:58 |   1,688,059,396 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 | SumOf2SquaresAnd2Cubes.py |
| 2024-03-31 20:35  | 2024-04-02 20:45 |  92,549,808,400 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 | SumOf2SquaresAnd2Cubes.py |
| 2024-04-02 20:45  | 2024-04-03 16:16 | 135,586,000,000 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 | SumOf2SquaresAnd2Cubes.py |
| 2024-04-02 20:45  | 2024-04-10 21:28 | 799,795,741,969 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 | SumOf2SquaresAnd2Cubes.py |
| 2024-04-11 06:24  | 2024-04-16 18:19 | 7,307,722,758,400 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 | SumOf2SquaresAnd2Cubes.py |
| 2024-04-17 19:56  | 2024-05-06 20:05 | 48,851,530,635,769 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 | SumOf2SquaresAnd2Cubes.py |
| 2024-05-07 19:56  | 2024-05-17 06:40 | 95,343,526,888,801 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 | 23Conjecture.py |

