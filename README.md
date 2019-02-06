# CSV Report Processing

This is first test project for [ClearCode internship program](https://clearcode.cc/) which parses Input CSV file and outputs a new CSV file according
to the given format criteries

### Initial Configuration

In order to execute this application you would need:
- File in CSV format "Input.csv" located in the same folder
- Import following libraries: pycountry, math, datetime, csv

## Features

Main functionality of the application:
- Application takes an input file in csv format with the following colums of data:
  date(MM/DD/YYYY), state name, number of impressions, CTR percentage;
- Using pycountry library programm find three letter country code for each state name;
- During execution of the programm data will be sorted lexicographically by date
followed by the country code;
- The final output is in format of csv file with the following columns:
date (YYYY-MM-DD),three letter country code (or XXX for unknown states), number of impressions, number of
clicks (rounded, assuming the CTR is exact)

## Links to used libraries in the project

- Pycountry: https://pypi.org/project/pycountry/

## Licensing

"The code in this project is licensed under MIT license."
