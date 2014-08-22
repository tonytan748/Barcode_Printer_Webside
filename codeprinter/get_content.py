#coding=utf-8

import os
import urllib,urllib2
import sys
import re

main_html='http://centrallinktech.com/'


classify_re='<td width="131" align="middle"><a href="../(.*?)"><img src=".*?" alt="(.*?)" width="131" height="25" border="0" />'
#url / name

classify_desc_re='<div class="sub_content">(.*)<div class="product_price">'

company_list_re='<div class="product_detail"><a href="(.*?)">'
#<div class="product_description">	<div class="product_imageA"><img src="(.*?)" height="65"></div>	<b>(.*?)</b><br>.*?<div class="product_price">'

file_path=os.path.split(os.path.realpath(__file__))[0]

cla_path=os.path.join(file_path,'classify.txt')
desc_file_path=os.path.join(file_path,'classify_desc.txt')
company_path=os.path.join(file_path,'company_list.txt')

def get_info(url,re_content):
	try:
		a=urllib2.urlopen(url).read()
	except Exception,e:
		print str(e)
	m=a.replace('\n','')
	m=m.replace('\t','')
	print len(m.split('\n'))
	return m
	
#	g=re.compile(re_content)
#	classify=g.findall(m)
#	return classify

def get_classify_content(url):
	m=get_info(url,classify_re)
	with open(os.path.join(file_path,'classify.txt'),'w') as f:
		for i in m:
			f.write('NAME:' + i[1] + '\n')
			f.write('URL:' +main_html + i[0] + '\n')

def get_classify_desc():
	urls=[]
	with open(cla_path,'r') as f:
		for i in f.readlines():
			if i.startswith('URL:'):
				urls.append((i[4:]).strip('\n'))
#	print urls

	with open(desc_file_path,'w') as g:
		x=1
		for i in urls:
			desc=get_info(i,classify_desc_re)
#			print desc[0]
			try:
				g.write('this is the %s content:\n' % str(x))
				g.write(desc[0]+'\n')
				x+=1
			except IndexError:
				pass

def get_company():
	urls=[]
	with open(cla_path,'r') as f:
		for i in f.readlines():
			if i.startswith('URL:'):
				urls.append((i[4:]).strip('\n'))
	print urls
	with open(company_path,'w') as g:
		for i in urls:
			desc=get_info(i,company_list_re)

			g.write(desc)
#			try:
#				g.write('URL:' + desc[0] + '\n')
#				g.write('PHOTO_URL:' + desc[1] + '\n')
#				g.write('NAME:' + desc[2] + '\n')
#			except IndexError:
#				pass
	x=''
	with open(company_path,'r') as f1:
		for i in f1.readlines():
			x=x+i.strip('\n')
	with open(company_path,'w') as f2:
		f2.write(x)


if __name__ == '__main__':
#	get_classify_content('http://centrallinktech.com/System/WMS.html')
#	get_classify_desc()
	get_company()