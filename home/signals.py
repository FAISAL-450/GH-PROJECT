from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
@receiver(user_logged_in)
def assign_group_by_email(sender, request, user, **kwargs):
    try:
        email = user.email.lower()
        group_name = settings.AZURE_AD_EMAIL_TO_GROUP.get(email)
        if not group_name:
            logger.warning(f"No group mapping for: {email}")
            return
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.clear()
        user.groups.add(group)
        logger.info(f"Assigned group '{group.name}' to user '{user.username}'")
    except Exception as e:
        logger.exception(f"Error assigning group: {str(e)}")

