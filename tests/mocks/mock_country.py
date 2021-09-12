class MockCountry:
  def __init__(self, *args, **kwargs):
    self.iso = 'abc'
    self.date = '2021-01-01' 

  @staticmethod
  def set_data(*args, **kwargs):
    pass

class MockCountryComplete(MockCountry):
  def __init__(self, *args, **kwargs):
    self.iso = 'abc'
    self.date = '2021-01-01' 
    self.confirmed = 5000
    self.deaths = 200
    self.recovered = 50
