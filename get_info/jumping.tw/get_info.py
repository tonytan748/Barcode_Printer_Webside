#coding=utf-8
import urllib,urllib2
import os,sys
import re

main_url="http://www.jumping.tw/"

product="http://www.jumping.tw/products_menu.html"

main_re='<div class="product_list"><a href="(.*?)"><img src="(.*?)" .*?><p>(.*?)</p></a>'

class_re='<li><a href="(.*?)" class="nav">(.*?)</a></li>'

products_re_url='<td width="30%" rowspan="2"><a href="(.*?)">'

products_re_content='<table .*? table>'

def get_content(url,re_content):
	x=urllib2.urlopen(url).read()
	a=x.replace('\n','')
	get_url=re.compile(re_content)
	m=get_url.findall(a)
	return m

def get_classify():
	m=get_content(product,main_re)
	url_list=[{'URL':main_url+str(i[0]),'SRC':i[1],'NAME':i[2]} for i in m]
	return url_list

def get_product_list(url):
	m=get_content(url,class_re)
	url_list=[{'URL':main_url+i[0],'NAME':i[1]} for i in m]
	return url_list

def get_products_detail(url):
	m=get_content(url,products_re_url)
	#url / src / url / name / desc
	return m
#	g=[{'URL':m[0]} for i in m]
#	return g
	
def get_products_content(url):
	m=get_content(url,products_re_content)
	
def main():
	a=get_classify()
	print a
	filepath=os.path.split(os.path.realpath(__file__))[0]
	#print filepath
	class_file_name=os.path.join(filepath,'classify.txt')
	product_name_list=os.path.join(filepath,'products_list.txt')
	
	with open(class_file_name,'w') as f:
		for i in a:
			f.write(str(i['NAME']) + ':' + str(i['URL']))
			f.write('\n')
				
	
	with open(product_name_list,'w') as g:
		for j in a:
			#print j
			g.write(str(j['NAME']) + '\n')
			product_name=get_product_list(str(j['URL']))
			for k in product_name:
				print k
				g.write(str(k['NAME']) + ':' + str(k['URL']) + "\n")

def get_products_detail_list():
	a=get_classify()
	#print a
	filepath=os.path.split(os.path.realpath(__file__))[0]
	#print filepath
	class_file_name=os.path.join(filepath,'classify.txt')
	product_name_list=os.path.join(filepath,'products_list.txt')
	prduct_name_detail_list=os.path.join(filepath,'products_detail.txt')
	prduct_name_detail_content=os.path.join(filepath,'products_content.txt')	
	
	with open(prduct_name_detail_content,'w') as g:
		for j in a:
			product_name=get_product_list(str(j['URL']))
			for k in product_name:
				products_detail_url=get_products_detail(k['URL'])
				for m in products_detail_url:
					print str(m)
					g.write(main_url + str(m) + '\n')
				
				

title_photo='<img src="(.*?)" alt=".*?" title=".*?"  width="338" height="319">'
title='<h1>(.*?)</h1>'
action='<p>(.*?)</p>'

tttt='<div class="title"><div class="left"><img src="(.*?)" alt=".*?" title=".*?"  width="338" height="319"></div> <div class="right"><h1>(.*?)</h1>.*<h2>.*?</h2><p>(.*?)</p>.*?<div class="tab_container"><div id="tab1" class="tab_content">(.*?)</div>.*<div id="tab2" class="tab_content"><table width="100%" sizcache="11" sizset="0">(.*?)</div><div id="tab3" class="tab_content">(.*?)</div><div id="tab4" class="tab_content">'

def get_product_content():
	filepath=os.path.split(os.path.realpath(__file__))[0]
	with open(os.path.join(filepath,'products_content.txt'),"r") as f:
		s = f.readlines()
	with open(os.path.join(filepath,'products_all_content.txt'),"w") as x:
		for i in s:
			m=get_content(i,tttt)
			print len(m[0])
			x.write('URL:' + main_url + m[0][0])
			x.write('\n')
			x.write('NAME:' + m[0][1])
			x.write('\n')
			x.write('注意事項:' + m[0][2])
			x.write('\n')
			x.write('商品詳細介紹:' + m[0][3])
			x.write('\n')
			x.write('規格說明:' + m[0][4])
			x.write('\n')
			x.write('下載專區:' + m[0][5])
			x.write('\n')

if __name__=='__main__':
	#main()
	#get_products_detail_list()
	get_product_content()