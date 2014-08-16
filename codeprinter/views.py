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
	
	if request.session.has_key('order') and str(request.session['order']) != '':
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
	
	if request.session.has_key('order') and str(request.session['order']) != '':
		order_qty=len(set(str(request.session['order']).split(',')))

	try:
		product=Product.objects.get(pk=product_id)
	except Product.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		#request.session['order']=product_id
		if request.session.has_key('order') and str(request.session['order']) != '':
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
	
	if request.session.has_key('order') and str(request.session['order']) != '':
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
	
	if request.session.has_key('order') and str(request.session['order']) != '':
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
	
	if request.session.has_key('order') and str(request.session['order']) != '':
		order_qty=len(set(str(request.session['order']).split(',')))
		
	try:
		product=Product.objects.get(pk=product_id)
	except Product.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		if request.session.has_key('order') and str(request.session['order']) != '':
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
	
	if 'order' in request.session and str(request.session['order']) == '':
		del request.session['order']

	if request.method == 'POST':
		if "delall" in request.POST:
			try:
				del request.session['order']
			except KeyError,e:
				print str(e)
			return HttpResponseRedirect('/order/')
		elif "require_info" in request.POST:
			if 'order' in request.session:
				del request.session['order']
			request.session['order']=(','.join(request.POST.getlist('order_id'))).decode()
			print request.session['order']
#			subject='Thank you send the require.'
#			messages='thank you for your interesting about our product and service. we will content with you as soon as possible.'
#			from_email='tonytan748@gmail.com'
#			recipient_list=[request.POST.get('e_mail')]
			
#			send_mail(subject, messages, from_email, recipient_list, fail_silently=False)
			
			print "dsfsfasdsfasdf   require_info"
		else:
			pass
	
	if 'order' in request.session and str(request.session['order']) != '':
		order_no = str(request.session['order']).split(',')
		order_products=Product.objects.filter(pk__in=order_no)
		if order_products:
			return render_to_response('order.html',{'order_products':order_products},context)
		else:
			return HttpResponseRedirect('/')
	elif str(request.session['order']) == '':
		del request.session['order']
		return render_to_response('order.html',{'order_products':''},context)
	else:
		return render_to_response('order.html',{'order_products':''},context)

	