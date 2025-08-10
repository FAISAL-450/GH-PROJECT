from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .azure_graph import get_user_azure_groups
from django.conf import settings

@receiver(user_logged_in)
def map_azure_to_django_groups(sender, request, user, **kwargs):
    access_token = request.META.get("HTTP_X_MS_TOKEN_AAD_ACCESS_TOKEN")
    if not access_token:
        return

    azure_groups = get_user_azure_groups(access_token)
    mapping = settings.AZURE_AD_TO_DJANGO_GROUPS

    for azure_group in azure_groups:
        django_group_name = mapping.get(azure_group)
        if django_group_name:
            group_obj, _ = Group.objects.get_or_create(name=django_group_name)
            user.groups.add(group_obj)








