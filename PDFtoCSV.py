# Imported Modules
#!/usr/local/bin/python3
import os
from pathlib import Path
import tabula

## PATH TO APP DIR - Currently assigned to Desktop on MacOS System
# os.chdir(os.path.expanduser(r'~/Desktop/PDFtoCSV/'))

# Setting Directory and paths
directory = ('pdf')
directory_encoded = ('csv')
files = Path(directory).glob('*')
names = os.listdir(directory)
fss = []
idx = 0

# Script
for i in names:
    if '.pdf' in i:
        fs = i.replace('.pdf', '.csv')
        fss.append(fs)
for f in files:
    if f.suffix == '.pdf':
        with open(f, 'r') as file:
            df = tabula.read_pdf(f, pages='all')
            tabula.convert_into(f, f'{directory_encoded}/{fss[idx]}', output_format='csv', pages='all')
            idx += 1
            print(df)
    else:
        continue


