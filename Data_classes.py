# Programming challenge: implement a dataclass

from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Asset(ABC):
  price: float

  @abstractmethod
  def _lt_(self, other):
    pass

@dataclass
class Stock(Asset):
    ticker: str
    company: str

    def _lt_(self, other):
      return self.price < other.price

@dataclass
class Bond(Asset):
  description: str
  duration: int
  yieldamt: float

  def_lt_(self, other):
    return self.yieldamt < other.yieldamt

# TEST CODE
stocks = [
  Stock("MSFT", 342.0, "Microsoft Corp"),
  Stock("GOOG", 135.0, "Google Inc"),
  Stock("META", 275.0, "Meta Platforms Inc"),
  Stock("AMZN", 120.0, "Amazon Inc")
]
