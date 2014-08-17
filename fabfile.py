from fabric.api import local

def deploy():
	local('git add .')
	comment=raw_input('please key in some words:')
	local('git commit -m "%s"' % comment)
	local('git push origin master')

#fab deploy
