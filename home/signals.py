from django.contrib.auth.models import Group
def assign_azure_groups_to_user(user, azure_group_ids):
    for group_id in azure_group_ids:
        group_name = AZURE_GROUP_MAP.get(group_id)
        if group_name:
            group, _ = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)








