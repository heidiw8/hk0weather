# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

#class Hk0WeatherPipeline(object):
#    def process_item(self, item, spider):
#        return item

from weatherdata.models import WeatherData

class Hk0RegionalPipeline(object):

  def process_item(self, item, spider):
    item.save()
    return item
