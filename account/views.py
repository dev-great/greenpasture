from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib import messages,auth
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                    messages.error(request , 'User Name Already Taken')
                    return redirect('   account:register_view')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request , 'Email Name Already Exits ')
                    return redirect('account:register_view')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email)
                    # auth.login(request , user)
                    # messages.success(request,'You Are Now LoggedIn')
                    # return redirect('pages:index')
                    user.save()
                    messages.success(request,'You Are Now Registered')
                    return redirect('account:login_view')
        else:
            messages.error(request , 'Password Doest Not Match')
            return redirect('account:register_view')

    else:
        return render(request,'account/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email , password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Invalid Credentials')
            return render(request,'registration/index.html')
        else:
            messages.error(request,'You Are Now LoggedIn')
            return redirect('account:login_view')
    else:
        return render(request,'account/login.html')

def logout(request):
    auth.logout(request)
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You Are Now Logged Out')
        return render(request,'registration/index.html')
    else:
        return redirect('account:login_view')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "account/messages/email_confirmation_sent.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')
                        
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect ("account:login_view")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="account/password_reset.html", context={"password_reset_form":password_reset_form})