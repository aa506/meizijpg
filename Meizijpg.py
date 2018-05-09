# -*- coding = "UTF-8" -*-
from bs4 import BeautifulSoup
import requests
class meizi(object):

	def __init__(self):
		self.headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
		self.url = 'http://www.meizijpg.com/home/1'
		self.server = 'http://www.meizijpg.com'
		self.url_s ='http://www.meizijpg.com/home/'
		self.path = 'G:/meizitu/'
		self.g = '.jpg'
	def get_content(self):
		for i in range(1,81):
			self.z = self.url_s + str(i)
			req = requests.get(url=self.z,headers=self.headers)
			html = req.text
			suop = BeautifulSoup(html,'lxml')
			bf = suop.find('ul').find_all('img',height='330')
			k =0
			for a in bf:
				k +=1
				self.href = a["src"] #下载路径
				self.title = a['alt'] #标题
				self.down = self.server + self.href #下载路径
				self.one = requests.get(url=self.down).content#获取图片
				with open(self.path + self.title + self.g,'wb') as code:#写文件并保存
					code.write(self.one)
					print(k,self.title,self.down)
		print('下载完成')

		
if __name__ == '__main__':
	dl = meizi()
	print('下载图片中：')
	dl.get_content()
	

	
