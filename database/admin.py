from django.contrib import admin
from .database import Participants, Issue, College, Users, Eventlist, ParticipantsAdmin

admin.site.site_header = "Registration admin"
admin.site.site_title = "Admin"
for i in [(Participants, ParticipantsAdmin), (Issue,), (College,), (Users,), (Eventlist,)]:
    admin.site.register(*i)
# Register your models here.

