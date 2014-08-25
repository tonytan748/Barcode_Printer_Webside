from fabric.api import local

def update():
	local('git add .')
	comment=raw_input('Please key in some commend:')
	local('git commit -m "%s"' % comment)
	local('git push origin master')


