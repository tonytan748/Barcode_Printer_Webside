#coding=utf-8

import os,sys
import urllib2
import re

file_path=os.path.split(os.path.realpath(__file__))[0]
main_html='http://centrallinktech.com/'

classify_url='http://centrallinktech.com/System/WMS.html'
classify_re='<a href="../(.*?)"><img src="(.*?)" alt="(.*?)" width="131" height="25" border="0" />'
classify_file=os.path.join(file_path,'classify_file.txt')

classify_content_re='<div class="sub_content">(.*?)<div class="product_price">'
classify_content_file=os.path.join(file_path,'classify_content.txt')

company_list_file=os.path.join(file_path,'company_list.txt')
company_list_re='<div class="product_description">(.*?)<div id="apDiv13">'
company_url_re='<a href="(.*?)"><div class="product_description">'

product_list_file=os.path.join(file_path,'company_list.txt')
product_list_re=''

product_desc_file=os.path.join(file_path,'products.txt')
product_desc_re=''


def get_info(url,re_content):
	a=urllib2.urlopen(url)
	x=''
	for i in a.readlines():
		x=x+i.strip().strip('\n').strip()
	geta=re.compile(re_content)
	get_all=geta.findall(x)
	return get_all

def get_classify():
	a=get_info(classify_url,classify_re)
	with open(classify_file,'w') as f:
		for i in a:
			f.write('URL:' + main_html + i[0] + '\n')
			f.write('PHOTOURL:' + i[1] + '\n')
			f.write('NAME:' + i[2] + '\n')
			f.write('\n')
	
def get_classify_content():
	m=[]
	with open(classify_file,'r') as f1:
		for i in f1.readlines():
			if i.startswith('URL:'):
				m.append(i[4:].strip('\n'))
	with open(classify_content_file,'w') as f2:
		x=1
		for i in m:
			print i
			s=get_info(i,classify_content_re)
			print s
			if len(s):
				f2.write('This is the %s pages\n' % x)
				f2.write(s[0]+'\n')
				x+=1
	clear_html(classify_content_file)
				
def get_content(path,re_content):
	m=[]
	with open(classify_file,'r') as f1:
		for i in f1.readlines():
			if i.startswith('URL:'):
				m.append(i[4:].strip('\n'))
	with open(path,'w') as f2:
		for i in m:
			s=get_info(i,re_content)
			print s
			if len(s):
				f2.write(s[0]+'\n')
	clear_html(path)
	with open(path,'a') as f3:
		for i in m:
			s=get_info(i,company_url_re)
			print s
			if len(s):
				f3.write(s[0]+'\n')
		
def checktext(text):
	txt=text.replace('\n','').replace('&nbsp;','').strip('').strip('\n')
	a=''
	m=0
	i=None
	for i in txt:
		if i=='<':
			m+=1
		if i=='>':
			m=0
		if m==0:
			a=a+i
	a.replace('>','')
	return a
	
def clear_html(path):
	s=[]
	with open(path,'r') as f:
		for i in f.readlines():
			txt=checktext(i.strip())
			s.append(txt)
			
	with open(path,'w') as f1:
		for i in s:
			i=i.replace('\n','').replace('>','')
			if len(i) >0:
				f1.write(i)
				f1.write('\n')
				
def get_company_list_url():
	url_re=re.compile('<a href="(.*?)">(.*?)</a>')
	s=''
	with open(company_list_file,'r') as f:
		for i in f.readlines():
			s = s + i
	print s
	g=url_re.findall(s)
	with open(os.path.join(file_path,'company_url_list.txt'),'w') as f1:
		for j in g:
			if j:
				f1.write('URL:' + main_html + j[0] + '\n')
				f1.write('NAME:' + j[1] + '\n')
				f1.write('\n')
	
def get_product_list():
	pro_re_1='<div class="div1"><a href="(.*?)">(.*?)</a>'
	pro_re_2='<div class="div1"><p><a href="(.*?)">(.*?)</a>'
	m=[]
	with open(os.path.join(file_path,'company_url_list.txt'),'r') as f:
		s=f.readlines()
#		print s
		for k,i in enumerate(s):
			print k
			if i.startswith('TYPE:1'):
				title_list={}
				u=s[k+1][4:]
				name=(s[k+2].strip())[5:]
				print u
				head_url='/'.join((u.split('/'))[:-1])
				g1=get_info(u,pro_re_1)
				g2=get_info(u,pro_re_2)
				g1.extend(g2)
				title_list['name']=name
				x=[]
				for i in g1:
					b=list(i)
					b[0]=head_url + '/' + b[0]
					x.append(b)
				title_list['content']=x
					
				m.append(title_list)
#	print m
	with open(os.path.join(file_path,'company_content_list.txt'),'w') as z:
		for i in m:
			z.write(i['name']+'\n')
			z.write('\n')
			for j in i['content']:
				z.write('\t')
				z.write(j[1] + '\t' + j[0]+'\n')
	
	
if __name__=='__main__':
#	get_classify()
#	get_classify_content()
#	get_content(company_list_file,company_list_re)
#	get_company_list_url()
	get_product_list()