#-*-coding=utf-8-*-
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render,render_to_response,RequestContext
from django.template import RequestContext
# Create your views here.
from .models import WebInfo,Classify,Company,Product

from django.core.mail import send_mail

def all_info():
	m={}
	m['webinfo']=WebInfo.objects.get(pk=1)
	m['navbar']=Classify.objects.all()
	m['company']=Company.objects.all()
	m['product']=Product.objects.all()
	return m

def show_product_by_classify(classify_id):
	if classify_id:
		a=Product.objects.get(classify=classify_id)
		return a
	else:
		return False

def show_product_by_company(company_id):
	if company_id:
		a=Product.objects.get(company=company_id)
		return a
	else:
		return False

def web_info():
	webinfo=all_info()['webinfo']
	return webinfo

def index(request):
	context=RequestContext(request)
	webinfo=web_info()

	classify=all_info()['navbar']
	companylist=all_info()['company'][:6]
	productlist=all_info()['product'][:4]
	
	print request.session['order']
	order_qty=len(set(str(request.session['order']).split(',')))
	
	if request.method == 'POST':
		#p=request.POST['p']
		product=Product.objects.get(name=request.POST['p'])
		product_id=product.id
		request.session['product']=product_id
		return HttpResponseRedirect('/products/')
	return render_to_response('index.html',locals(),context)
	
def products(request):
	product_id=''
	if 'product' in request.session:
		product_id=request.session['product']
	context=RequestContext(request)
	webinfo=web_info()
	classify=all_info()['navbar']
	
	print request.session['order']
	order_qty=len(set(str(request.session['order']).split(',')))
	try:
		product=Product.objects.get(pk=product_id)
	except Product.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		#request.session['order']=product_id
		if request.session['order']:
			m=str(request.session['order'])
			request.session['order']=m + ',' + str(product_id)
		else:
			request.session['order']=str(product_id)
		return HttpResponseRedirect('/order/')
	return render_to_response('product.html',locals(),context)
	
def classify(request,kinds_id):
	context=RequestContext(request)
	webinfo=web_info()
	classes=all_info()['navbar']
	
	print request.session['order']
	order_qty=len(set(str(request.session['order']).split(',')))
	try:
		classify=Classify.objects.get(pk=kinds_id)
		companylist=Company.objects.filter(classify=kinds_id)[:5]
	except Classify.DoesNotExist:
		raise Http404
	return render_to_response('classify.html',locals(),context)

def company(request,company_id):
	context=RequestContext(request)
	webinfo=web_info()
	classify=all_info()['navbar']
	
	print request.session['order']
	order_qty=len(set(str(request.session['order']).split(',')))
	try:
		company=Company.objects.get(pk=company_id)
		productlist=Product.objects.filter(company=company_id)
	except Company.DoesNotExist:
		raise Http404
	return render_to_response('company.html',locals(),context)

def product(request,product_id):
	context=RequestContext(request)
	webinfo=web_info()
	classify=all_info()['navbar']
	
	print request.session['order']
	order_qty=len(set(str(request.session['order']).split(',')))
	try:
		product=Product.objects.get(pk=product_id)
	except Product.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		if request.session['order']:
			m=str(request.session['order'])
			request.session['order']=m + ',' + str(product_id)
		else:
			request.session['order']=str(product_id)
		return HttpResponseRedirect('/order/')
	return render_to_response('product.html',locals(),context)

def order(request):
	context=RequestContext(request)
	webinfo=web_info()
	classify=all_info()['navbar']
	
	productlist=all_info()['product']
	
	if request.method == 'POST':
#		print request.POST['e_mail']
		order_id=request.POST.getlist('order_id')
		order_num=request.POST.getlist('order_num')
		order_name=request.POST.getlist('order_name')
		cnnt_name=request.POST['name']
		cnnt_email=request.POST["e_mail"]
		cnnt_require=request.POST['require']
		order_info=zip(order_id,order_num)
		a=''
		for oname,oqty in zip(order_name,order_num):
			a += oname + ' : ' + oqty
		message='this is a email to confirm your require the product & service of \n%s \n%s' % (a,cnnt_require)
		try:
			send_mail('Require Comfirme Email', message, 'tonytan748@gmail.com',[ cnnt_email,'115222956@qq.com'],fail_silently=False)
		except Exception,e:
			print str(e)
		print request.POST.getlist('order_id')
		print request.POST.getlist('order_num')
		print request.POST['name']

	if 'order' in request.session:
		order_no = str(request.session['order']).split(',')
		order_products=Product.objects.filter(pk__in=order_no)
		if order_products:
			return render_to_response('order.html',{'order_products':order_products},context)
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')
	
