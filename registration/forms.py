# coding=utf-8

from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, ChoiceField, ModelForm, CharField, ModelMultipleChoiceField, CheckboxSelectMultiple, TextInput, FileField, EmailField, BooleanField, RadioSelect
from django.forms.models import modelformset_factory, BaseModelFormSet

from accounting.models import Fee
from members.models import Member, Address


class ErrorForm(Form):
  error 	= BooleanField(label='Input error! Try again?',required=False)


class MemberTypeForm(Form):
  member_type = ChoiceField(label='Membership type',choices=Member.MEMBER_TYPES)
#  captcha = ReCaptchaField(attrs={'theme' : 'clean'}) #doesn't work -> do via email confirmation (!)

class AddressForm(ModelForm):
  organisation 	= CharField(required=False)
  first_name 	= CharField(required=False)
  last_name 	= CharField(required=False)
  email 	= EmailField(required=False)

  class Meta:
    model = Address
    fields = ( 'first_name', 'last_name', 'email', 'organisation', 'street', 'postal_code', 'town', 'country', 'c_other', )
    labels = {
      'c_other'	: 'Other country',
    }
    help_text = {
      'c_other'	: 'If none from above please specify here',
    }

ORG_NB_USERS = (
  (5, '6 - 400EUR'),
  (11, '12 - 700EUR'),
  (17, '18 - 1000EUR'),
)
class RegisterUserForm(UserCreationForm):
  delegate 	= BooleanField(label='add Delegate?',help_text='The delegate is the head-of-list\'s alternate for all it\'s roles: point of contact and membership management.',required=False)
  more 		= ChoiceField(label='Nb of Users?',choices=ORG_NB_USERS,initial=5,help_text='Set the number of Users for your membership. Want more Users in your membership? Contact us for mass membership: <a href="mailto:membership@clusil.lu?Subject=Mass Membership">membership@clusil.lu</a>.',widget=RadioSelect(),required=False)

  class Meta:
    model = User
    fields = ( 'first_name', 'last_name', 'email', 'username', 'password1', 'password2', )
    widgets = {
      'email'		: TextInput(attrs={'type': 'email', }),
      'password1'	: TextInput(attrs={'type': 'password', }),
      'password2'	: TextInput(attrs={'type': 'password', }),
    }

#multiuser formset
class UserForm(ModelForm):

  class Meta:
    model = User
    fields = ( 'first_name', 'last_name', 'email', )

#this is needed to set the queryset to none by default
class BaseUserFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseUserFormSet, self).__init__(*args, **kwargs)
        self.queryset = User.objects.none()

MultiUserFormSet = modelformset_factory(User, form=UserForm, formset=BaseUserFormSet, extra=5)


class StudentProofForm(ModelForm):
  student_proof = FileField(required=True)

  class Meta:
    model = Member
    fields = ( 'student_proof', )

