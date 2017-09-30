# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os.path

from urllib.request import urlopen

class WeatherPipeline(object):
    def process_item(self, item, spider):
        today=time.strftime('%Y%m%d',time.localtime())
        fileName=today + '.txt'
        with open(fileName,'a') as fp:
            fp.write(str(item['cityDate'].encode('utf8')+ b'\t'))
            fp.write(str(item['week'].encode('utf8')+ b'\t'))
            imgName=os.path.basename(item['img'])
            fp.write(imgName+ '\t')
            if os.path.exists(imgName):
                pass
            else:
                with open(imgName,'wb') as fp:
                    response=urlopen(item['img'])
                    fp.write(response.read())

            fp.write(str(item['temperature'].encode('utf8') + b'\t'))
            fp.write(str(item['weather'].encode('utf8') + b'\t'))

            fp.write(str(item['wind'].encode('utf8') + b'\n\n'))
        time.sleep(1)
        return item
