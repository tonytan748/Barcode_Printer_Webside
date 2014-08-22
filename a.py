		if request.POST.has_key('require'):
#			print request.POST['e_mail']
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


		if request.POST.get('delall') :
			print "adsfadadfsfsd"
			try:
				del request.session['order']
			except KeyError:
				pass
			#print request.session['order']
			print "response"
			return render_to_response('/order/',locals())
		else:
			pass
		
		
		
	$('#delthis').click(function(){
		var delid;
		delid = $(this).attr("del-id");
		$.get('/delete_require_item/', {delete_id: delid},function(){
			
		});
	});
