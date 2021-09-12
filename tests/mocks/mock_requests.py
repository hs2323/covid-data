class MockRequest:
  def __init__(self, *args, **kwargs): 
    self.status_code = 200

  @staticmethod
  def json(*args):
    return {
      'data': [
        { 'iso': 'abc', 'confirmed': 5283, 'deaths': 126, 'recovered': 2353 },
       ]
    }

class MockRequestNoData(MockRequest):
  @staticmethod
  def json(*args):
    return {
      'data': []
    }

class MockRequestError:
  def __init__(self, *args, **kwargs): 
    self.status_code = 500
