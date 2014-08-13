from django.conf.urls import patterns,url

from codeprinter import views

urlpatterns=patterns('',
		url(r'^$',views.index,name='index'),
		url(r'^class/(?P<kinds_id>\d+)/$',views.classify,name='classify'),
		url(r'^company/(?P<company_id>\d+)/$',views.company,name='company'),
		url(r'^product/(?P<product_id>\d+)/$',views.product,name='product'),
		url(r'^products/$',views.products,name='products'),
		url(r'^order/$',views.order,name='order'),
		)
