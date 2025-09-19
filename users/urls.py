from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegistrationView, email_varification, EditCustomUser, UserPasswordChangeView

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='message:index'), name="logout"),
    path('email-confirm/<str:token>/', email_varification, name='email_varification'),
    path('edit_user/<int:pk>/', EditCustomUser.as_view(), name='edit_user'),
    path('edit_user/password/', UserPasswordChangeView.as_view(), name='password_change'),
    ]