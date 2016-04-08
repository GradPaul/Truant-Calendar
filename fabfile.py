from fabric.api import cd,run,env,hosts,roles,execute,settings,local
import os






def save():
	local("git add -A")
	with settings(warn_only=True):
		local("git commit -m 'save' ")
		local("git push")

