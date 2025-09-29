from django.contrib import admin
from django.urls import path, include
from expenses import views as expense_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', expense_views.landing_page, name='landing'),  # 👈 New landing page
    path("admin/", admin.site.urls),
    path("expenses/", include("expenses.urls")),
    path("accounts/", include("django.contrib.auth.urls")),  # login/logout
    # Explicitly define LogoutView with next_page
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
]
