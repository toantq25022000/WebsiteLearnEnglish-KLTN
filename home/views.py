from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .forms import registerForm, loginForm,ContactForm
from django.views import View
from django.contrib.auth.models import User
from usermember.models import MyUser
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect
from course.models import Chapter, Course
from usermember.models import Student,Teacher
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail, BadHeaderError
# Create your views here.


def index(request):
    course = Course.objects.all()
    teacher = Teacher.objects.filter(active=True)[:5]
    context = {
        'course':course,
       'teacher':teacher,
    }
    return render(request,'home/index.html',context)

def About(request):
    return render(request, 'home/about.html')

def Contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        name=''
        email=''
        comment=''
        form= ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            name= form.cleaned_data.get("fullname")
            email= form.cleaned_data.get("email")
            comment=form.cleaned_data.get("content")

            if request.user.is_authenticated:
                subject= str(request.user) + "'s phản hồi"
            else:
                subject= str(name) +"'s phản hồi"


            comment= name + " với email, " + email + ", gửi thông tin phản hồi với nội dung:\n\n" + comment;
            send_mail(subject, comment, email, ['toantran25022000@gmail.com'])
            suse = "Cảm ơn bạn đã đóng góp ý kiến. Chúng tối đã nhận được phản hồi từ bạn!!"

            context= {'form': form,'suse':suse}

            return render(request, 'home/contact.html', context)

        else:
            context= {'form': form}
            return render(request, 'home/contact.html', context)

    return render(request, "home/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Cảm ơn bạn đóng góp ý kiến.')     

def search_text(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if q == '':
            return redirect('home:index')
        else:
            # co du lieu
              
            data_search = Chapter.objects.filter(title__icontains=q)
            count_search = Chapter.objects.filter(title__icontains=q).count()
            
            return render(request,'home/search.html',{'result':q,'data_search':data_search,'count_search':count_search})
    else:
        return redirect('home:index')

class registerTeacher(LoginRequiredMixin,View):   
    login_url = '/login/'
    def get(self, request):
        return render(request,'home/register_teacher.html')

    def post(self, request):
        print(request.POST)
        fullname = request.POST['fullname_id']
        title = request.POST['title_id']
        phone = request.POST['phone_id']
        email = request.POST['email_id']
        address = request.POST['address_id']
        linkVideo = request.POST['linkVideo_id']
        linkFB = request.POST['linkFB_id']
        experience = request.POST['experience_id']

        check_is_student = Student.objects.filter(user_id=request.user.id)
        check_is_teacher = Teacher.objects.filter(user_id=request.user.id)

        if check_is_student:
            return JsonResponse({'status': 500})

        if check_is_teacher:
            return JsonResponse({'status': 400})
        try:
            teacher = Teacher.objects.create(
                user=request.user,
                fullname=fullname,
                title=title,
                phone=phone,
                email=email,
                address=address,
                link_video=linkVideo,
                link_fb=linkFB,
                experience=experience
            )

            return JsonResponse({'status': 200})
        except:
            return JsonResponse({'status': 300})
    
def registerUser(request):
    form = registerForm()
    if request.user.is_authenticated:
        return redirect('usermember:dashboard_user',name_url="profile")
    if request.method == "POST":
        form = registerForm(request.POST)
        print(form)
        if form.is_valid():
            print('form valid')
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return redirect('usermember:dashboard_user',name_url="profile")
      
    return render(request, 'home/register.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'home/change_password.html', {
        'form': form
    })
    

class loginUser(View):
    def get(self, request):    
        return render(request,'home/login.html')
    def post(self,request):
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            return redirect('usermember:dashboard_user',name_url='course')
        else:          
            context = {'mess':'Tên đăng nhập hoặc mật khẩu không đúng','uN':username,'pW':password}
            return render(request,'home/login.html',context)

def logoutUser(request):
    logout(request)

