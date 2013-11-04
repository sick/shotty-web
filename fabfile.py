from fabric.api import *
import os
import fabric.contrib.project as project

PROD = 'shotty.cc'
WSGI_DEST_PATH = '/home/shotty/public_html/shotty.cc'
DEST_PATH = '/home/shotty/public_html/shotty.cc'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
# WSGI_DEPLOY_PATH = os.path.join(ROOT_PATH, 'webapp.wsgi')
DEPLOY_PATH = os.path.join(ROOT_PATH, 'dist/')


@hosts(PROD)
def publish():
	env.user = 'shotty'
	project.rsync_project(
		remote_dir=DEST_PATH,
		# local_dir=ROOT_PATH.rstrip('/') + '/',
		local_dir=DEPLOY_PATH,
		exclude={'*.pyc', '.git/', '*.db'},
		delete=True,
	)