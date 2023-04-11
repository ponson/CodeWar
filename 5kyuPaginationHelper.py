class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.items_per_page = items_per_page
        self.itemsCount = len(collection)
        self.pagesCount = self.itemsCount // items_per_page
        self.lastItems = self.itemsCount % items_per_page
        if self.lastItems > 0:
            self.pagesCount += 1

    # returns the number of items within the entire collection
    def item_count(self):
        return self.itemsCount 

    # returns the number of pages
    def page_count(self):
        return self.pagesCount

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index in range(self.pagesCount):
            if page_index == self.pagesCount - 1 and self.lastItems > 0:
                return self.lastItems
            else:
                return self.items_per_page
        else:
            return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index in range(self.itemsCount):
            return item_index // self.items_per_page
        else:
            return -1

helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)

print(helper.page_count())  # should == 2
print(helper.item_count())  # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1))  # last page - should == 2
print(helper.page_item_count(2))  # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5))  # should == 1 (zero based index)
print(helper.page_index(2))  # should == 0
print(helper.page_index(20))  # should == -1
print(helper.page_index(-10))  # should == -1 because negative indexes are invalid
