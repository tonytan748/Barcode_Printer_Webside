from django.db import models

from django.utils.encoding import smart_unicode
#-- ---
#-- Table 'website'
#-- 
#-- ---

class WebInfo(models.Model):
	name = models.CharField(max_length=50,null=False,blank=False)
	url = models.URLField(max_length=255,null=False,blank=False)
	author = models.CharField(max_length=120,null=True,blank=True)
	title = models.CharField(max_length=120,null=True,blank=True)
	subtitle = models.CharField(max_length=120,null=True,blank=True)
	introduction = models.TextField(null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	pic_1=models.CharField(max_length=250,null=True,blank=True)
	pic_2=models.CharField(max_length=250,null=True,blank=True)
	pic_3=models.CharField(max_length=250,null=True,blank=True)
	vedio_1 = models.CharField(max_length=250,null=True,blank=True)
	vedio_2 = models.CharField(max_length=250,null=True,blank=True)
	vedio_3 = models.CharField(max_length=250,null=True,blank=True)
	content_address = models.TextField(null=True,blank=True)
	content_phone = models.CharField(max_length=20,null=True,blank=True)
	content_handphone = models.CharField(max_length=20,null=True,blank=True)
	content_email = models.EmailField(null=True,blank=True)
	content_name = models.CharField(max_length=20,null=True,blank=True)
	content_name_position = models.CharField(max_length=50,null=True,blank=True)

	def __unicode__(self):
		return smart_unicode(self.name)
#-- ---
#-- Table 'web_content'
#-- 
#-- ---

class Classify(models.Model):
	name = models.CharField(max_length=50,null=False,blank=False)
	title = models.CharField(max_length=120,null=True,blank=True)
	subtitle = models.CharField(max_length=120,null=True,blank=True)
	introduction = models.TextField(null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	pic_1 = models.CharField(max_length=250,null=True,blank=True)
	pic_2 = models.CharField(max_length=250,null=True,blank=True)
	pic_3 = models.CharField(max_length=250,null=True,blank=True)
	vedio_1 = models.CharField(max_length=250,null=True,blank=True)
	vedio_2 = models.CharField(max_length=250,null=True,blank=True)
	vedio_3 = models.CharField(max_length=250,null=True,blank=True)

	def __unicode__(self):
		return smart_unicode(self.name)
#-- ---
#-- Table 'company'
#-- 
#-- ---


class Company(models.Model):
	name = models.CharField(max_length=50,null=False,blank=False)
	classify=models.ForeignKey('Classify')
	title = models.CharField(max_length=120,null=True,blank=True)
	subtitle = models.CharField(max_length=120,null=True,blank=True)
	introduction = models.TextField(null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	pic_1 = models.CharField(max_length=250,null=True,blank=True)
	pic_2 = models.CharField(max_length=250,null=True,blank=True)
	pic_3 = models.CharField(max_length=250,null=True,blank=True)
	vedio_1 = models.CharField(max_length=250,null=True,blank=True)
	vedio_2 = models.CharField(max_length=250,null=True,blank=True)
	vedio_3 = models.CharField(max_length=250,null=True,blank=True)

	def __unicode__(self):
		return smart_unicode(self.name)

#-- ---
#-- Table 'product'
#-- 
#-- ---

class Product(models.Model):
	name = models.CharField(max_length=50,null=False,blank=False)
	model = models.CharField(max_length=120,null=False,blank=False)
	company = models.ForeignKey('Company')
	classify = models.ForeignKey('Classify')
	title= models.CharField(max_length=120,null=True,blank=True)
	subtitle= models.CharField(max_length=120,null=True,blank=True)
	introduction = models.TextField(null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	pic_1 = models.CharField(max_length=250,null=True,blank=True)
	pic_2 = models.CharField(max_length=250,null=True,blank=True)
	pic_3 = models.CharField(max_length=250,null=True,blank=True)
	vedio_1 = models.CharField(max_length=250,null=True,blank=True)
	vedio_2 = models.CharField(max_length=250,null=True,blank=True)
	vedio_3 = models.CharField(max_length=250,null=True,blank=True)
	features = models.TextField(null=True,blank=True)
	specifications = models.TextField(null=True,blank=True)

	def __unicode__(self):
		return smart_unicode(self.name)
