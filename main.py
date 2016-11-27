
import pandas as pd
import requests as r
from time import sleep


def scrape_data(year, week):    
    #create url
    url = 'http://rotoguru1.com/cgi-bin/fyday.pl?year=%s&week=%s&game=fd&scsv=1'
    url = url %(year, week)

    #the table begins with "pre" tags
    start_flag = '<pre>'
    end_flag = '</pre>'

    #user agent spoofing
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    #actually make hte request
    resp = r.get(url, headers=headers)

    #find the location of the "pre" tags
    start = resp.content.index(start_flag) + len(start_flag)
    end = resp.content.index(end_flag)

    #extract only that part of the response within the pre tags
    out = resp.content[start:end]

    #split string into list of lists
    lines = [item.strip().split(';') for item in out.split('\n')]

    #drop the last list because it's always empty
    #(it ends with a semi-colon, so it's always got a trailing blank)
    lines = lines[:-1]

    #construct pandas dataframe from the data
    df = pd.DataFrame(lines[1:], columns = lines[0])
    return df


if __name__ == '__main__':
    #create list of years and weeks
    years = list(range(2011,2017))
    weeks = list(range(1, 18))

    #loop over years and weeks, pull data for each yearweek
    #append results to a list
    output = list()
    for year in years:
        print year
        for week in weeks:
            print '\t', week
            #this script was written during week 12 of 2016
            if year == 2016 and week > 11:
                break
            df = scrape_data(year, week)
            output.append(df)
            sleep(3)

    #concatenate list into one large DataFrame
    out = pd.concat(output)
    out.to_csv('all_data.csv', index = False)
