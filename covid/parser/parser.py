import openpyxl
import sys

from .country import Country

def open_excel(path):
  """Opens an excel file

  Args:
      path (str): The file location of the spreadsheet

  Returns:
      list: a list of Country objects
  """

  print("Opening data excel file \n")

  try:
    workbook = openpyxl.load_workbook(path)
    worksheet = workbook.active
    data = []

    for row in worksheet.iter_rows(min_row=2):
      try:
        date = row[0].value.strftime("%Y-%m-%d")
        iso = row[1].value
        data.append(Country(date=date, iso=iso))
      except AttributeError:
        print ("Issue parsing row with ISO: " + row[1].value + " and Date:" + row[0].value + "\n")
 
    return data
  except openpyxl.utils.exceptions.InvalidFileException:
    print ("The data file does not exist or is in an invalid format \n")
    sys.exit("Exiting application")
