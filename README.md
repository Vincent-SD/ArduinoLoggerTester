# ArduinoLoggerTester


## What is it

The Arduino Logger Tester is a small python program that can be used to plot easily the IBI, EDA and pressure collected by the  [Arduino Logger](https://github.com/med-material/ArduinoLogger) from a CSV file.

## How to use

### Imports

The programs uses python and requires:
- pandas
- matplotlib
- sys
- os

You may need to install those modules. See how [here](https://docs.python.org/3/installing/index.html#basic-usage)

### Usage

The first step is to log data using the  [Arduino Logger](https://github.com/med-material/ArduinoLogger) program and save it to a csv file.

Once you have your CSV file, simply run the following command:
```bash
python arduino-logger-tester.py /path/to/csv/file.csv
```

If everything is set up correctly, you should be able to see the 3 graphs.
![image](https://user-images.githubusercontent.com/49280157/153022296-825ae7bb-5ee2-48fe-9a39-9784e9a248ac.png)

