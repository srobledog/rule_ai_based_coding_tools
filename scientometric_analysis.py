import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("data/scopus_dt_count.csv")

plt.plot(df.DT, df.FREQUENCY, label="Ransom")
plt.show()
