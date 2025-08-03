from django.urls import include, path
from .views import construction_department_view
urlpatterns = [
    path('', construction_department_view, name='construction_department'),
    path('project/', include('project.urls')),        # ✅ Ensures projects are accessible
]
