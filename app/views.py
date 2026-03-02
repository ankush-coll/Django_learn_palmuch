from django.shortcuts import render
from .models import Members, Songs
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import random
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import EmailOTP, SiteVisit
from .forms import RegisterForm
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib.admin.views.decorators import staff_member_required
import os
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

def root_redirect(request):
    return redirect('/accounts/login/')

# Create your views here.

@staff_member_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect("home")
    SiteVisit.objects.create()
    no_of_songs=Songs.objects.all().count()
    no_of_members=User.objects.all().count()
    #name_of_users=list(User.objects.values_list("username",flat=True))
    total_views=SiteVisit.objects.count()
    users=User.objects.order_by('-is_staff').all()
    staticfiles=os.path.join(settings.BASE_DIR,'prodstatic/app/')
    no_of_static=len(os.listdir(staticfiles))
    last_7_days = timezone.now() - timedelta(days=7)

    new_users = User.objects.filter(date_joined__gte=last_7_days).count()
    context={
        "songs":no_of_songs,
        "members":no_of_members,
        "static":no_of_static,
        "users":users,
        "site_views":total_views,
        "no_of_users":new_users
    }
    return render(request,'admin_dashboard.html',context=context)


@login_required
def data(request):
    data=Members.objects.all().values()
    return render(request, 'data.html',{'data':data})

@login_required
def photos(request):
    return render(request,'photos.html')

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def songs(request):
    data=Songs.objects.all()
    return render(request,'songs.html',{'data':data})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Delete old OTP
            EmailOTP.objects.filter(user=user).delete()

            # Generate OTP
            raw_otp = str(random.randint(100000, 999999))
            hashed_otp = make_password(raw_otp)

            EmailOTP.objects.create(
                user=user,
                otphash=hashed_otp
            )
            subject = "Verify Your Account"

            html_content = f"""
            <div style="font-family: Arial, sans-serif; padding: 20px;">
                <h2 style="color: #d63384;">Hello dear Palakian {user} 💕</h2>

                <p style="font-weight:bold;">Here’s your OTP:</p>

                <h1 style="color: #ff1493; letter-spacing: 3px;">
                    {raw_otp}
                </h1>

                <p style="font-weight:bold;">
                    Join us to enjoy her songs and know more about her 🎶
                </p>

                <br>
                <p>
                    Thanks,<br>
                    <strong>PlMh Admin Team</strong>
                </p>
            </div>
            """

            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                         subject,
                    text_content,
                    settings.EMAIL_HOST_USER,
                    [user.email]
                )
            email.attach_alternative(html_content, "text/html")
            email.send()

            # Send email
            # send_mail(
            #     "Verify your account",
            #     f"Your OTP is {raw_otp}",
            #     settings.EMAIL_HOST_USER,
            #     [user.email],
            # )
            print(form.errors)

            return redirect("verify-otp")
    # If form NOT valid, it must return here
        return render(request, "register.html", {"form": form})
        print(form.errors)
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

def verify_otp(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        entered_otp = request.POST.get("otp").strip()

        user = User.objects.filter(username=username).first()
        otp_obj = EmailOTP.objects.filter(user=user).first()

        if not otp_obj:
            return render(request, "verify_otp.html", {"error": "No OTP found"})

        # Expiry check (5 mins)
        if otp_obj.created_at < timezone.now() - timedelta(minutes=5):
            return render(request, "verify_otp.html", {"error": "OTP expired"})

        # Attempt limit
        if otp_obj.attempts >= 5:
            return render(request, "verify_otp.html", {"error": "Too many attempts"})

        if check_password(entered_otp, otp_obj.otphash):
            user.is_active = True
            user.save()
            otp_obj.delete()
            return redirect("login")
        else:
            otp_obj.attempts += 1
            otp_obj.save()
            return render(request, "verify_otp.html", {"error": "Invalid OTP"})

    return render(request, "verify_otp.html")