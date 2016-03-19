# Application settings for profile app
# coding=utf-8

ACTIONS = (
  {
    'label'	: 'Change Profile',
    'icon'	: 'pencil',
    'grade'	: 'warning',
    'url'    	: '/profile/modify/',
  },
  {
    'label'	: 'Check Invoice',
    'icon'	: 'euro',
    'grade'	: 'info',
    'url'    	: '/profile/invoice/',
  },
)
ACTIONS_ORG = (
  {
    'label'	: 'Add User',
    'icon'	: 'plus',
    'grade'	: 'success',
    'url'	: '/profile/adduser/',
  },
)


PROFILE_TMPL_CONTENT = {
  'profile': {
    'template'          : 'overview.html',
    'actions'           : ACTIONS,
    'actions_org'	: ACTIONS + ACTIONS_ORG,
    'title'             : u'Member profile for <i>%(member)s</i>',
    'overview' : {
      'template'        : 'overview_member.html',
      'managers'       	: u'Managers',
      'firstname'       : u'Firstname',
      'name'            : u'Name',
      'login'        	: u'Login',
      'email'           : u'E-mail',
      'role'            : u'Role',
      'affil'          	: u'Affiliation',
    },
    'user_overview' : {
      'template'        : 'overview_user.html',
      'firstname'       : u'Firstname',
      'name'            : u'Name',
      'login'        	: u'Login',
      'email'           : u'E-mail',
      'role'            : u'Role',
    },
  },
  'modify': {
    'template'		: 'form.html',
    'title'     	: 'Modify Profile [{id}]',
    'desc'  	   	: 'Modify/adjust your Membership Profile',
    'submit'   		: 'Modify',
    'done' : {
      'template'        : 'done.html',
      'title'           : 'Profile [{id}] modified.',
      'message'         : '''Fields (information) modified:
{list}
''',
    },
  },
  'adduser': {
    'template'		: 'form.html',
    'title'     	: 'Add User for [{id}]',
    'submit'   		: 'Add',
    'done': {
      'template'	: 'done.html',
      'title'     	: 'User [{user}] added.',
      'no_org'		: '<p>Your membership type does only allow one(1) User.</p>',
      'max'		: '''<p>You already have the maximum of allowed Users for your Membership type.</p>
<p>If you want more Users, you'll have to get the next membership level: <a href="/profile/upgrade/">Upgrade membership</a>.</p>''',
    },
  },
  'affiluser': {
    'template'		: 'form.html',
    'title'     	: 'Affiliate {name}',
    'desc'     		: 'Procede to affiliate <i>{name}</i> to a Working Group, Ad-Hoc Group or Tool',
    'submit'   		: 'Affiliate',
    'done': {
      'template'	: 'done.html',
      'title'     	: '{name} successfully affiliated.',
      'message'     	: 'User <i>{name}</i> is now affiliated to the following groups: <b>{groups}</b>',
    },
  },
  'make_head': {
    'template'		: 'done.html',
    'title'     	: 'Changed Head of List for [{id}]',
    'message'     	: '{head} is now your new Head of List!',
  },
  'make_delegate': {
    'template'		: 'done.html',
    'title'     	: 'Changed Delegate for [{id}]',
    'message'     	: '{head} is now your new Delegate!',
  },
  'rmuser': {
    'template'		: 'form.html',
    'title'     	: 'Remove User',
    'desc'     		: 'Remove a User from the CLUSIL Membership',
    'submit'   		: 'Remove',
    'done': {
      'template'	: 'done.html',
      'title'     	: 'User removed.',
    },
  },
  'invoice': {
    'template'		: 'list.html',
    'title'     	: 'View Invoices',
    'desc'     		: 'View Invoices and payment status of the CLUSIL Membership',
    'done': {
      'template'	: 'done.html',
      'title'     	: 'Invoice.',
    },
  },
}
