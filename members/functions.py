

def get_members_to_validate():
  from .models import Member
  return Member.objects.filter(status=Member.REG)

def get_active_members():
  from .models import Member
  return Member.objects.filter(status=Member.ACT)

def gen_fullname(user):
  return unicode(user.first_name) + u' ' + unicode.upper(user.last_name) + u' (' + unicode(user.email) + u')'

def create_ldap_user(user):
  from cms.models import LdapUser

  lu = LdapUser(username=user.username)
  lu.first_name = u.first_name
  lu.last_name 	= u.last_name
  lu.email	= u.email
  lu.password 	= u.password
  lu.save()
  return lu

def add_to_ldap_group(ldap_user,ldap_group_name):
  from cms.models import LdapGroup

  group = LdapGroup.objects.get(name=ldap_group_name)
  group.members.add(ldap_user)
  group.save()

def replicate_to_ldap(member):

  #create and add hol and delegate to 'cms' group
  add_to_ldap_group(create_ldap_user(member.head_of_list),'cms')
  add_to_ldap_group(create_ldap_user(member.delagate),'cms')

  for u in member.users.all:
    create_ldap_user(u)

def gen_member_initial(m):
  initial_data = {}

  initial_data['first_name'] = m.first_name
  initial_data['last_name'] = m.last_name
  initial_data['email'] = m.email
  initial_data['start_date'] = m.start_date
  initial_data['end_date'] = m.end_date
  initial_data['status'] = m.status

  return initial_data

def gen_role_initial(r):
  initial_data = {}

  initial_data['title'] = r.title
  initial_data['desc'] = r.desc
  initial_data['member'] = r.member
  initial_data['start_date'] = r.start_date
  initial_data['end_date'] = r.end_date

  return initial_data

def gen_member_id():
  from .models import Member
  num = 0
  #member-id model CLUSIL-YYYY-NNNN
  try:
    ml = str(Member.objects.filter(member_id__contains=date.today().strftime('%Y')).latest('member_id'))
    id = ml.split('-')[2].split(' ')[0]
    num = int(id) + 1
  except Member.DoesNotExist:
    num = 1

  mid = 'CLUSIL-%(year)s-%(num)04d' % { 'year': date.today().strftime('%Y'), 'num': num }
  return mid

def add_group(u,g):
  from groups.models import Group, Affiliation
  group = Affiliation(user=u,group=g)
  group.save()
  default = Affiliation(user=u,group=Group(pk='default'))
  default.save()
