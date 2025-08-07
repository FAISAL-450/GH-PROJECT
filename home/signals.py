from django.contrib.auth.models import Group
from django_auth_adfs.signals import post_authenticate
from django.dispatch import receiver

@receiver(post_authenticate)
def sync_user_groups(sender, user=None, claims=None, **kwargs):
    group_names = claims.get("groups", [])
    user.groups.clear()

    for group_name in group_names:
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

    user.save()







