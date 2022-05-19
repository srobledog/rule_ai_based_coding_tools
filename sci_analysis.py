# %% [markdown]
# # Creating the environment

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# # Getting Data

# %%
data = pd.read_csv('https://docs.google.com/spreadsheets/d/12QwD4c5cYbFYb9eGrtwDGRn5ssEpIbYLSeEDm0BO5kM/export?format=csv&gid=1259389890')

# %% [markdown]
# # Scientific Production 

# %%
# select PY column from data and save it to a new variable called annual_production_1
annual_production = data['PY']

# group PY and count the unique values in annual_production and save the results to a new variable called annual_production_count
# arrange the index of annual_production_count in ascending order
annual_production_count = annual_production.value_counts().sort_index()

# create a bar plot from annual_production_count 
# show only the last 20 years
annual_production_count.tail(20).plot(kind='bar')


# %% [markdown]
# # journal production

# %%
# create a new variable with column SO from data named source
source = data['SO']
# group SO and count the unique values in source and save the results to a new variable called source_count
# arrange SO column in descending order
source_count = source.value_counts().sort_values(ascending=False)
# print source_count
print(source_count)

# %%
# Create a dataframe called 


