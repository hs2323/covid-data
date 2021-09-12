import openpyxl

from covid.parser import parser

from tests.mocks.mock_country import MockCountry
from tests.mocks.mock_workbook import MockWorkbook, MockWorkbookError

def test_open_excel(mocker, monkeypatch):
  _mock_workbook(mocker, monkeypatch, MockWorkbook)

  data = parser.open_excel('/some-path')

  assert data[0].iso == 'abc'
  assert data[0].date == '2021-01-01'
  monkeypatch.undo()

def test_open_excel_attribute_error(mocker, monkeypatch, capsys):
  _mock_workbook(mocker, monkeypatch, MockWorkbookError)

  parser.open_excel('/some-path')

  captured = capsys.readouterr()
  assert 'Issue parsing row' in captured.out
  monkeypatch.undo()

def _mock_workbook(mocker, monkeypatch, workbook):
  monkeypatch.setattr(openpyxl, "load_workbook", workbook)
  m = mocker.Mock()
  m('covid.parser.country', MockCountry)
