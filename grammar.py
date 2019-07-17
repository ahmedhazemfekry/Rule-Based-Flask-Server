from pyknow import *

class Knowledge(KnowledgeEngine):
  category = ""
  @Rule(Fact(title = P(lambda title : title.find("Cola")!=-1)))
  def categorizeA(self):
      self.category = "Soft Drink"

  @Rule(Fact(title = P(lambda title : title.find("Cola")==-1)))
  def categorizeB(self):
      self.category = "Others"
