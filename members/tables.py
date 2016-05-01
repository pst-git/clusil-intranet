#coding=utf-8

from datetime import date

from django_tables2.tables import Table
from django_tables2 import Column

from django.utils.safestring import mark_safe
from django.utils.html import escape

#from smash.tables import format_number, format_datetime

from .models import Member, Role

#table for visualisation via django_tables2
class MemberTable(Table):
  row_class     = Column(visible=False, empty_values=()) #used to highlight some rows
  details	= Column(verbose_name='Details',empty_values=())
  modify	= Column(verbose_name='Modify',empty_values=())

  def render_row_class(self, value, record):
    if record.status == Member.STB:
      return 'warning'

    if record.status == Member.WBE:
      return 'info'

    if record.status == Member.ACT:
      return 'success'

    if record.end_date:
      return 'danger'

  def render_details(self, record):
    link = '<center><a class="btn btn-info btn-sm" href="/members/list/{}/"><span class="glyphicon glyphicon-list"></span></a></center>'.format(escape(record.id))
    return mark_safe(link)

  def render_modify(self, record):
    link = '<center><a class="btn btn-danger btn-sm" href="/members/modify/{}/"><span class="glyphicon glyphicon-pencil"></span></a></center>'.format(escape(record.id))
    return mark_safe(link)


#  def render_start_date(self, value):
#    return format_datetime(value)

#  def render_end_date(self, value):
#    return format_datetime(value)

  class Meta:
    model = Member
    fields = ( 'id', 'type', 'head_of_list', 'delegate', 'status', )
    attrs = {"class": "table"}


