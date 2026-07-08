import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

script_dir = Path(__file__).resolve().parent
data_path = script_dir / "sales.csv"

df = pd.read_csv(
    data_path,
    sep=r"\s*\|\s*",
    engine="python",
    skiprows=[1],
    skipinitialspace=True,
)
df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
df.columns = df.columns.str.strip()

column = "Sales"     
group_col = "Region"  
sns.set(style="whitegrid")

plt.figure(figsize=(8,5))
sns.histplot(df[column], bins=30, kde=False, color="skyblue")
plt.title(f"Histogram of {column}")
plt.xlabel(column)
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(script_dir / "histogram.png", dpi=300)
plt.show()

plt.figure(figsize=(8,5))
sns.kdeplot(df[column], fill=True, color="green")
plt.title(f"KDE Plot of {column}")
plt.xlabel(column)
plt.tight_layout()
plt.savefig(script_dir / "kde_plot.png", dpi=300)
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df[column], color="orange")
plt.title(f"Boxplot of {column}")
plt.tight_layout()
plt.savefig(script_dir / "boxplot.png", dpi=300)
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x=group_col, y=column, data=df)
plt.title(f"{column} Distribution by {group_col}")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(script_dir / "group_boxplot.png", dpi=300)
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(
    data=df,
    x=column,
    hue=group_col,
    kde=True,
    element="step"
)
plt.title(f"{column} Distribution by {group_col}")
plt.tight_layout()
plt.savefig(script_dir / "group_histogram.png", dpi=300)
plt.show()

Q1 = df[column].quantile(0.25)
Q3 = df[column].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df[column] < lower) | (df[column] > upper)]

print("="*40)
print("Outlier Detection")
print("="*40)
print("Number of Outliers:", len(outliers))
print(outliers[[column]].head())

print("\nSummary Statistics")
print(df[column].describe())

print("\nSkewness :", df[column].skew())
print("Kurtosis :", df[column].kurt())

skew = df[column].skew()

if skew > 0.5:
    shape = "positively (right) skewed"
elif skew < -0.5:
    shape = "negatively (left) skewed"
else:
    shape = "approximately symmetric"

print("\nInterpretation:")
print(f"""
The distribution of {column} is {shape}. The histogram and KDE plot
show the overall distribution, while the boxplot highlights potential
outliers. A total of {len(outliers)} outliers were detected using the
IQR method. Comparing groups using boxplots reveals differences in
median, spread, and variability across {group_col}. These plots help
identify unusual observations and understand the overall data
distribution.
""")