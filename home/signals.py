import logging
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import Group
from django.conf import settings

logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def assign_group(sender, request, user, **kwargs):
    # Retrieve Azure AD group IDs from session
    azure_group_ids = request.session.get("azure_groups", [])
    if not azure_group_ids:
        logger.warning(f"No Azure AD groups found in session for user '{user.username}'")
        return

    # Retrieve role mapping from settings
    roles_mapping = getattr(settings, "AZURE_AUTH", {}).get("ROLES", {})
    if not roles_mapping:
        logger.warning("AZURE_AUTH['ROLES'] mapping is missing or empty in settings.")
        return

    # Assign Django groups based on Azure AD group IDs
    for azure_id in azure_group_ids:
        group_name = roles_mapping.get(azure_id)
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            logger.info(
                f"Assigned Django group '{group_name}' to user '{user.username}' "
                f"(Azure group ID: {azure_id}, created={created})"
            )
        else:
            logger.info(
                f"Azure group ID '{azure_id}' not mapped to any Django group for user '{user.username}'"
            )

    # Optional: log final group list
    final_groups = [g.name for g in user.groups.all()]
    logger.info(f"Final Django groups for user '{user.username}': {final_groups}")

