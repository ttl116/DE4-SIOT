import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Core Temperatures (pandas)
core_temps = pd.read_csv('CT-log_all.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
print(type(core_temps)) # Gives what type of object the data file is
print(core_temps.head()) # Gives preview of first 5 rows of csv file

sns.set(rc={'figure.figsize':(20,10)})
plot = core_temps['Core 0'].plot(linewidth=0.5)
core_temps['Core 1'].plot(linewidth=0.5)
core_temps['Core 2'].plot(linewidth=0.5)
core_temps['Core 3'].plot(linewidth=0.5)

# London Temperatures (pandas)
LDN_temps = pd.read_csv('London-temp_all.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, dayfirst=True)
print(type(LDN_temps)) # Gives what type of object the data file is
print(LDN_temps.head()) # Gives preview of first 5 rows of csv file

sns.set(rc={'figure.figsize':(20,10)})
plot = LDN_temps['Temperature  [2 m above gnd]'].plot(linewidth=0.5)
plot.set_ylabel('Temperature (Celcius)')
plot.legend()
