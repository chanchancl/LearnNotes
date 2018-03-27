
import re

text = '''2017-03-18 21:38:14 [scrapy.core.scraper] DEBUG: Scraped from <200 http://pankiti.tumblr.com/>
{'name': 'tumblr_omyqw3jBZq1qa7c9no1_500.jpg',
 'src': 'http://68.media.tumblr.com/ba34c472b819a5bc9b5df2a985e311f3/tumblr_omyqw3jBZq1qa7c9no1_500.jpg'}
2017-03-18 21:38:14 [scrapy.core.scraper] DEBUG: Scraped from <200 http://pankiti.tumblr.com/>
{'name': 'tumblr_omyqulmPlu1qa7c9no1_1280.jpg',
 'src': 'http://68.media.tumblr.com/2ad80df433b966f5d1b54c7085e78742/tumblr_omyqulmPlu1qa7c9no1_1280.jpg'}
2017-03-18 21:38:14 [scrapy.core.scraper] DEBUG: Scraped from <200 http://pankiti.tumblr.com/>
{'name': 'tumblr_omyqdvSpVG1qa7c9no1_1280.jpg',
 'src': 'http://68.media.tumblr.com/f96120bf519646d40e9087de8528f33d/tumblr_omyqdvSpVG1qa7c9no1_1280.jpg'}
2017-03-18 21:38:14 [scrapy.core.scraper] DEBUG: Scraped from <200 http://pankiti.tumblr.com/>
{'name': 'tumblr_omyqciM8l61qa7c9no1_1280.jpg',
 'src': 'http://68.media.tumblr.com/31bd8bb78e4aa1091d77bce7cbd523a2/tumblr_omyqciM8l61qa7c9no1_1280.jpg'}
2017-03-18 21:38:14 [scrapy.core.scraper] DEBUG: Scraped from <200 http://pankiti.tumblr.com/>
{'name': 'tumblr_omyqbkH0SM1qa7c9no1_1280.jpg',
 'src': 'http://68.media.tumblr.com/5e9abf2ef93639b35f89141214071f1f/tumblr_omyqbkH0SM1qa7c9no1_1280.jpg'}
2017-03-18 21:38:14 [scrapy.core.scraper] DEBUG: Scraped from <200 http://pankiti.tumblr.com/>
http://123.png'''

p = re.compile('(http://.*\.tumblr\.com/.*(?:\.jpg|\.png))')

print(p.findall(text))

p2 = re.compile('\'name\': \'(.*)\'')

print(p2.findall(text))