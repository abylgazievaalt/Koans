class ClosingSale:
    def __init__(self):
        self.hamsters = 7
        self.zebras = 84

    def cameras(self):
        return 34

    def toilet_brushes(self):
        return 48

    def jellies(self):
        return 5
crazy_discounts = ClosingSale()
del ClosingSale.toilet_brushes
still_available = crazy_discounts.toilet_brushes()

