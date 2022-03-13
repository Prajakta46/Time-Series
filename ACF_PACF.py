from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
import matplotlib.pyplot as plt

# Reading in Data - we have monthly data here
df_ice_cream = pd.read_csv('ice_cream.csv')
print("First few rows: \n", df_ice_cream.head())
print("\n Shape of the dataframe", df_ice_cream.shape)
print("\n Dataframe Description \n ", df_ice_cream.describe())

# Renaming the Columns
df_ice_cream.rename(columns={'DATE':'date', 'IPN31152N':'production'}, inplace=True)

# Converitng date column to datetime format
df_ice_cream['date'] = pd.to_datetime(df_ice_cream.date)

# Setting date as index
df_ice_cream.set_index('date', inplace=True)

# Taking data 2010 onwards
start_date = pd.to_datetime('2010-01-01')
df_ice_cream = df_ice_cream[start_date:]

print("First few rows: \n", df_ice_cream.head())
print("\n Shape of the dataframe", df_ice_cream.shape)

# Plotting the Time Series
plt.figure(figsize=(10,4))
plt.plot(df_ice_cream.production)
plt.title('Ice Cream Production over time', fontsize=20)
plt.ylabel('Production', fontsize=16)
for year in range(2011, 2021):
    plt.axvline(pd.to_datetime(str(year) + '-01-01'), color ='k', linestyle='--', alpha=0.2 )
plt.show()

# ACF plot - Considers both direct and indirect effects
acf_plot = plot_acf(df_ice_cream.production, lags = 100)
plt.show()


# PACF plot - Considers only the direct effects
pacf_plot = plot_pacf(df_ice_cream.production)
plt.show()