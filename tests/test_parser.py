import openpyxl
from pytest import raises

from covid.parser import parser

from tests.mocks.mock_country import MockCountry, MockCountryComplete
from tests.mocks.mock_workbook import MockWorkbook, MockWorkbookError, MockWorkbookSaveError

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

def test_write_excel(mocker, monkeypatch, capsys):
  _mock_workbook(mocker, monkeypatch, MockWorkbook)

  parser.write_excel('/some-path', [MockCountryComplete()])

  captured = capsys.readouterr()
  assert 'Saved COVID API' in captured.out
  monkeypatch.undo()

def test_write_excel_save_error(mocker, monkeypatch, capsys):
  with raises(SystemExit):
    _mock_workbook(mocker, monkeypatch, MockWorkbookSaveError)

    parser.write_excel('/some-path', [MockCountryComplete()])
    
    monkeypatch.undo()

def _mock_workbook(mocker, monkeypatch, workbook):
  monkeypatch.setattr(openpyxl, "load_workbook", workbook)
  monkeypatch.setattr(openpyxl, "Workbook", workbook)
  m = mocker.Mock()
  m('covid.parser.country', MockCountry)
