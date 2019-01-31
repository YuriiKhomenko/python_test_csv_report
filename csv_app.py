import csv
import math
from datetime import datetime
import pycountry as pc

subdivisions = list(pc.subdivisions)
subdivisions_names = []

for item in subdivisions: # creating a list of all possible subdivision names
  subdivisions_names.append(item.name)

def get_c_code(state): # looks through the name of subdivision and returns three letter country code (alpha_3) 
  if state in subdivisions_names:
    index = subdivisions_names.index(state)
    item = pc.subdivisions.get(code=subdivisions[index].code)
    c_code = item.country.alpha_3
    return(c_code)
  elif state not in subdivisions_names:
    return('XXX')

def get_clicks(imp, ctr): # calculates clicks and returns the value rounded to the nearest integer and converts it as a string
  imp = int(imp)
  ctr = float(ctr.strip('%'))/100
  return str(math.ceil(imp * ctr))

def get_date(string_date): # returns data in the format YYYY-MM-DD
  date = datetime.strptime(string_date, '%m/%d/%Y')
  date.strftime('%Y-%m-%d')
  date = str(date)[:10]
  return date

output_data = []

with open('input.csv', 'r', encoding='UTF-8') as csv_file: # goes through the input file and changes the format of the rows
  csv_reader = csv.reader(csv_file)
  csv_reader = list(csv_reader)[1:]
  for row in csv_reader:
    row[0] = get_date(row[0])
    row[1] = get_c_code(row[1])
    row[3] = get_clicks(row[2], row[3])
    output_data.append(row)

output_data.sort()
output_data.insert(
    0, ['Date(YYYY-MM-DD)', 'Country_code', 'Number_Impressions', 'CTR'])

with open('output.csv', 'w', encoding='UTF-8') as csv_file:
  csv_writer = csv.writer(csv_file, delimiter=',')
  for row in output_data:
    csv_writer.writerow(row)
