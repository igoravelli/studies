import os
import subprocess
from PyPDF2 import PdfFileReader

def main():
    #os.system('copy_files.sh')
    #subprocess.call('copy_files.sh')
    os.popen('bash copy_files.sh')

if __name__ == '__main__':
    main()