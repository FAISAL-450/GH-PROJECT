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

        # Safely get group mapping from settings
        group_map = getattr(settings, "AZURE_AD_EMAIL_TO_GROUP", {})
        group_name = group_map.get(email)

        if not group_name:
            logger.warning(f"No group mapping found for email: {email}")
            return

        # Assign group
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.clear()
        user.groups.add(group)

        # Ensure admin access
        if not user.is_staff:
            user.is_staff = True
            user.save()

        logger.info(f"User '{user.username}' assigned to group '{group.name}' and marked as staff.")
    except Exception as e:
        logger.exception(f"Error during group assignment for user '{user.username}': {str(e)}")



