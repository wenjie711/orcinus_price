__author__ = 'Dazdingo'

from common.model.book import Book
class dangdangPipeline(object):
	#con = pymongo.Connection("localhost", 27017)
	#db = con.bestbuyer
	#def process_item(self, item, spider):
	#	if(len(item['ISBN']) == 0):
	#		return item
	#	dbdata = {"name":"","price":"","ISBN":"","author":"","press":""}
	#	dbdata["name"] = item["name"][0]
	#	dbdata["price"] = item["price"][0]
	#	dbdata["ISBN"] = item["ISBN"][0]
	#	dbdata["author"] = item["author"][0]
	#	dbdata["press"] = item["press"][0]
		#try:
		#	self.db.bookInfo.insert(dbdata)
		#except:
		#	print "====================================wocao"

    def process_item(self, item, spider):
        if(len(item['ISBN']) == 0):
            return item
        newbook = Book()
        newbook.title = item["name"][0]
        newbook.price = item["price"][0]
        newbook.isbn = item["ISBN"][0]
        newbook.author = item["author"][0]
        newbook.press = item["press"][0]
        newbook.instant_price = item["instant"][0]
        newbook.link = item["url"]
        newbook.cover = item["img"][0]
        newbook.desc = item["desc"][0]
        newbook.platform = "dangdang"
        # if newbook.isbn do not exist in book_info then
        #     insert into bookinfo
        # set newbook.time desc etc..
        # insert into bookgoodsinfo
        return item
