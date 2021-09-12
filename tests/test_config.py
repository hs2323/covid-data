import configparser
from pytest import raises
from covid.config import config

from tests.mocks.mock_config_parser import MockConfigParser, MockConfigParserFailRead, MockConfigParserFailGet

def test_get_config(monkeypatch):

  monkeypatch.setattr(configparser, "ConfigParser", MockConfigParser)
  location = config.get_config('path', 'params')

  assert location == '/app/data.xlsx'
  monkeypatch.undo()

def test_get_config_read_error(monkeypatch):
  with raises(SystemExit):
    monkeypatch.setattr(configparser, "ConfigParser", MockConfigParserFailRead)
    config.get_config('path', 'params')
    monkeypatch.undo()

def test_get_config_get_error(monkeypatch):
  with raises(SystemExit):
    monkeypatch.setattr(configparser, "ConfigParser", MockConfigParserFailGet)
    config.get_config('path', 'params')
    monkeypatch.undo()
