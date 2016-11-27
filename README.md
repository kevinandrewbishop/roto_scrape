# roto_scrape
scrape Fanduel data from rotoguru

##Source Info
rotoguru1.com has a very simple api to pull fantasy data
for each player at the game level. It returns semicolon-delimited
data that is very easily parsed. The data goes back to 2011 and,
as of the time of writing, it is updated weekly on the same
schedule as FanDuel. A "Week" starts on the Thursday night games
and ends with the Monday night games.


##Usage
To scrape data, pass the year and week to the scrape_data function
like this:

```python
df = scrape_data(year = 2015, week = 7)
```

df is now a pandas DataFrame containing the FanDuel data
for week 7 of year 2015.
