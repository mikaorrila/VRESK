from django.shortcuts import render
from members.models import Person, Group, Membership
from django.db.models import Count

def members_page(request):
    # Fetch data
    personnel = Person.objects.all()
    groups = Group.objects.all()
    memberships = Membership.objects.all()

    # Pass data to the template
    context = {
        'personnel': personnel,
        'groups': groups,
        'memberships': memberships,
    }

    # Render the template
    return render(request, 'members/members.html', context)
    
def members_groups(request):
    groups = Group.objects.annotate(member_count=Count('members'))
    context = {
        'groups': groups,
    }
    return render(request, 'members/groups.html', context)

def members_military(request):
    memberships = Membership.objects.all()
    context = {        
        'memberships': memberships,
    }
    return render(request, 'members/military.html', context)

def members_person(request):
    personnel = Person.objects.all()
    context = {
        'personnel': personnel,
    }
    return render(request, 'members/person.html', context)