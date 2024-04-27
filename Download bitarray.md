## How to download bitarray

Because this program uses a large array of ones and zeroes it is more memory efficient but slower to use a bit array.

In order to do this you need to install pip ( if it iosn't already installed ) which is the Python package installer and then install bitarray using pip:-

###  Install bitarray for py ( Python install package)


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
