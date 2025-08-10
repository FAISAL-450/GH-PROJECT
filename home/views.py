from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def home_view(request):
    user = request.user
    email = getattr(user, 'email', 'N/A')
    groups = [g.name for g in user.groups.all()] if user.is_authenticated else []
    print(f"🧑 User: {user}")
    print(f"📧 Email: {email}")
    print(f"👥 Groups: {groups}")

    context = {
        'user_email': email,
        'user_groups': groups,
    }

    return render(request, 'home/home.html', context)



