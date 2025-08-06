import logging
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import Group
from django.conf import settings

logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def assign_azure_ad_groups(sender, request, user, **kwargs):
    # 🔍 Get Azure AD group IDs from session
    azure_group_ids = request.session.get("azure_groups", [])
    roles_mapping = settings.AZURE_AUTH.get("ROLES", {})

    if not azure_group_ids:
        logger.warning(f"[Azure AD] No group IDs found in session for user '{user.username}'")
        return

    # 🧹 Clear existing Django groups to avoid stale assignments
    user.groups.clear()

    assigned_groups = []

    for azure_id in azure_group_ids:
        group_name = roles_mapping.get(azure_id)
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            assigned_groups.append(group_name)
            logger.info(f"[Azure AD] Assigned Django group '{group_name}' to user '{user.username}'")

    if assigned_groups:
        logger.info(f"[Azure AD] Final Django groups for user '{user.username}': {assigned_groups}")
    else:
        logger.warning(f"[Azure AD] No matching Django groups for user '{user.username}'")


