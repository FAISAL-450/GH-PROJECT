from django.conf import settings
from django.contrib.auth.models import Group
from django_auth_adfs.signals import post_authenticate

def sync_groups(sender, user, claims, **kwargs):
    group_ids = claims.get("groups", [])
    role_map = settings.AZURE_AUTH.get("ROLES", {})
    assigned = []

    for group_id in group_ids:
        role_name = role_map.get(group_id)
        if role_name:
            group, _ = Group.objects.get_or_create(name=role_name)
            user.groups.add(group)
            assigned.append(role_name)

    user.groups.exclude(name__in=assigned).filter(name__in=role_map.values()).delete()

post_authenticate.connect(sync_groups)





