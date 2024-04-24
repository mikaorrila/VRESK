from django.contrib import admin
from members.models import Person, Group, Membership

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'rank', 'current_group', 'joined', 'active')
    search_fields = ['firstname', 'lastname']
    def current_group(self, obj):
        return ", ".join([group.name for group in obj.group_set.all()])

class MembershipInline(admin.TabularInline):
    model = Membership
    
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'member_count')
    search_fields = ['name']
    inlines = [
        MembershipInline,
    ]

    def member_count(self, obj):
        return obj.members.count()

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('person', 'group', 'date_joined', 'invite_reason')

admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)