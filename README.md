# COVID Data
Read data from an Excel file, grab API data and write it to a new Excel sheet.

## Configuration
To configure the Excel file, open data/countries.xlsx. Change the values in Date (ex. YYYY-MM-DD) and three digit ISO code (ex. USA) to get API results.

## Installation

### Local Installation
Make sure that Python 3.9 and pip are installed. Install the dependencies by running ```pip install -r requirements.txt```.

### Docker Installation
Go to the application directory and run the docker build command:
```docker build . --tag covid-data:[TAG]``` where ```[TAG]``` is the current application version.

## Usage

### Local Usage
Go to the application directory and run ```python -m covid --path /[PATH]``` where ```/[PATH]``` is the location where you want the Excel data saved.

### Docker Usage
Once the container is built, you can run ```docker run --rm -v [PATH]:/data covid-data``` where ```[PATH]``` is the local folder you would like to save the results in.
