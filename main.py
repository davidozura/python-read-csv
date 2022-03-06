# read csv file journal onkologija articles pdf usage

import csv

with open('prenosi_pdf_clanki_revija_onkologija.csv', mode='r') as file:

    csvFile = csv.reader(file)

    for lines in csvFile:
        print(lines)
