from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import Group
from home.models import RoleOverride

@receiver(user_logged_in)
def assign_group_on_login(sender, request, user, **kwargs):
    try:
        # Normalize email casing
        email = user.email.lower()
        print(f"🔍 Incoming email: {email}")

        # Look up RoleOverride
        override = RoleOverride.objects.filter(email=email).first()

        if override:
            print(f"✅ RoleOverride match: {override.email} → {override.group_name}")

            # Get or create the group
            group, _ = Group.objects.get_or_create(name=override.group_name)

            # Clear existing groups and assign new one
            user.groups.clear()
            user.groups.add(group)

            print(f"🎯 Assigned group: {group.name}")
        else:
            print(f"⚠️ No RoleOverride found for: {email}")

    except Exception as e:
        print(f"❌ Error in assign_group_on_login: {str(e)}")









