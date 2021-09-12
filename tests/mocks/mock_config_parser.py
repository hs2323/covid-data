class MockConfigParser:

    @staticmethod
    def read(*args):
      return ['/some-file.ini']

    @staticmethod
    def get(*args):
      return '/app/data.xlsx'

class MockConfigParserFailRead:
    @staticmethod
    def read(*args):
      return []

class MockConfigParserFailGet:

    @staticmethod
    def read(*args):
      return ['/some-file.ini']

    @staticmethod
    def get(*args):
      raise
