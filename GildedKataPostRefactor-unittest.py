# -*- coding: utf-8 -*-
import unittest

from GildedKataPostRefactor import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_within_sell_in_date(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 20, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_sell_in_date_passed(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_aged_brie_sell_in_date_decrease_quality_increase(self):
        items = [Item("Aged Brie", 20, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].sell_in)
        self.assertEqual(31, items[0].quality)

    #"Aged Brie" actually increases in Quality the older it gets
    # Once the sell by date has passed, Quality degrades twice as fast -> meaning for "Aged Brie" it increases twice as fast past sell date.
    def test_aged_brie_sell_in_date_passed_quality_increase_by_2(self):
        items = [Item("Aged Brie", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(32, items[0].quality)

    def test_aged_brie_quality_between_0_and_50(self):
        items = [Item("Aged Brie", 20, 0)]
        self.assertTrue(items[0].quality >= 0 and items[0].quality <= 50)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # self.assertEqual(50 , items[0].quality)
        self.print_sell_in_and_quality(items)

    #Quality of normal item degrades upon time passed.
    def test_normal_item_quality_degrade(self):
        items = [Item("Bow Of Peril", 20, 10)]
        gilded_rose = GildedRose(items)
        print ("########################################################")
        print ("normal degrade of quality ="+str(items[0].quality))
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)
        print ("normal degrade of quality ="+str(items[0].quality))
        print ("sell_in_days ="+str(items[0].sell_in))

    #Quality of normal item degrades twice as fast upon time passed.
    def test_normal_item_quality_degrade_twice_as_fast(self):
        items = [Item("Bow Of Peril", 0, 10)]
        gilded_rose = GildedRose(items)
        print ("########################################################")
        print ("#### Quality degrades twice as fast upon time passed.")
        print ("twice as fast degrade of quality ="+str(items[0].quality))
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        print ("twice as fast degrade of quality ="+str(items[0].quality))
        print ("sell_in_days ="+str(items[0].sell_in))

    #Quality of normal item cant be negative and above 50
    def test_normal_item_quality_between_0_and_50(self):
        items = [Item("Bow Of Peril", 10, 0)]
        self.assertTrue(items[0].quality >= 0 and items[0].quality <= 50)
        self.print_quality_and_seperator(items)
        print ("#### Quality of an item cant be negative or above 50")
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.print_sell_in_and_quality(items)

    #Quality of backstage pass increases over time passed above 10 days.
    def test_backstage_pass_quality_increases(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 45)]
        self.print_quality_and_seperator(items)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].sell_in)
        self.assertEqual(46, items[0].quality)
        self.print_sell_in_and_quality(items)

    #Quality of backstage pass increases by 2 over time passed between 10 days and 6 days
    def test_backstage_pass_quality_increases_by_2_between_10_and_6_days_left(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 45)]
        self.assertTrue(items[0].sell_in > 5 and items[0].sell_in <= 10)
        self.print_quality_and_seperator(items)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(47, items[0].quality)
        self.print_sell_in_and_quality(items)

    #Quality of backstage pass increases by 3 over time passed between 5 days and 0 days
    def test_backstage_pass_quality_increases_by_3_between_5_and_0_days_left(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 45)]
        self.assertTrue(items[0].sell_in > 0 and items[0].sell_in <= 5)
        self.print_quality_and_seperator(items)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(48, items[0].quality)
        self.print_sell_in_and_quality(items)

    #Quality of backstage pass when less then 0 days left => quality = 0
    def test_backstage_pass_quality_less_than_0_days_left(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    #Quality of backstage pass cant go above 50
    def test_backstage_pass_quality_cant_go_above_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 50)]
        self.print_quality_and_seperator(items)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.print_sell_in_and_quality(items)

    #Test the new conjured items which will be degrading twice as fast
    def test_conjured_items_quality_degrade_twice_as_fast(self):
        items = [Item("Conjured Unholy Flail +10", 15, 40)]
        self.print_quality_and_seperator(items)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(38, items[0].quality)
        self.print_sell_in_and_quality(items)

    def test_conjured_items_sell_in_0_quality(self):
        items = [Item("Conjured Unholy Flail +10", 0, 40)]
        self.print_quality_and_seperator(items)
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(36, items[0].quality)
        self.print_sell_in_and_quality(items)

    def print_sell_in_and_quality(self, items):
        print ("quality ="+str(items[0].quality))
        print ("sell_in_days ="+str(items[0].sell_in))

    def print_quality_and_seperator(self, items):
        print ("########################################################")
        print ("quality ="+str(items[0].quality))
        
if __name__ == '__main__':
    unittest.main()

#return "%s, %s, %s" % (self.name, self.sell_in, self.quality)