import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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

numeric_df = df.select_dtypes(include=['number'])

print("Numeric Columns:")
print(numeric_df.columns)

corr_matrix = numeric_df.corr(method='pearson')

print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure(figsize=(10,8))


mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    square=True,
    cbar=True
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(script_dir / "correlation_heatmap.png", dpi=300)
plt.show()

sns.pairplot(
    numeric_df,
    diag_kind="kde",
    corner=True
)

plt.savefig(script_dir / "pairplot.png", dpi=300)
plt.show()


corr_pairs = corr_matrix.unstack()

corr_pairs = corr_pairs[corr_pairs != 1]

corr_pairs = corr_pairs.drop_duplicates()

positive = corr_pairs.sort_values(ascending=False)

negative = corr_pairs.sort_values()

print("\nTop 5 Positive Correlations")
print(positive.head())

print("\nTop 5 Negative Correlations")
print(negative.head())

print("\nSummary")
print("-"*40)

strong_pos = positive.index[0]
strong_neg = negative.index[0]

print(f"Strongest Positive Correlation:")
print(f"{strong_pos[0]} & {strong_pos[1]} = {positive.iloc[0]:.2f}")

print()

print(f"Strongest Negative Correlation:")
print(f"{strong_neg[0]} & {strong_neg[1]} = {negative.iloc[0]:.2f}")

print("\nInterpretation:")
print("""
The correlation heatmap displays Pearson correlation coefficients
between all numerical features. Dark red indicates strong positive
correlation, while dark blue indicates strong negative correlation.
The pairplot visualizes relationships between variables using scatter
plots and shows each variable's distribution along the diagonal.
Highly correlated variables may indicate dependency, while values
close to zero suggest little or no linear relationship.
""")