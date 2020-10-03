class ShopOption:
    purchases = 0
    upgrades = 0

    def __init__(self, name, description, upgradeDescription, purchaseCost, upgradeCost, possiblePurchases=1, possibleUpgrades=1):
        self.name = name
        self.purchaseCost = purchaseCost
        self.upgradeCost = upgradeCost
        self.description = description
        self.upgradeDescription = upgradeDescription
        self.purchaseCost = purchaseCost
        self.upgradeCost = upgradeCost
        self.possiblePurchases = possiblePurchases
        self.possibleUpgrades = possibleUpgrades

    def purchase(self):
        if self.purchases < self.possiblePurchases:
            self.purchases += 1
            return True
        elif self.upgrades < self.possibleUpgrades:
            return self.upgrade()
        else:
            return False
    
    def upgrade(self):
        if self.upgrades < self.possibleUpgrades:
            self.upgrades += 1
            return True
        else:
            return False
    
    def getName(self):
        return self.name
    
    def getCost(self):
        if self.purchases >= self.possiblePurchases:
            return self.upgradeCost
        else:
            return self.purchaseCost
    
    def getDescription(self):
        if self.purchases < self.possiblePurchases:
            return self.description
        elif self.upgrades < self.possibleUpgrades:
            return self.upgradeDescription
        return ""

    def getShopString(self):
        if self.purchases < self.possiblePurchases:
            return self.name + " (x" + str(self.possiblePurchases - self.purchases) + ")"
        elif self.upgrades < self.possibleUpgrades:
            return self.name + " Upgrade (x" + str(self.possibleUpgrades - self.upgrades) + ")"
        elif self.possibleUpgrades > 0:
            return "No more upgrades! (" + self.name + ")"
        else:
            return "No more purchases! (" + self.name + ")"

    def canPurchase(self, knights):
        if self.purchases < self.possiblePurchases:
            return knights > self.purchaseCost
        elif self.upgrades < self.possibleUpgrades:
            return knights > self.upgradeCost
        
        return False

    def getProduction(self):
        return -1
    
    def getKSkill(self):
        return -1
    
    def getVikingsTrapped(self):
        return -1
    
    def getSubtractedSkill(self):
        return -1

class Barracks(ShopOption):
    def __init__(self):
        ShopOption.__init__(self, "Barracks", "Improves knight production by 2", "Improves knight production by 1", 5, 1, 1, 10)

    def getProduction(self):
        return (self.purchases * 2) + self.upgrades

class Weaponry(ShopOption):
    def __init__(self):
        ShopOption.__init__(self, "Weaponry", "Improves knight effectiveness by 7", "Improves knight effectiveness by 3", 15, 5, 1, 0)
    
    def getKSkill(self):
        return (self.purchases * 7) + (self.upgrades * 3)

class TrapFactory(ShopOption):
    def __init__(self):
        ShopOption.__init__(self, "Trap Factory", "Traps up to 10 vikings per battle", "Traps up to 5 more vikings per battle", 25, 15, 1, 5)

    def getVikingsTrapped(self):
        return (10 * self.purchases) + (5 * self.upgrades)

class RaMirror(ShopOption):
    def __init__(self):
        ShopOption.__init__(self, "Ra Mirror", "Decreases viking effectiveness by 3 per battle", "Decreases viking effectiveness by 1 more per battle", 30, 20, 1, 5)
    
    def getSubtractedSkill(self):
        return 3 * self.purchases + self.upgrades