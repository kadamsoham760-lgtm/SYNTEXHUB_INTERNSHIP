import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style("whitegrid")

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

df = pd.read_csv(url)

df = df.drop(columns=["Province/State", "Lat", "Long"])

country_df = df.groupby("Country/Region").sum()

country_df.columns = pd.to_datetime(country_df.columns)

countries = ["India", "US", "Brazil"]

data = country_df.loc[countries].T

daily_cases = data.diff().fillna(0)

weekly_cases = daily_cases.resample("W").sum()

rolling_avg = daily_cases.rolling(window=7).mean()

plt.figure(figsize=(12,6))

for country in countries:
    plt.plot(data.index, data[country], label=country)

plt.title("Total COVID Cases")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend()

plt.savefig("total_cases.png")
plt.show()

plt.figure(figsize=(12,6))

for country in countries:
    plt.plot(daily_cases.index,
             daily_cases[country],
             label=country)

plt.title("Daily Cases")
plt.legend()

plt.savefig("daily_cases.png")
plt.show()

plt.figure(figsize=(12,6))

for country in countries:
    plt.plot(rolling_avg.index,
             rolling_avg[country],
             linewidth=2,
             label=country)

plt.title("7-Day Rolling Average")
plt.legend()

plt.savefig("rolling_average.png")
plt.show()

print("\nPEAK DAILY CASES\n")

for country in countries:
    peak = daily_cases[country].max()
    peak_date = daily_cases[country].idxmax()

    print(f"{country}")
    print(f"Peak Cases : {int(peak):,}")
    print(f"Peak Date  : {peak_date.date()}\n")

print("\nApproximate Growth Ratio\n")

growth = daily_cases / daily_cases.shift(1)

for country in countries:
    latest = growth[country].dropna().iloc[-1]
    print(country, ":", round(latest,2))

weekly_cases.to_csv("weekly_cases.csv")

print("\nweekly_cases.csv exported.")

print("\nConclusions")

for country in countries:

    peak = daily_cases[country].max()

    avg = daily_cases[country].tail(30).mean()

    print(f"\n{country}")
    print("Highest Daily Cases :", int(peak))
    print("Average Last 30 Days :", int(avg))

print("\nAnalysis Complete.")