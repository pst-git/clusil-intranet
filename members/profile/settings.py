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
INV_ACTIONS = (
  {
    'label'	: 'Generate Invoice',
    'icon'	: 'euro',
    'grade'	: 'warning',
    'url'	: '/profile/invoice/new/',
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
    'title'     	: u'Modify Profile [{id}]',
    'desc'  	   	: u'Modify/adjust your Membership Profile',
    'submit'   		: u'Modify',
    'done' : {
      'template'        : 'done.html',
      'title'           : u'Profile [{id}] modified.',
      'message'         : u'''Fields (information) modified:
{list}
''',
    },
  },
  'adduser': {
    'template'		: 'form.html',
    'title'     	: u'Add User for [{id}]',
    'submit'   		: u'Add',
    'done': {
      'template'	: 'done.html',
      'title'     	: u'User [{user}] added.',
      'no_org'		: u'<p>Your membership type does only allow one(1) User.</p>',
      'max'		: u'''<p>You already have the maximum of allowed Users for your Membership type.</p>
<p>If you want more Users, you'll have to get the next membership level: <a href="/profile/upgrade/">Upgrade membership</a>.</p>''',
    },
  },
  'affiluser': {
    'template'		: 'form.html',
    'title'     	: u'Affiliate {name}',
    'desc'     		: u'Procede to affiliate <i>{name}</i> to a Working Group, Ad-Hoc Group or Tool',
    'submit'   		: 'Affiliate',
    'done': {
      'template'	: 'done.html',
      'title'     	: u'{name} successfully affiliated.',
      'message'     	: u'User <i>{name}</i> is now affiliated to the following groups: <b>{groups}</b>',
    },
  },
  'make_head': {
    'template'		: 'done.html',
    'title'     	: u'Changed Head of List for [{id}]',
    'message'     	: u'{head} is now your new Head of List!',
  },
  'make_delegate': {
    'template'		: 'done.html',
    'title'     	: u'Changed Delegate for [{id}]',
    'message'     	: u'{head} is now your new Delegate!',
  },
  'rmuser': {
    'template'		: 'form.html',
    'title'     	: u'Remove User',
    'desc'     		: u'Remove a User from the CLUSIL Membership',
    'submit'   		: u'Remove',
    'done': {
      'template'	: 'done.html',
      'title'     	: u'User removed.',
    },
  },
  'invoice': {
    'template'		: 'list.html',
    'title'     	: u'Invoices',
    'desc'     		: u'View Invoices and payment status of the CLUSIL Membership',
    'actions'  		: INV_ACTIONS,
    'done': {
      'template'	: 'done.html',
      'title'     	: u'View Invoice.',
    },
  },
  'newinv': {
    'template'		: 'form.html',
    'title'     	: u'Generate a new Invoice',
    'desc'     		: u'This CLUSIL membershipfee invoice replaces and cancels all previous ones for the same year',
    'submit'   		: u'Generate',
    'done': {
      'template'	: 'done.html',
      'title'     	: u'View Invoice.',
    },
  },
}
