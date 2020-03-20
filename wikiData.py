from pandas.io.html import read_html
import pandas
import csv

page = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
wikitables = read_html(page, attrs={"class":"wikitable"})
te = wikitables[0].to_csv()

#print(wikitables)
#print("extracted {} number of tables".format(len(wikitables)))
#print(wikitables[0].shape)
#wikitables[0]".shape" the .shape will give your dimensions of rows and columns. ".tail" will give you last 4 and .header is the first 4

with open('snp500.csv') as S:
    reader = csv.DictReader(S)
    #print(reader)
    candles = list(reader)

csv_file = open('snp500.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['ticker', 'name'])
for item in candles:
    csv_writer.writerow([item['Symbol'], item['Security']])

csv_file.close()
