from datetime import datetime

class MockWorkbook:
  def __init__(self, *args, **kwargs): 
    self.active = MockIterRows()
  
  @staticmethod
  def load_workbook(*args):
    pass

  @staticmethod
  def save(*args):
    return True

class MockWorkbookError(MockWorkbook):
  def __init__(self, *args, **kwargs): 
    self.active = MockIterRowsError()

class MockIterRows:
  @staticmethod
  def iter_rows(*args, **kwargs):
       cell1 = MockCell(datetime(2021,1,1))
       cell2 = MockCell('abc')
       return [[cell1, cell2]]

  def cell(*args, **kwargs):
    return MockCell

class MockIterRowsError:
  @staticmethod
  def iter_rows(*args, **kwargs):
       cell1 = MockCell('bad-date')
       cell2 = MockCell('abc')
       return [[cell1, cell2]]

class MockCell:
  def __init__(self, value=''):
    self.value = value