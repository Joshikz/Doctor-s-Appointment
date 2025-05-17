from django.shortcuts import render
from .form import RegistrationForm
from django.contrib.auth.models import User 
from django.core.mail import EmailMessage
# Create your views here.

def registration(request):
    if request.method != "POST":
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                 exist_user = User.objects.get(email = email)
                 if not exist_user.is_active:
                    exist_user.delete()
                 else:
                    return render(request, 'auth/registration.html', {'form': form, 'error': 'Данный пользователь уже зарегистрирован'})
            except:
                pass

            user = form.save(commit=False)
            user.is_active = False
            user.save()

            #Потверждение через почту
            email_subject = 'Ссылка на активацию аккаунта'
            message = 'Тестировка отправки сообщения'
            to_email = email
            email = EmailMessage( email_subject, message, to=[to_email])
            email.send()

            return render(request, 'auth/register_email_messege.html', {"email": email})
    return render(request, 'auth/registration.html', {'form': form}) 
            