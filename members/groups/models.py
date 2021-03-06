from django.db.models import Model, IntegerField, CharField, ForeignKey, EmailField
from django.contrib.auth.models import User

from members.functions import gen_fulluser

# Group (board, working group, etc.) model
class Group(Model):
  MG = 0
  WG = 1
  AG = 2
  SG = 3
  TL = 4
  TYPES = (
    (MG, 'Management Group'), #only for specific members
    (WG, 'Working Group'),
    (AG, 'Ad-Hoc Group'),
    (SG, 'Special Group'),  # for all group for instance
    (TL, 'Tool'),
  )

  CMS    = 0
  CLOUD  = 1
  COLLAB = 2
  TOOLS = (
    (CMS    , 'cms'),
    (CLOUD  , 'cloud'),
    (COLLAB , 'collab'),
  )

  ACT = 0
  SPL = 1
  STB = 2
  OLD = 3
  STATUSES = (
    (ACT, 'active'),
    (STB, 'standby'), #inactive
    (OLD, 'archived'), #not used any more
  )

  acronym 	= CharField(max_length=15)
  title 	= CharField(max_length=150)
  desc 		= CharField(max_length=500,blank=True,null=True)
  email 	= EmailField(blank=True,null=True)
  type 		= IntegerField(choices=TYPES)
  status      	= IntegerField(choices=STATUSES,default=ACT) 

  def __unicode__(self):
    return self.title


# Affiliation (user to group) model
class Affiliation(Model):
  user 		= ForeignKey(User)
  group 	= ForeignKey(Group)

  def __unicode__(self):
    g=u' - '
    try:
      g += unicode(self.group)
    except: pass
    return gen_fulluser(self.user) + g

  class Meta:
    unique_together = ( 'user', 'group', )


