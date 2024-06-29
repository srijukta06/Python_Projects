# Programming challenge: use inheritance and abstract classes

from abc import ABC, abstractmethod

class Asset (ABC):
  def _init_(self, price): 
    self.price = price

  @abstractmethod
  def get_description (self): 
    pass
    
class Stock(Asset):
  def _init_(self, ticker, price, company):
    super(). _init_(price)
    self.company = company
    self.ticker = ticker

  def get_description(self):
    return f"{self.ticker}: {self.company} -- ${self.price}"

class Bond(Asset):
  def _init_(self, price, description, duration, yieldamt):
  super()._init_(price)
  self.description = description
  self.duration = duration
  self.yieldamt = yieldamt

  def get_description (self): 
    return f"{self.description}: {self.duration} yr : ${self.price} : {self.yieldamt}
