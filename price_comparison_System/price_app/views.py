from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from price_app.models import Registration, UserType
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

class RegistrationView(TemplateView):
    template_name = 'registration.html'
    def post(self,request,*args,**kwargs):
        name=request.POST['name']
        email=request.POST['email']
        mobile = request.POST['mobile']
        username = request.POST['username']
        password = request.POST['password']
        con_password= request.POST['con_password']

        if password== con_password:
            user=User.objects._create_user(username=username,password=password,email=email,first_name=name,is_staff='0',last_name='0')
            user.save()
            regs=Registration()
            regs.user= user
            regs.mobile=mobile
            regs.con_password=con_password
            regs.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "userr"
            usertype.save()
            messages = "Register Successfully."
            return render(request, 'user_reg.html', {'message': messages})
        else:
            messages = "Password does no t match!.."
            return render(request,'user_reg.html',{'message':messages})

# class Login(TemplateView):
#     template_name = 'login.html'
#     def post(self, request, *args, **kwargs):
#         username = request.POST['username']
#         password= request.POST['password']
#
#         user = authenticate(username=username,password=password)
#         if user is not None:
#
#             login(request,user)
#             return redirect('/user')
#
#         else:
#             return render(request,'login.html',{'message':"Invalid Username or Password"})


class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']

        user = authenticate(username=username,password=password)
        det = User.objects.get(id=1)
        det.last_name=1
        det.save()

        if user is not None:

            login(request,user)
            if user.last_name == '1':

                if user.is_superuser:
                    return redirect('/admin')

                # elif UserType.objects.get(user_id=user.id).type == "health_officer":
                #     return redirect('/health_officer')
                else:
                    return redirect('/user')

            else:


                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:

            return render(request,'login.html',{'message':"Invalid Username or Password"})





# class Login(TemplateView):
#     template_name='login.html'
#
#     def post(self, request, *args, **kwargs):
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#         det = User.objects.get(id=1)
#         det.last_name = 1
#         det.save()
#
#         if user is not None:
#
#             login(request, user)
#             if user.is_superuser:
#                 return redirect('/admin')
#             elif UserType.objects.get(user_id=user.id).type == "userr":
#                 return redirect('/user')
#
#
#         else:
#
#             return render(request, 'login.html', {'message': " User Account Not Authenticated"})



