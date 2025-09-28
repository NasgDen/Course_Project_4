import secrets

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import (PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordResetDoneView, PasswordResetView)
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import (CustomProfileForm, CustomUserCreationForm, UserPasswordChangeForm, UserPasswordResetForm,
                         UserSetNewPasswordForm)
from users.models import CustomUser


class RegistrationView(CreateView):
    """Контроллер для регистрации пользователя"""

    # model = CustomUser
    # fields = ['email', 'phone_number', 'avatar', 'country']
    template_name = "users/registration.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("message:index")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        host = self.request.get_host()
        user.token = token
        user.save()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Здравствуйте, передите по ссылке для подтверждения своей почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class EditCustomUser(UpdateView):
    """Контроллер для редактирования профиля пользователя"""

    model = CustomUser
    template_name = "users/edit_user.html"
    form_class = CustomProfileForm
    success_url = reverse_lazy("message:index")


class UserPasswordChangeView(PasswordChangeView):
    """Контроллер для изменения пароля пользователя"""

    model = CustomUser
    template_name = "users/edit_user.html"
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("message:index")


class UserPasswordReset(SuccessMessageMixin, PasswordResetView):
    """Контроллер для сброса пароля пользователя"""

    template_name = "users/password_reset.html"
    email_template_name = "users/password_reset_email.html"
    from_email = EMAIL_HOST_USER
    form_class = UserPasswordResetForm
    success_url = reverse_lazy("users:password_reset_done")


class UserPasswordResetDoneView(PasswordResetDoneView):
    """Контроллер для использования шаблона при успешном сбросе пароля"""

    template_name = "users/password_reset_done.html"


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """Контроллер для предстовление установки нового пароля"""

    form_class = UserSetNewPasswordForm
    template_name = "users/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    """Контроллер для использования шаблона при успешном восстановлении пароля"""

    template_name = "users/password_reset_complete.html"
    # form_class = UserSetNewPasswordForm


def email_varification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserListView(ListView):
    """Класс реализующий интерфейс для отображения информации о пользователях"""

    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"


class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Класс реализующий интерфейс для отображения детальной информации о пользователе"""

    model = CustomUser
    template_name = "users/user_detail.html"
    context_object_name = "user_detail"
    permission_required = "users.view_customuser"


class BlockUserView(LoginRequiredMixin, View):
    """Класс реализующий интерфейс для блокировки пользователя"""

    def post(self, request, *args, **kwargs):
        user_id = kwargs["pk"]
        print(f"User_id {user_id}")
        user = get_object_or_404(CustomUser, id=user_id)
        print(f"User {user.email}")
        if not request.user.groups.filter(name="Manager").exists():
            return HttpResponseForbidden("У вас нет прав для публикации товара.")
        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True
        user.save()

        return redirect("users:user_detail", pk=user_id)
