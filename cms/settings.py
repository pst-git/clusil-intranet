# coding=utf-8
"""
Django settings for cms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '"&_-L%/(OI&RB�tzdb*v6hv+b8@rav4fgh@zre64z$54wrefdB%&*/çZR(r!)0b71c1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ 'cms.clusil.lu', 'intranet.clusil.lu', ]

# Application definition

INSTALLED_APPS = (
# global bootstrap4 integration
#  'bootstrap3',
  'bootstrap4',
  'bootstrap4_datetime',
# django core apps
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.sites',
  'django.contrib.flatpages', #needed by breadcrumbs
# specific supporting apps
  'formtools',
  'django_tables2',
  'breadcrumbs',
  'captcha',
#  'password_reset',
  'import_export',
# my apps
  'cms.apps.CmsConfig',
  'registration.apps.RegistrationConfig',
  'members.apps.MembersConfig',
  'members.groups.apps.GroupsConfig',
  'meetings.apps.MeetingsConfig',
  'attendance.apps.AttendanceConfig',
  'events.apps.EventsConfig',
  'accounting.apps.AccountingConfig',
  'upload.apps.UploadConfig',
  'ideabox.apps.IdeaboxConfig',
)

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
#    'django_auth_ldap.backend.LDAPBackend', #won't be needed anymore probably
    'django.contrib.auth.backends.ModelBackend',
)
#LDAP config
#won't be needed anymore probably
#AUTH_LDAP_SERVER_URI = 'ldap://localhost'
#AUTH_LDAP_BIND_DN = "cn=admin,dc=clusil,dc=lu"
#AUTH_LDAP_BIND_PASSWORD = "DklIBGzcKA4i"
#
#AUTH_LDAP_USER_DN_TEMPLATE = "cn=%(user)s,ou=users,dc=clusil,dc=lu"
#AUTH_LDAP_REQUIRE_GROUP = "cn=cms,ou=groups,dc=clusil,dc=lu"
#AUTH_LDAP_USER_ATTR_MAP = {
#	"first_name": "givenName", 
#	"last_name": "sn", 
#	"email": "mail"
#}


MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
# via supporting apps
  'breadcrumbs.middleware.BreadcrumbsMiddleware',
)

ROOT_URLCONF = 'cms.urls'

WSGI_APPLICATION = 'cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'cms/db.sqlite'),
  },
# 'ldap': {
#   'ENGINE': 'ldapdb.backends.ldap',
#   'NAME': 'ldap://localhost/',
#   'USER': 'cn=admin,dc=clusil,dc=lu',
#   'PASSWORD': 'DklIBGzcKA4i',
#  }
}
#DATABASE_ROUTERS = ['ldapdb.router.Router']

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures/'),
)
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'
LC_ALL = 'en_GB.utf8' #to be used inpython afterwards

TIME_ZONE = 'Europe/Luxembourg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'cms/static/'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
FILE_UPLOAD_HANDLERS = ( #default
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)

# LOCAL settings

#where to store and get user-uploaded files
WEBROOT = '/var/www/clusil.lu/cms/'
MEDIA_ROOT = os.path.join(WEBROOT,'media/')
MEDIA_URL = '/media/'

#login/auth (used by the login_required decorator)
LOGIN_URL="/login/"
LOGIN_REDIRECT_URL="/home/"

#where to find templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
	'DIRS': [
		os.path.join(BASE_DIR, 'templates/'),
  		os.path.join(BASE_DIR, 'templates/email/'),
  		os.path.join(BASE_DIR, 'templates/documentation/'),
		],
	'OPTIONS': {
	  'context_processors': [
		'django.template.context_processors.debug',
                'django.template.context_processors.request', #tables2 needs this
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'cms.context_processors.template_content', #for own templating system
                'cms.context_processors.group_perms', #for perms model using groups
                'cms.context_processors.user_context', #for perms model using groups
	  	],
	  },
    },
]

#ReCAPTCHA stuff (not used anymore, keeping 'in case of')
RECAPTCHA_USE_SSL = True
#NOCAPTCHA = True
RECAPTCHA_PUBLIC_KEY = "6Lc7twwTAAAAANJUI4eaSt2cBq0gm7U9QTcyXlLM"
RECAPTCHA_PRIVATE_KEY = "6Lc7twwTAAAAAD5Gh03S-3FTE3eza8n9QD3WWQSf"

# email config

#mailgun stuff
#EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = '81ac7d85d5de3e94cdd02fc1e1cce098'
MAILGUN_SERVER_NAME = 'mail.clusil.lu'

SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'CLUSIL Admin <admin@clusil.lu>'

ADMINS = (
  ('Pascal Steichen', 'pst@clusil.lu'),
)

EMAILS = {
  'email' : {
    'board'	: 'CLUSIL Board <board@clusil.lu>',
    'secgen'	: 'Secretariat <secgen@clusil.lu>',
    'no-reply'	: 'CLUSIL (no-reply) <no-reply@clusil.lu>',
  },
  'salutation' 	: '''
Best Regards,
Your CLUSIL team
''',
  'disclaimer' 	: '''
''',
}



## global content for templates and views
TEMPLATE_CONTENT = {
  #basic/generic content for all templates/views:
  'meta' : {
    'author'            : 'Pascal Steichen - pst@clusil.lu ; 2012, 2014, 2015, 2018',
    'copyright'         : 'CLUSIL a.s.b.l. - info@clusil.lu ; 2012, 2014, 2015, 2018',
    'title'             : 'CLUSIL Club Management System',
    'logo' : {
      'url'		: "/",
      'img'		: STATIC_URL + 'pics/logo.png',
      'thumb'		: STATIC_URL + 'pics/thumb.png',
    },
    'description'       : '',
    'keywords'          : '',
    'css' : {
#        'bt'            : '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
        'bt'            : '//stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css',
#        'bt_theme'      : '//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css',
        'bt_theme'      : '//stackpath.bootstrapcdn.com/bootswatch/4.1.1/lux/bootstrap.min.css',
        'jumbotron'	: '//clusil.lu/css/jumbotron.css',
        'jt_narrow'	: '//clusil.lu/css/jumbotron-narrow.css',
        'own'           : STATIC_URL + 'css/bt-clusil.css',
        'dtpicker'      : '//cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.7.14/css/bootstrap-datetimepicker.min.css',
    },
    'js' : {
#        'jq'            : '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js',
#        'bt'            : '//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js',
	'jq'            : '//code.jquery.com/jquery-3.3.1.slim.min.js',
	'popper'        : '//cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js',
        'bt'            : '//stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js',
        'bt_bundle'     : '//stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.bundle.min.js',
        'fontawesome'   : '//use.fontawesome.com/42b7f0ba56.js',
#        'momentjs'      : '//cdnjs.cloudflare.com/ajax/libs/moment.js/2.10.3/moment-with-locales.min.js',
#        'dtpicker'      : '//cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.7.14/js/bootstrap-datetimepicker.min.js',
    },
  },
  'error' : {
    'gen'               : 'Error in input validation!',
    'email'             : 'Error in email notification!',
    'no-data'           : 'No data!',
    'duplicate'         : 'Duplicate found, reconsider your input!',
  },
  'auth' : {
    'title'	: 'Member Sign In',
    'submit'	: 'Login',
    'reg' : {
      'title'	: 'Sign Up',
      'content'	: '[will be overwritten below]',
    },
  },
  'pwd' : {
    'recover' : {
      'title': 'Password Recovery',
      'submit': 'Recover',
      'done' : {
        'title': 'Password Recovery completed successfully',
        'message': 'Your password has been changed successfully. Please re-login with your new credentials.',
      },
    },
    'change' : {
      'title': 'Change password for User: ',
      'submit': 'Change',
      'done' : {
        'title': 'Password Change completed successfully',
        'message': 'Your password has been changed successfully. Please re-login with your new credentials.',
        'backurl': '/',
        'backurl_txt': 'Back to main page.',
      },
    },
  },
}

## registration
REG_ACTIONS = (
  {
    'label'	: 'Individual',
    'price'	: '1 user: 100',
    'icon'    	: 'user',
    'grade'    	: 'info',
    'url'     	: '/reg/individual/',
  },
  {
    'label'	: 'Organisation',
    'price'	: 'per group of 6 users: 400',
    'icon'    	: 'building',
    'grade'    	: 'success',
    'url'     	: '/reg/organisation/',
  },
  {
    'label'	: 'Student',
    'price'	: '1 user: 25',
    'icon'    	: 'student',
    'grade'    	: 'warning',
    'url'     	: '/reg/student/',
  },
)

TEMPLATE_CONTENT['auth']['reg']['content'] = {
  'template'	: 'action-list.html',
  'title'	: 'Sign Up as <i>CLUSIL member</i>',
  'desc'  	: 'CLUSIL memberships come in 3 flavours:', 
  'actions'	: REG_ACTIONS,
}

from registration.settings import *

MEMBER_ID_SALT     = u']*8/bi83}7te!TJZ(IL!K?&+U'
REG_VAL_URL 	= u'https://' + ALLOWED_HOSTS[0] + '/reg/validate/'
REG_SALT	= u'CLUSIL 1996-2016, 20 years of CHEEBANG!'

TEMPLATE_CONTENT['reg'] = REGISTRATION_TMPL_CONTENT


## home
HOME_ACTIONS = (
  {
    'heading'		: 'Membership Management',
    'actions' : (
      {         
        'label'         : 'Profile', 
        'icon'     	: 'home',
        'grade'     	: 'primary',
        'desc'          : 'Manage your Membership profile',
        'url'           : '/profile/',
      },
    ),
  },
  {
    'heading'		: 'Suggestion Box',
    'desc'         	: 'An idea? A remark? A suggestion?',
    'actions' : (
      {         
        'label'        	: 'Submit your thought', 
        'icon' 		: 'commenting-o',
        'grade'  	: 'primary',
    	'desc'         	: 'Please share with us your thoughts about CLUSIL!',
        'url'          	: '/ideabox/',
      },
#      {         
#        'label'        : 'Document Management', 
#        'icon'  	: 'folder-open',
#        'grade'  	: 'info',
#        'desc'         : 'Filesharing and document management platform (SeaFile based)',
#        'url'          : 'https://cloud.clusil.lu/',
#    	'has_perms'	: 'cms.MEMBER',
#      },
#      {         
#        'label'        : 'Team Collaboration', 
#        'icon'     	: 'comment',
#        'grade'  	: 'info',
#        'desc'         : 'Wiki, Workflows and Calendar platform (Confluence based)',
#        'url'          : 'https://collab.clusil.lu/',
#    	'has_perms'	: 'cms.MEMBER',
#      },
#
    ),
  },
  {
    'heading'   	: 'Management Console (BOARD)',
    'perms'		: 'Board',
    'cols'		: '12',
    'actions' : (
      {         
        'label'         : 'Dashboard', 
        'icon'     	: 'tasks',
        'grade'  	: 'info',
        'desc'          : 'Club management tools and functions',
        'url'           : '/board/',
        'perms'		: 'Board',
      },
    ),
  },
)

TEMPLATE_CONTENT['home'] = {
  'title'     	: 'What do you want to do today ?',
  'template'    : 'actions.html',
  'actions'     : HOME_ACTIONS,
}

## documentation
TEMPLATE_CONTENT['documentation'] = {
  'title'     	: 'CLUSIL Intranet Documentation',
  'desc'     	: 'Use the categories/tabs herebelow to view the documentation on how to best use the CLUSIL Intranet:',
  'template'    : 'main.html',
  'docs' : (
    {
      'ref'	: 'reg',
      'title'	: 'HowTo register and use the membership platform',
      'content'	: 'reg.html',
    },
    {
      'ref'	: 'cloud',
      'title'	: 'HowTo use the (SeaFile) cloud-system for document sharing',
      'content'	: 'cloud.html',
    },
  ),
}

## upload
from upload.settings import *
TEMPLATE_CONTENT['upload'] = UPLOAD_TMPL_CONTENT


## board
BOARD_ACTIONS = (
  {
    'heading'      	: 'Meetings, Events and Communication',
    'has_perms'		: 'cms.SECR',
    'cols'		: '6',
    'actions' : (
      {         
        'label'         : 'Meetings and <i>members-only</i> Events', 
        'icon'     	: 'calendar',
        'grade'     	: 'info',
        'desc'          : 'Manage regular meetings (board, working groups...) or members-only events.',
        'url'           : '/meetings/',
	'has_perms'	: 'cms.SECR',
      },
      {         
        'label'         : 'Public Events', 
        'icon'     	: 'glass',
        'grade'     	: 'warning',
        'desc'          : 'Manage public events or activities',
        'url'           : '/events/',
	'has_perms'	: 'cms.SECR',
      },
      {         
        'label'         : 'Web Content', 
        'icon'     	: 'cloud',
        'grade'     	: 'danger',
        'desc'          : 'Manage the public website content',
        'url'           : '/webcontent/',
	'has_perms'	: 'cms.SECR',
      },
    ),
  },
  {
    'heading'      	: 'Club Management',
    'has_perms'		: 'cms.SECR',
    'cols'		: '6',
    'actions' : (
      {         
        'label'         : 'Members', 
        'icon'     	: 'user',
        'grade'     	: 'info',
        'desc'          : 'Manage members.',
        'url'           : '/members/',
	'has_perms'	: 'cms.SECR',
      },
      {         
        'label'         : 'Organisation', 
        'icon'     	: 'users',
        'grade'     	: 'info',
        'desc'          : 'Manage and affiliate members to groups.',
        'url'           : '/members/groups/',
	'has_perms'	: 'cms.BOARD',
      },
      {         
        'label'         : 'Treasury', 
        'icon'     	: 'euro',
        'grade'     	: 'info',
        'desc'          : 'Manage and check payments or other financial figures.',
        'url'           : '/accounting/',
	'has_perms'	: 'cms.BOARD',
      },
    ),
  },
)

TEMPLATE_CONTENT['board'] = {
  'title'      	: 'Management Dashboard',
#  'template'    : 'dashboard.html',
  'template'    : 'actions.html',
  'actions'     : BOARD_ACTIONS,
}


## members
from members.settings import *
TEMPLATE_CONTENT['members'] = MEMBERS_TMPL_CONTENT
RENEW_URL 	= u'https://' + ALLOWED_HOSTS[0] + '/profile/renew/'
RENEW_SALT	= u'CLUSIL 1996-2016, 20 years of CHEEBANG!'

## groups
from members.groups.settings import *

TEMPLATE_CONTENT['groups'] = GROUPS_TMPL_CONTENT

## profile
from members.profile.settings import *

TEMPLATE_CONTENT['profile'] = PROFILE_TMPL_CONTENT

## ideabox
from ideabox.settings import *

TEMPLATE_CONTENT['ideabox'] = IDEABOX_TMPL_CONTENT


## attendance
from attendance.settings import *
TEMPLATE_CONTENT['attendance'] = ATTENDANCE_TMPL_CONTENT
ATTENDANCE_BASE_URL = 'https://' + ALLOWED_HOSTS[0] + '/attendance/'

## meetings
from meetings.settings import *
TEMPLATE_CONTENT['meetings'] = MEETINGS_TMPL_CONTENT
MEETINGS_ATTENDANCE_URL = ATTENDANCE_BASE_URL + 'meetings/'


## events
from events.settings import *
TEMPLATE_CONTENT['events'] = EVENTS_TMPL_CONTENT
EVENTS_REG_BASE_URL = 'https://' + ALLOWED_HOSTS[0] + '/events/reg/'


## accounting
from accounting.settings import *
TEMPLATE_CONTENT['accounting'] = ACCOUNTING_TMPL_CONTENT

#from members.models import Member
#FEE = {
#  Member.IND	: 100,
#  Member.STD 	: 25,
#  Member.ORG_6	: 400,
#  Member.ORG_12	: 700,
#  Member.ORG_18 : 1000,
#}

ACCOUNTING = {
  'invoice' : {
    'logo'		: STATIC_ROOT + 'pics/logo.png',
    'currency' 		: 'EUR',
    'subject' 		: 'Invoice for membership: %s',
    'mail_template' 	: 'invoice.txt',
  },
  'credit' : {
    'logo'		: STATIC_ROOT + 'pics/logo.png',
    'currency' 		: 'EUR',
    'subject' 		: 'Credit note for: %s',
    'mail_template' 	: 'credit.txt',
  }
}

#add local settings
from local_settings import *
