from django.shortcuts import render, redirect
from .form import RegistrationForm, UserLoginForm
from django.contrib.auth import get_user_model

User = get_user_model()
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from .token import TokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.utils import timezone
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.

account_activation_token = TokenGenerator()


def registration(request):
    if request.method != "POST":
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            try:
                exist_user = User.objects.get(email=email)
                if not exist_user.is_active:
                    exist_user.delete()
                else:
                    return render(
                        request,
                        "auth/registration.html ",
                        {
                            "form": form,
                            "error": "Данный пользователь уже зарегистрирован",
                        },
                    )
            except:
                pass

            user = form.save(commit=False)

            user.is_active = False
            user.save()

            # Потверждение через почту
            domain = get_current_site(request).domain
            email_subject = "Link to confirm your email"
            message = render_to_string(
                "auth/acc_activate_email.html",
                {
                    "user": user,
                    "domain": domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            to_email = email
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()

            return render(
                request, "auth/register_email_messege.html", {"email": to_email}
            )
    return render(request, "auth/registration.html", {"form": form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        time_elapsed = timezone.now() - user.date_joined
        if time_elapsed.total_seconds() < 900:
            user.is_active = True
            user.save()
            return render(request, "auth/activate_result.html", {"is_active": True})
        else:
            return render(
                request,
                "auth/activate_result.html",
                {"is_active": False},
            )


def user_login(request):
    if request.method != "POST":
        form = UserLoginForm()
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"], password=form.cleaned_data["password"]
            )
            if user is not None:
                auth_login(request, user)
                return redirect("doctor_list")
    return render(request, "auth/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("doctor_list")
