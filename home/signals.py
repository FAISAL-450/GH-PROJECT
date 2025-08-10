from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

@receiver(user_logged_in)
def assign_group_on_login(sender, request, user, **kwargs):
    email = user.email.lower()
    if "helal" in email:
        group_name = "Construction"
    elif "payal" in email:
        group_name = "Sales"
    else:
        group_name = "General"

    group, _ = Group.objects.get_or_create(name=group_name)
    user.groups.add(group)
    user.save()

