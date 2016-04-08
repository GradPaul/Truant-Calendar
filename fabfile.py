from fabric.api import cd,run,env,hosts,roles,execute,settings,local
import os






grad=['grad',]
env.user="root"


def save():
	local("git add -A")
	with settings(warn_only=True):
		local("git commit -m 'save' ")
		local("git push")


@roles('grad')		
def update():
	with cd('/date/src/Truant-Calendar'):
 		run ("git reset --hard HEAD^")
 		run("git pull")