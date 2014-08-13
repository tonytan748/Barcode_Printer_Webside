from django.db import models

# Create your models here.

from django.utils.encoding import smart_unicode

class WebClass(models.Model):
	name=models.CharField(max_length=120,null=False,blank=False)
	title=models.CharField(max_length=120,null=True,blank=True)
	subtitle=models.CharField(max_length=120,null=True,blank=True)
	description=models.TextField(null=True,blank=True)
	pic_1=models.URLField(null=True,blank=True)
	pic_2=models.URLField(null=True,blank=True)
	pic_3=models.URLField(null=True,blank=True)
	video_1=models.URLField(null=True,blank=True)
	video_2=models.URLField(null=True,blank=True)

	def __unicode__(self):
		return smart_unicode(self.name)

class CompanyName(models.Model):
	company_name=models.CharField(max_length=120,null=False,blank=False)
	title=models.CharField(max_length=120,null=True,blank=True)
	subtitle=models.CharField(max_length=120,null=True,blank=True)
	description=models.TextField(null=True,blank=True)
	pic_1=models.URLField(null=True,blank=True)
	pic_2=models.URLField(null=True,blank=True)
	vedio_1=models.URLField(null=True,blank=True)
	vedio_2=models.URLField(null=True,blank=True)
	def __unicode__(self):
		return smart_unicode(self.company_name)

class ProductClass(models.Model):
	class_id=models.ForeignKey('WebClass')
	company=models.ForeignKey('CompanyName')
	product_name=models.CharField(max_length=120,null=False,blank=False)
	title=models.CharField(max_length=120,null=True,blank=True)
	subtitle=models.CharField(max_length=120,null=True,blank=True)
	description=models.TextField(null=True,blank=True)
	pic_1=models.URLField(null=True,blank=True)
	pic_2=models.URLField(null=True,blank=True)
	pic_3=models.URLField(null=True,blank=True)
	pic_4=models.URLField(null=True,blank=True)
	vedio_1=models.URLField(null=True,blank=True)
	vedio_2=models.URLField(null=True,blank=True)
	vedio_3=models.URLField(null=True,blank=True)
	vedio_4=models.URLField(null=True,blank=True)
	features_title=models.CharField(max_length=120,null=True,blank=True)
	features_description=models.TextField(null=True,blank=True)
	format_title=models.CharField(max_length=120,null=True,blank=True)
	format_description=models.TextField(null=True,blank=True)

	def __unicode__(self):
		return smart_unicode(self.product_name)


