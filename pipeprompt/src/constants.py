import os
import platform

CWD = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
CACHE_DIR = f"{CWD}/cache/"


PLATFORM = platform.system().lower()


OPTIONS = """
ls
cp
mv
rm
""".strip()




TEST_DATA = """
hello_world from cmd@#cmd: echo {row_data}#@ @#color: RED#@
C:\@#cmd: ls -la {row_data}#@ @#color: ORANGE#@
10.100.1.1@#cmd: echo {row_data}#@ @#color: YELLOW#@
10.100.1.2@#cmd: echo command {row_data}#@ @#color: GREEN#@
10.100.1.3@#cmd: echo command {row_data}#@ @#color: BLUE#@
10.100.1.4@#cmd: echo command {row_data}#@ @#color: INDIGO#@
10.100.1.5@#cmd: echo command {row_data}#@ @#color: VIOLET#@
"""