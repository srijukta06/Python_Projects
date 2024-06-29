# Programming challenge: define a class to represent a stock symbol

class Stock:
  def _init_(self, ticker, price, company) -> None:
    self.ticker = ticker
    self.price = price
    self.company = company

  def get_description (self):
    return f"{self.ticker}: {self.company}--${self.price}"

# TEST CODE
msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock ("GOOG", 135.0, "Google Inc")
meta = Stock ("META", 275.0, "Meta Platforms Ine") 
amzn = Stock ("AMZN", 135.0, "Amazon Inc")

print(msft.get_description())
print (goog.get description())
print(meta.get_description())
