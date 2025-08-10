from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import Group
from home.models import RoleOverride

@receiver(user_logged_in)
def assign_group_on_login(sender, request, user, **kwargs):
    try:
        role = RoleOverride.objects.get(email=user.email)
        group, _ = Group.objects.get_or_create(name=role.group_name)
        user.groups.add(group)
        print(f"✅ {user.email} assigned to group: {group.name}")
    except RoleOverride.DoesNotExist:
        print(f"⚠️ No role mapping found for {user.email}")









