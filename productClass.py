"""

This program sets up the class system by which products will be classified in smartStore

"""

class Product(object):

    def __init__(self,name,quantity,relationPLU,relationQuantity):
        self.name = name
        self.quantity = quantity
        self.relationPLU = relationPLU
        self.relationQuantity = relationQuantity

    def getName(self,name):
        return name
    def getQuantity(self,quantity):
        return quantity
    def getRelationPLU(self,relationPLU):
        return relationPLU
    def getRelationQuantity(self,relationQuantity):
        return relationQuantity
