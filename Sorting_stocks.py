# Programming challenge: add methoda for comparison and equality

from abc import ABC, abstractmethod

class Asset(ABC):
  def_init_(self, price):
    self.price = price

  @abstractmethod
  def_str_(self):
    pass

class Stock(Asset):
  def_init_(self, ticker, price, company):
    super()._init_(price)
    self.company = company
    self.ticker = ticker
  
  def _str_(self):
    return f"{self.ticker}: {self.company} -- ${self.price}"

  def _lt_(self, other):
    return self.price < other.price

class Bond(Asset):
  def _init_(self, price, description, duration, yieldamt):
    super()._init_(price)
    self.description = description
    self.duration = duration
    self.yieldamt = yieldamt

def _str_(self):
  return f"{self.secription}: {self.duration}yr : ${self.price} : {self.yieldamt}

def _lt_(self, other):
  return self.yieldamt < other.yieldamt
