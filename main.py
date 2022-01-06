import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def zero_to_nan(values):
    """Replace every 0 with 'nan' and return a copy."""
    return [float('nan') if x == 0 else x for x in values]


def display_scatter_plot(title, x_assis_label, x_axis_values, y_axis_label, y_axis_values):
    plt.figure()
    plt.title(title)
    plt.xlabel(x_assis_label)
    plt.ylabel(y_axis_label)
    plt.plot(x_axis_values, y_axis_values, marker='o')
    plt.show()


def display_plot(title, x_assis_label, x_axis_values, y_axis_label, y_axis_values):
    plt.figure()
    plt.title(title)
    plt.xlabel(x_assis_label)
    plt.ylabel(y_axis_label)
    plt.plot(x_axis_values, y_axis_values)
    plt.show()


# reads the cdv file
cols = list(pd.read_csv("log3.csv", nrows=1, sep=';', index_col=False, on_bad_lines='skip'))
data = pd.read_csv("log3.csv", sep=';', index_col=False, on_bad_lines='skip', usecols =[i for i in cols if i != 'TimeStamp'])

millis = data['Millis'].to_numpy()

# displays IBI plot
IBI = data['IBI'].to_numpy()
# removes extreme values
IBI[IBI > 1000] = np.nan
IBI = zero_to_nan(IBI)
display_scatter_plot("IDI", "Millis", millis, "IBI", IBI)

# displays EDA plot
EDA = data['EDA'].to_numpy()
display_plot("EDA", "Millis", millis, "EDA", EDA)


# displays pressure plot
pressure = data['Pressure'].to_numpy()
pressure = zero_to_nan(pressure)
display_scatter_plot("Pressure", "Millis", millis, "Pressure", pressure)



