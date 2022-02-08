import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import sys
import os

TIMESTAMP_COLUMN_LABEL = 'TimeStamp'
EDA_COLUMN_LABEL = 'EDA'
IBI_COLUMN_LABEL = 'IBI'
PRESSURE_COLUMN_LABEL = 'Pressure'
MILLIS_COLUMN_LABEL = 'Millis'


def zero_to_nan(values):
    """Replace every 0 with 'nan' and return a copy."""
    return [float('nan') if x == 0 else x for x in values]


def generator_scatter_plot(fig, title, x_assis_label, x_axis_values, y_axis_label, y_axis_values):
    plt.subplot(fig)
    plt.title(title)
    plt.xlabel(x_assis_label)
    plt.ylabel(y_axis_label)
    plt.plot(x_axis_values, y_axis_values, marker='o')


def generate_plot(fig, title, x_assis_label, x_axis_values, y_axis_label, y_axis_values):
    plt.subplot(fig)
    plt.title(title)
    plt.xlabel(x_assis_label)
    plt.ylabel(y_axis_label)
    plt.plot(x_axis_values, y_axis_values)


if len(sys.argv) < 2:
    print("No file provided, aborting")
    exit(0)
file = sys.argv[1]

if not os.path.exists(file):
    print("file " + file + "doesn't exist")
    exit(0)

# reads the csv file
cols = list(pd.read_csv(file, nrows=1, sep=';', index_col=False, on_bad_lines='skip'))
data = pd.read_csv(file, sep=';', index_col=False, on_bad_lines='skip', usecols =[i for i in cols if i != TIMESTAMP_COLUMN_LABEL])

fig = gridspec.GridSpec(2, 2, height_ratios=[1,1])
plt.subplots_adjust(wspace=0.5, hspace=0.5)
millis = data['Millis'].to_numpy()

# displays IBI plot
IBI = data[IBI_COLUMN_LABEL].astype(float).to_numpy()
# removes extreme values
IBI[IBI > 3000] = 3000
IBI = zero_to_nan(IBI)
generator_scatter_plot(fig[0], IBI_COLUMN_LABEL, MILLIS_COLUMN_LABEL, millis, IBI_COLUMN_LABEL, IBI)

# displays EDA plot
EDA = data[EDA_COLUMN_LABEL].to_numpy()
generate_plot(fig[1], EDA_COLUMN_LABEL, MILLIS_COLUMN_LABEL, millis, EDA_COLUMN_LABEL, EDA)

# displays pressure plot
pressure = data[PRESSURE_COLUMN_LABEL].to_numpy()
pressure = zero_to_nan(pressure)
generator_scatter_plot(fig[2], PRESSURE_COLUMN_LABEL, MILLIS_COLUMN_LABEL, millis, PRESSURE_COLUMN_LABEL, pressure)

plt.show()


