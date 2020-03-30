import csv
from datetime import datetime
import requests


def get_files(day):
    # Downloads the files from the REPO and places them in the data/raw folder 
    r = requests.get(f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{day}.csv")
    file = r.text
    with open(f'./data/raw/{day}-raw.csv','w') as infile:
        for line in file:
            infile.write(line)

def format_files(day):
    # Swaps the column order and fills out missing data for countries and states
    with open(f'./data/raw/{day}-raw.csv', encoding="utf-8-sig") as infile, open(f'./data/{day}.csv', 'w') as outfile:
        reader = csv.DictReader(infile)
        headers = ["Country/Region","Province/State","Last Update","Confirmed","Deaths","Recovered","Latitude","Longitude"]
        writer = csv.DictWriter(outfile,fieldnames=headers)
        writer.writeheader()
        for line in reader:
            if not line["Province/State"]:
               line["Province/State"] = line["Country/Region"]
            writer.writerow(line)

def main():
    # Run everything you fool
    for i in range(1,32):
        if i <= 9:
            i = "0"+str(i)
        day = f"03-{i}-2020"
        get_files(day)
        format_files(day)

if __name__ == "__main__":
    main()