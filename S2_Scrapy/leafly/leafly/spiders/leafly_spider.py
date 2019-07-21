from scrapy import Spider, Request
from leafly.items import LeaflyItem
import re

class LeaflySpider(Spider):
    name = 'leafly_spider'
    allowed_urls = ['https://www.leafly.com/']
 
    with open('strain_urls.txt', 'r') as f:
        strain_urls = f.readlines()
        regex = re.compile(r'[\n]')
        strain_urls = [re.compile(r'[\n]').sub(" ", s).strip() for s in strain_urls]


    start_urls = strain_urls

#start_urls = ['https://www.leafly.com/hybrid/98-white-widow']
    
    
    
    def parse(self, response):
        Name = response.xpath('/html/body/main/div[1]/div[4]/div[1]/div/div[3]/text()').get()
        Leafly_Name = response.xpath('/html/body/main/div[1]/div[4]/div[1]/div/div[2]/text()').get()
        Type = response.xpath('/html/body/main/div[1]/div[4]/div[1]/div/div[1]/text()').get()
        Rating = response.xpath('/html/body/main/div[1]/div[4]/div[2]/meta[3]/@content').get()
        Number_of_Reviews = response.xpath('/html/body/main/div[1]/div[4]/div[2]/meta[1]/@content').get()
        Effect_1 = response.xpath('//*[@id="effects-tab-content"]/div[1]/div[1]/text()').get()
        Effect_2 = response.xpath('//*[@id="effects-tab-content"]/div[2]/div[1]/text()').get()
        Effect_3 = response.xpath('//*[@id="effects-tab-content"]/div[3]/div[1]/text()').get()
        Effect_4 = response.xpath('//*[@id="effects-tab-content"]/div[4]/div[1]/text()').get()
        Effect_5 = response.xpath('//*[@id="effects-tab-content"]/div[5]/div[1]/text()').get()
        Effect_Level_1 = response.xpath('//*[@id="effects-tab-content"]/div[1]/div[2]/@style').get()
        Effect_Level_2 = response.xpath('//*[@id="effects-tab-content"]/div[2]/div[2]/@style').get()
        Effect_Level_3 = response.xpath('//*[@id="effects-tab-content"]/div[3]/div[2]/@style').get()
        Effect_Level_4 = response.xpath('//*[@id="effects-tab-content"]/div[4]/div[2]/@style').get()
        Effect_Level_5 = response.xpath('//*[@id="effects-tab-content"]/div[5]/div[2]/@style').get()
        Medicinal_1 = response.xpath('//*[@id="medical-tab-content"]/div[1]/div[1]/text()').get()
        Medicinal_2 = response.xpath('//*[@id="medical-tab-content"]/div[2]/div[1]/text()').get()
        Medicinal_3 = response.xpath('//*[@id="medical-tab-content"]/div[3]/div[1]/text()').get()
        Medicinal_4 = response.xpath('//*[@id="medical-tab-content"]/div[4]/div[1]/text()').get()
        Medicinal_5 = response.xpath('//*[@id="medical-tab-content"]/div[5]/div[1]/text()').get()
        Medicinal_Level_1 = response.xpath('//*[@id="medical-tab-content"]/div[1]/div[2]/@style').get()
        Medicinal_Level_2 = response.xpath('//*[@id="medical-tab-content"]/div[2]/div[2]/@style').get()
        Medicinal_Level_3 = response.xpath('//*[@id="medical-tab-content"]/div[3]/div[2]/@style').get()
        Medicinal_Level_4 = response.xpath('//*[@id="medical-tab-content"]/div[4]/div[2]/@style').get()
        Medicinal_Level_5 = response.xpath('//*[@id="medical-tab-content"]/div[5]/div[2]/@style').get()
        Negative_1 = response.xpath('//*[@id="negatives-tab-content"]/div[1]/div[1]/text()').get()
        Negative_2 = response.xpath('//*[@id="negatives-tab-content"]/div[2]/div[1]/text()').get()
        Negative_3 = response.xpath('//*[@id="negatives-tab-content"]/div[3]/div[1]/text()').get()
        Negative_4 = response.xpath('//*[@id="negatives-tab-content"]/div[4]/div[1]/text()').get()
        Negative_5 = response.xpath('//*[@id="negatives-tab-content"]/div[5]/div[1]/text()').get()
        Negative_Level_1 = response.xpath('//*[@id="negatives-tab-content"]/div[1]/div[2]/@style').get()
        Negative_Level_2 = response.xpath('//*[@id="negatives-tab-content"]/div[2]/div[2]/@style').get()
        Negative_Level_3 = response.xpath('//*[@id="negatives-tab-content"]/div[3]/div[2]/@style').get()
        Negative_Level_4 = response.xpath('//*[@id="negatives-tab-content"]/div[4]/div[2]/@style').get()
        Negative_Level_5 = response.xpath('//*[@id="negatives-tab-content"]/div[5]/div[2]/@style').get()
        Flavor_1 = response.xpath('/html/body/main/div[4]/div[5]/ul/li[1]/div/text()').get()
        Flavor_2 = response.xpath('/html/body/main/div[4]/div[5]/ul/li[2]/div/text()').get()
        Flavor_3 = response.xpath('/html/body/main/div[4]/div[5]/ul/li[3]/div/text()').get()

        
        
        
        item = LeaflyItem()
        item['Name'] = Name
        item['Leafly_Name'] = Leafly_Name
        item['Type'] = Type
        item['Rating'] = Rating
        item['Number_of_Reviews'] = Number_of_Reviews
        item['Effect_1'] = Effect_1
        item['Effect_2'] = Effect_2
        item['Effect_3'] = Effect_3
        item['Effect_4'] = Effect_4
        item['Effect_5'] = Effect_5
        item['Effect_Level_1'] = Effect_Level_1
        item['Effect_Level_2'] = Effect_Level_2
        item['Effect_Level_3'] = Effect_Level_3
        item['Effect_Level_4'] = Effect_Level_4
        item['Effect_Level_5'] = Effect_Level_5
        item['Medicinal_1'] = Medicinal_1
        item['Medicinal_2'] = Medicinal_2
        item['Medicinal_3'] = Medicinal_3
        item['Medicinal_4'] = Medicinal_4
        item['Medicinal_5'] = Medicinal_5
        item['Medicinal_Level_1'] = Medicinal_Level_1
        item['Medicinal_Level_2'] = Medicinal_Level_2
        item['Medicinal_Level_3'] = Medicinal_Level_3
        item['Medicinal_Level_4'] = Medicinal_Level_4
        item['Medicinal_Level_5'] = Medicinal_Level_5
        item['Negative_1'] = Negative_1
        item['Negative_2'] = Negative_2
        item['Negative_3'] = Negative_3
        item['Negative_4'] = Negative_4
        item['Negative_5'] = Negative_5
        item['Negative_Level_1'] = Negative_Level_1
        item['Negative_Level_2'] = Negative_Level_2
        item['Negative_Level_3'] = Negative_Level_3
        item['Negative_Level_4'] = Negative_Level_4
        item['Negative_Level_5'] = Negative_Level_5
        item['Flavor_1'] = Flavor_1
        item['Flavor_2'] = Flavor_2
        item['Flavor_3'] = Flavor_3
        
        
        
        yield item



