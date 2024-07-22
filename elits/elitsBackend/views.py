from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Merchandise, Officer, Students, VerificationToken
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from .forms import StudentCreationForm, StudentLogin

from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings 

# Create your views here.
def index(request):
    events = Event.objects.all()
    for event in events:
        event.parsed_date = datetime.strptime(event.eventDate, '%d/%m/%Y')
        event.date = event.parsed_date.strftime('%B %d, %Y')

    events = sorted(events, key=lambda x: x.parsed_date, reverse=True)
    recent_events = sorted(events, key=lambda x: x.parsed_date, reverse=True)[:3]
    print(events)
    return render(request, 'sections/homepage/homepage.html', {'events': events, 'recent_events': recent_events})

def shop(request):
    lanyards = Merchandise.objects.filter(category='Lanyard')
    for lanyard in lanyards:
        lanyard.originalPrice = round(lanyard.originalPrice)
        lanyard.discountPrice = round(lanyard.discountPrice)
    shirts = Merchandise.objects.filter(category='T-shirt')
    return render(request, 'sections/shop/shop.html', {'lanyards': lanyards, 'shirts': shirts})

def who_we_are(request):
    officers = Officer.objects.all()
    return render(request, 'sections/who-we-are/who-we-are.html', {'officers': officers})

def signup(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            try:
                student = Students.objects.get(email=email)
            except Students.DoesNotExist:
                messages.error(request, f"No result found on student having an email of {email}")
                return redirect('signup')

            if User.objects.filter(email=email).exists():
                messages.error(request, f"E-mail {email} already taken")
                return redirect('signup')
            elif len(form.cleaned_data['password1']) < 8:
                messages.error(request, "Password must contain atleast 8 characters.")
                return redirect('signup')
            elif form.cleaned_data['password1'] != form.cleaned_data['password2']:
                messages.error(request, "Password do not matched")
                return redirect('signup')
            
            password = form.cleaned_data['password1']
            
            token = get_random_string(32)
            VerificationToken.objects.create(student=student, token=token, password=password)

            verificationLink = request.build_absolute_uri(f"/verify_email/{token}/")
            send_mail(
                'Verify your ELITS account',
                f"Please click the following link to verify your email: {verificationLink}",
                settings.DEFAULT_FROM_EMAIL, 
                [email],
                fail_silently=False,
            )

            messages.info(request, f"A verification email has been sent to {email}. Please check your email")
            return redirect('signup')
    else:
        form = StudentCreationForm()
        
    return render(request, 'signup.html', {'form': form})

def verify_email(request, token):
    try:
        verfication_token = VerificationToken.objects.get(token=token)
        user = verfication_token.user
    except VerificationToken.DoesNotExist:
        messages.error(request, "Invalid")
        return redirect('signup')
    
    user = User.objects.create_user(username=verfication_token.student.email, email=verfication_token.student.email, password=verfication_token.password)
    user.is_active = True
    user.save()

    student = Students.objects.get(email=verfication_token.student.email)
    student.user = user
    student.save()

    verfication_token.delete()

    messages.success(request, "Email has been verified")
    return redirect('login')
    
def login(request):
    if request.method == 'POST':
        form = StudentLogin(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            pasword = form.cleaned_data['password']
            print(email)
            user = authenticate(username=email, password=pasword)
            if user is not None:
                auth_login(request, user)
                return redirect('student_dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
                return redirect('login')
    else:
        form = StudentLogin()

    return render(request, 'login.html', {'form': form})

def logout(request):
    messages.success(request, 'You have logged out.')
    auth_logout(request)
    return redirect('homepage')


def student_dashboard(request):
    return render(request, 'dashboard.html', {})





















# site = get_current_site(request)
            # mailSubject = 'Activate your ELITS account'
            # message = render_to_string('activate-email.html', {
            #     'domain': site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(email)),
            #     'token': account_activation_token.make_token()
            # })

# def signup(request):
#     if request.method == 'POST':
#         form = StudentCreationForm(request.POST)
#         if form.is_valid():
#             student = form.save(commit=False)
#             student.is_verified = False
#             student.save()
#             site = get_current_site(request)
#             mailSubject = 'Activate your ELITS Account'
#             message = render_to_string('activate-email.html', {
#                 'student': student,
#                 'domain': site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(student.pk)),
#                 'token': account_activation_token.make_token(student),
#             })
#             toEmail = form.cleaned_data.get('email')
#             email = EmailMessage(mailSubject, message, to=[toEmail])
#             email.send()
#             return render(request, 'email-verify.html')
#             # email = form.cleaned_data['email']
            
#     else:
#         form = StudentCreationForm()
        
#     return render(request, 'signup.html', {'form': form})

# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         student = get_object_or_404(StudentProfile, pk=uid)
#     except(TypeError, ValueError, OverflowError, StudentProfile.DoesNotExist):
#         student = None
#     if student is not None and account_activation_token.check_token(student, token):
#         student.is_verified = True
#         student.save()
#         return render(request, 'homepage.html')
#     else:
#         return render(request, 'signup.html')