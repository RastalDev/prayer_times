# Islamic Prayer Times

## Python script to display a daily Islamic prayer timetable

- Python script to scrape website content and parse the relevant content into a pandas dataframe to display to the user.
- This script, by default, uses the prayer timetable of Islamic relief UK for London.
- Script can be modified to display the prayer times from any location.
- If you live in UK, see [here](https://www.islamic-relief.org.uk/islamic-resources/prayer-timetables/), for a list of prayer times in different UK cities, select the nearest city to your location and then modify the script accordingly by inserting the appropriate URL.
- The script should work with any website displaying a single table of prayer times on a single web page for any location worldwide, simply modify the script in this case for whatever URL you wish to use.

## Necessary Python libraries which must be installed to run the script

- `urllib.request` is a standard library for Python3.
- [html-table-parser](https://pypi.org/project/html-table-parser-python3/): Install with pip using `pip install html-table-parser-python3`
- [pandas](https://pypi.org/project/pandas/): Install with pip using `pip install pandas`

## Example of output when script is run in a terminal emulator

![example.png](https://github.com/RastalDev/prayer_times/blob/master/example.png)

## License

This script is licensed under [GPLv3.](https://github.com/RastalDev/prayer_times/blob/master/LICENSE)

![gplv3.png](https://github.com/RastalDev/prayer_times/blob/master/gplv3.png)
