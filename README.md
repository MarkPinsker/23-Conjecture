# Warings
Conjecture: 23 is the only positive integer for which \$n = x^2 + y^2 + z^3 + w^3$ has no solution with non-negative x,y,z,w.

## Why
It is a well know result proven by <a href="https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem">Lagrange</a> in 1770 that \$n = x^2 + y^2 + z^2 + w^2$ always has integer solutions for all positive n.
It is also proven that \$n = x^2 + y^2 + z^2 + w^3$ also always has integer solutions.
But what about \$n = x^2 + y^2 + z^3 + w^3$ ?
If the cubes are positive then there is a conjecture that they can be any natural number except 23. So far this program has checked this conjecture up to n equals 9.3 trillion and not found any counter examples.

Professor Trevor Wooley of Bristol university replied to my email on the subject on 11th April 2011:-

>“Your conjecture seems quite plausible, although we do not know how to prove it at this point! It is known that all large enough integers are the sum of two squares and three cubes of natural numbers ( see Hooley, Christopher on Waring’s problem for two squares and three cubes. J. Reine Angew. Math. 328 (1981), 161–207. ) for more on this.

>“One can also prove, subject to the proof of the Generalised Riemann hypothesis, that all large enough integers are the sum of two squares, two cubes and 2 sixth powers of natural numbers.( that’s an unpublished result of mine with Elena Golubeva). But two squares and two cubes is just too far beyond our current methods. The best approach we have is to replace the two cubes by something of the shape \$(h+z)^3+(h−z)^3$  , which has a \$6hz^2$ term, so that the problem becomes ternary quadratic form problem with a large coefficient. But we know too little about the associated cusp form coefficients to prove anything from here.

>“So ….your conjecture is likely true, but a proof will need ideas beyond what are currently available.”

The attached Python program attempts to give a lower limit on n up to which this conjecture is true.

## How to run
### 1. Download the file SumOf2SquaresAnd2Cubes.py and params.txt into a windows file.

### 2. Edit the parameter file in notepad. The following three rows must be present:-
   
#### 2.1. First square root of n to be calculated. 
        Required: Yes
        Syntax:- "Initial square root of n:{n}"
   
#### 2.2. Last square root of n to be calculated. Note that this initially uses memory in proportion to twice its value. 
        Required: Yes
        Syntax:- "Final square root of n:{n}"

#### 2.3. Maximum value of z that is checked. 
        Required: Yes
        
        Syntax:- "Maximum value of z:{n}"
        
      Note that this uses memory in proportion to the cube of this value. 30 is sufficient for n up to a million and 200 is sufficient for n up to 83 billion. 300 is sufficient for up to 3,209,056,635,456.

#### 2.4. Use of bitarray. If this parameter is set to true then the program will import bitarray which will reduce the memory usage of the program but will only work if bitarray has been downloaded. 
          Required: No
           
           Syntax: "Use bitarray:true"
   
### 3. In command prompt

   py SumOf2SquaresAnd2Cubes.py params.txt

There is a jit compiler called [pypy](https://www.pypy.org/download.html)  which on my machine runs 7 times faster than standard windows Python.

## How to download bitarray

Because this program uses a large array of ones and zeroes it is more memory efficient but slower to use a bit array.

###  Install bitarray for py ( Python install package)

   If you are using py   
      C:\Users\Mark>py -m ensurepip --upgrade
      Looking in links: c:\Users\Mark\AppData\Local\Temp\tmp8yul8agr
      Requirement already satisfied: pip in c:\users\mark\appdata\local\programs\python\python312\lib\site-packages (24.0)
      
      C:\Users\Mark>python -m pip install bitarray
      Collecting bitarray
        Downloading bitarray-2.9.2-cp312-cp312-win_amd64.whl.metadata (35 kB)
      Downloading bitarray-2.9.2-cp312-cp312-win_amd64.whl (126 kB)
         ---------------------------------------- 126.2/126.2 kB 1.9 MB/s eta 0:00:00
      Installing collected packages: bitarray
      Successfully installed bitarray-2.9.2

###    Install bitarray for pypy ( Python install package)
   
        Looking in links: c:\Users\Mark\AppData\Local\Temp\tmpf2g0sxwt
      Processing c:\users\mark\appdata\local\temp\tmpf2g0sxwt\setuptools-65.5.0-py3-none-any.whl
      Processing c:\users\mark\appdata\local\temp\tmpf2g0sxwt\pip-23.0.1-py3-none-any.whl
      Installing collected packages: setuptools, pip
        WARNING: The scripts pip3.10.exe and pip3.exe are installed in 'C:\Users\Mark\Downloads\pypy3.10-v7.3.15-win64\pypy3.10-v7.3.15-win64\Scripts' which is not on PATH.
        Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
      Successfully installed pip-23.0.1 setuptools-65.5.0
      
      C:\Users\Mark\Downloads\pypy3.10-v7.3.15-win64\pypy3.10-v7.3.15-win64>pypy -m pip install bitarray
      Collecting bitarray
        Downloading bitarray-2.9.2-pp310-pypy310_pp73-win_amd64.whl (126 kB)
           ---------------------------------------- 126.5/126.5 kB 7.3 MB/s eta 0:00:00
      Installing collected packages: bitarray
      Successfully installed bitarray-2.9.2
      
      [notice] A new release of pip is available: 23.0.1 -> 24.0
      [notice] To update, run: pypy.exe -m pip install --upgrade pip
      
      C:\Users\Mark\Downloads\pypy3.10-v7.3.15-win64\pypy3.10-v7.3.15-win64>pypy.exe -m pip install --upgrade pip
      Requirement already satisfied: pip in c:\users\mark\downloads\pypy3.10-v7.3.15-win64\pypy3.10-v7.3.15-win64\lib\site-packages (23.0.1)
      Collecting pip
        Downloading pip-24.0-py3-none-any.whl (2.1 MB)
           ---------------------------------------- 2.1/2.1 MB 10.3 MB/s eta 0:00:00
      Installing collected packages: pip
        Attempting uninstall: pip
          Found existing installation: pip 23.0.1
          Uninstalling pip-23.0.1:
            Successfully uninstalled pip-23.0.1
        WARNING: The scripts pip.exe, pip3.10.exe and pip3.exe are installed in 'C:\Users\Mark\Downloads\pypy3.10-v7.3.15-win64\pypy3.10-v7.3.15-win64\Scripts' which is not on PATH.
        Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

  
## How does it work

The program splits into three main parts: the first two precalculate arrays which are used to optimise the third part. 
The third part loops through values of n and finds candidate values of x, y, z and w which rule n out as a sum of two squares and two positive cubes.

### 1. Calculate all positive integers up to specified limit which cannot be written as \$y^2 + z^3 +w^3$
See [OEIS A022557](https://oeis.org/A022557)

### 2. Calculate for every positive integer up to cube of maximum z parameter if sum of two cubes

### 3. Loop through values of n finding values of x,y,z,w such that \$n = x^2 + y^2 + z^3 + w^3$
This section has 4 nested loops:-
1. Loop through groups of square shells. The next square side is determined by adding twice the last square side to the previous one.
2. Loop through n from inner to outer square shell, but only using increments which can not be written as \$y^2 + z^3 +w^3$ 
3. Loop through x from square root of n downwards.
4. Loop though y ( Highest to lowest ). For each y calculate residual \$r = n - x^2 - y^2$ and check to see if residual is listed as sum of two cubes.


## Results
   
| Start Date(UTC)  | End Date(UTC) | Maximum n | Posted by | System | Software |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 2024-03-26 19:32  | 2024-03-29 10:00  |  1,226,540,484 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 v2 |
| 2024-03-26 19:32  | 2024-03-30 20:58 |   1,688,059,396 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 v2|
| 2024-03-31 20:35  | 2024-04-02 20:45 |  92,549,808,400 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 v2|
| 2024-04-02 20:45  | 2024-04-03 16:16 | 135,586,000,000 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 v2|
| 2024-04-02 20:45  | 2024-04-10 21:28 | 799,795,741,969 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 v2|
| 2024-04-11 06:24  | 2024-04-16 18:19 | 7,307,722,758,400 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 v1|
| 2024-04-17 19:56  | 2024-04-18 16:49 | 9,290,267,424,036 | Mark Pinsker | i7-6700 CPU@3.40GHz | Python pypy3.10-v7.3.15-win64 v2|

