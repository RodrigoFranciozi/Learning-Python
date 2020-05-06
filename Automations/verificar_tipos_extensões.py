from pathlib import Path
import shutil
import os

path = Path("C:/Users/mtzcpd1796/Downloads")
# destino_pdf = "C:/Users/mtzcpd1796/Desktop/pdf"

for filename in path.glob('*'):
        print (filename.suffix)




