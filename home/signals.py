from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def assign_group_by_email(sender, request, user, **kwargs):
    try:
        # Normalize email casing
        email = user.email.lower()
        logger.info(f"🔍 Incoming email: {email}")

        # Look up group from settings
        group_name = settings.AZURE_AD_EMAIL_TO_GROUP.get(email)

        if not group_name:
            logger.warning(f"⚠️ No group mapping found for: {email}")
            return

        # Get or create the group
        group, _ = Group.objects.get_or_create(name=group_name)

        # Clear existing groups and assign new one
        user.groups.clear()
        user.groups.add(group)

        logger.info(f"🎯 Assigned group '{group.name}' to user '{user.username}'")

    except Exception as e:
        logger.exception(f"❌ Error in assign_group_by_email: {str(e)}")

