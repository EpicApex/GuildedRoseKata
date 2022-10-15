# -*- coding: utf-8 -*-
# Refactor guidelines
# - Search for duplication
# - Search for multiple nested conditionals
# - Search for negative code conditions and change them
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Handle the unique item Sulfuras -> so Ragnaros the Firelord can burst into his favourite flames given his uniquely magnificant hand
            if item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
                continue

            if item.name == "Aged Brie":
                self.item_increase_quality(item)
                item.sell_in = item.sell_in - 1

                if item.sell_in < 0:
                    self.item_increase_quality(item)
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                #item quality in this if statement can go above 50 and not be sulfurus, but right after that you have an if that takes care of the case where item quality is above 50 nad set it to 50 again.
                item.quality = item.quality + 1
                if item.sell_in < 11:
                    item.quality = item.quality + 1
                if item.sell_in < 6:
                    item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1

                if item.quality > 50:
                    item.quality = 50

                if item.sell_in < 0:
                    item.quality = 0
                continue

            if item.quality > 0:
                    item.quality = item.quality - 1
            
            item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.quality > 0:
                    item.quality = item.quality - 1

    def item_increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)