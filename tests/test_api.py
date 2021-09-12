import requests

from covid.api import api

from tests.mocks.mock_requests import MockRequest, MockRequestNoData, MockRequestError
from tests.mocks.mock_country import MockCountry

def test_process_data(monkeypatch, mocker):
  monkeypatch.setattr(requests, "get", MockRequest)
  
  country = MockCountry()
  spy = mocker.spy(MockCountry, 'set_data')

  api.get_remote_data([country])

  spy.assert_called_once_with(confirmed=5283, deaths=126, recovered=2353)
  monkeypatch.undo()

def test_process_no_data(monkeypatch, capsys):
  monkeypatch.setattr(requests, "get", MockRequestNoData)
  
  country = MockCountry()

  api.get_remote_data([country])
  captured = capsys.readouterr()

  assert "No data" in captured.out
  monkeypatch.undo()

def test_process_data_error(monkeypatch, capsys):
  monkeypatch.setattr(requests, "get", MockRequestError)
  
  country = MockCountry()

  api.get_remote_data([country])
  captured = capsys.readouterr()

  assert "No response" in captured.out
  monkeypatch.undo()
