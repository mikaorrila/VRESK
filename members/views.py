from django.shortcuts import render
from members.models import Person, Group, Membership

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