from fabric.api import cd, env, local, run
from fabric.colors import red, green

import os, xmlrpclib


"""
Fabric "fab" file for deploying to WebFaction web host

Prerequisites on Webfaction box:
- pip, virtualenv, virtualenvwrapper
- creation of a virtual environment
- environment variables in ~/.bash_profile

Usage:
- `fab setup`
- `fab deploy`

Fabric env variables:
- Find info at https://my.webfaction.com
"""

# WebFaction username
env.user = os.environ['RICHARDCORNISH_WF_NAME']
# WebFaction password
env.password = os.environ['RICHARDCORNISH_WF_PASS']
# WebFaction server
env.host = 'web48.webfaction.com'
# WebFaction IP
env.ip = '75.126.137.82'

# Name of mod_wsgi "webapp" on WebFaction
env.django = 'cyndiloza_django'
# Name of project source directory inside Django "webapp"
env.project = 'cyndiloza'
# Name of static "webapp" on WebFaction
env.assets = 'cyndiloza_assets'
# Name of virtualenv (that uses virtualenvwrapper) on WebFaction
env.virtualenv = 'cyndiloza'

# Database type ('mysql', 'postgresql')
env.db_type = 'mysql'
# Database name/username
env.db_name = os.environ['RICHARDCORNISH_DB_NAME']
# Database password
env.db_pass = os.environ['RICHARDCORNISH_DB_PASS']

# SSH URL of Git repo (must be Git)
env.repo = 'git@github.com:richardcornish/cyndiloza.git'
# URL of "Website", sans http(s)://
env.website_url = 'cyndiloza.com'


"""
Do not edit the settings below unless you know what you're doing
"""

# Assemble paths for deploys

env.hosts = ['%s@%s' % (env.user, env.host)]

env.django_root  = '/home/%s/webapps/%s'    % (env.user, env.django)
env.project_root = '/home/%s/webapps/%s/%s' % (env.user, env.django, env.project)
env.assets_root  = '/home/%s/webapps/%s'    % (env.user, env.assets)


"""
Subsequent deploys
"""

def prepare_deploy():
    """
    Prepares deploy with dependencies, commits, merge, and push
    """
    # message = raw_input("Enter a Git commit message: ")
    # local('./manage.py test')
    # local('pip freeze > requirements.txt')
    # local('git add -A && git commit -m "%s"' % message)
    # local('git checkout master && git merge ' + branch_name)
    # local('git push origin master')
    pass


def activate_venv(cmd):
    run('workon %s; %s' % (env.virtualenv, cmd))


def pull_repo():
    """
    Updates Django project with newest code from Git repository
    """
    with cd(env.project_root):
        run('git pull origin master')


def install_reqs():
    """
    Installs dependencies with Pip
    """
    with cd(env.project_root):
        activate_venv('pip install -r requirements.txt')


def sync_database():
    """
    Syncs the database with new tables and possible migrations
    """
    with cd(env.project_root):
        activate_venv('./manage.py syncdb --noinput')
        activate_venv('./manage.py migrate --noinput')


def collect_static():
    """
    Copies all static files from project to static directory of assets webapp
    """
    with cd(env.project_root):
        activate_venv('./manage.py collectstatic --clear --noinput --verbosity 0')


def restart_server():
    """
    Restarts Apache web server
    """
    with cd(env.django_root):
        run('./apache2/bin/stop')
        run('./apache2/bin/start')


def check_website():
    """
    Checks that the website returns an HTTP 200 status code
    """
    print('Checking website...')
    if not '200 OK' in local('curl --silent -I "http://%s"' % env.website_url, capture=True):
        print(red('\nDude, the website is down!'))
    else:
        print(green('\nWay to go, Ace!'))


def deploy():
    """
    Deploys the update, i.e. `fab deploy`
    """
    prepare_deploy()
    pull_repo()
    install_reqs()
    sync_database()
    collect_static()
    restart_server()
    check_website()



"""
First deploy
"""

def setup_webfaction():
    """
    Sets up webapps (mod_wsgi and static), database,
    domain, and websites on WebFaction
    """

    # Creates connection to API
    server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
    session_id, account = server.login(env.user, env.password)

    # Creates Django "webapp"
    # (must manually remove Apache cron job, crontab -e)
    server.create_app(session_id, env.django, 'mod_wsgi34-python27', False, '', False)
    cmd = 'rm -r htdocs/;'
    server.system(session_id, cmd)

    # Creates static "webapp"
    server.create_app(session_id, env.assets, 'static', False, '', False)
    cmd = 'rm index.html;'
    cmd += 'mkdir static;'
    cmd += 'mkdir media;'
    server.system(session_id, cmd)

    # Creates database
    server.create_db(session_id, env.db_name, env.db_type, env.db_pass)

    # Creates domain (and subdomains)
    server.create_domain(session_id, env.website_url, 'www', 'assets')

    # Creates website entries
    server.create_website(
        session_id,
        env.django,
        env.ip,
        False,
        [env.website_url, 'www' + env.website_url],
        [env.django, '/']
    )
    server.create_website(
        session_id,
        env.assets,
        env.ip,
        False,
        ['assets' + env.website_url],
        [env.assets, '/']
    )


def setup_repo():
    """
    Downloads Django project from Git repository for the first time
    """
    with cd(env.django_root):
        run('git clone %s %s' % (env.repo, env.django_root))


def setup_database():
    """
    Syncs the database for the first time and fakes possible migrations
    """
    with cd(env.project_root):
        activate_venv('./manage.py syncdb --all')
        activate_venv('./manage.py migrate --fake --noinput')


def setup():
    """
    Deploys the installation, i.e. `fab setup`
    """
    setup_webfaction()
    setup_repo()
    install_reqs()
    setup_database()
    collect_static()
    restart_server()
    check_website()
