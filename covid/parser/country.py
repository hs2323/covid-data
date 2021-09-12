class Country:
  """Country data and API response."""

  def __init__(self, date, iso): 
    self.date = date 
    self.iso = iso

  def set_data(self, confirmed, deaths, recovered):
    self.confirmed = confirmed
    self.deaths = deaths
    self.recovered = recovered