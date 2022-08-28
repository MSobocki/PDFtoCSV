# PDFtoCSV
PDFtoCSV using tabula module

######## Usage #########

1. Creating on Desktop (macOS) folder named PDFtoCSV
2. Inside PDFtoCSV create 2 folders named: pdf, csv
3. All filles from pdf folder will be converted into csv files and storen inside csv folder

Scritp ignores all non .PDF files inside the pdf folder

######## pyinstaller --onefile issues ###########
There are issues compoling the script using pyinsteller - missing tabula-version-jar-with-dependencies.jar file.

Wrokaround is to use line as bellow:

#pyinstaller --onefile --add-binary "/PATH/TO/FILE/tabula-1.0.5-jar-with-dependencies.jar:./tabula/" main.py

IMPORTANT!!!! between in place '(...).jar:./tabula/' the ':' is used for UNIX based system (macOS, linux), use ';' if you are going to compail it on Windows



Enjoy!
Marcel S.
