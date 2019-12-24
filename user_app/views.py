
from .models import MyUser,Message
from .forms import  (MyUserForm,
                    UserCreateForm,
                    Myloginform,
                    MyGoodsForm,
                    MyPasswordChangeForm,
                    
                    )
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,TemplateView,DetailView,UpdateView
from django.views.generic import FormView
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.auth import authenticate
class get_users(ListView):
    queryset=User.objects.all()
    context_object_name='users'
    template_name='users_list.html'

class ContactMessageView(View):
    def  post(self, request):
        name1 = request.POST.get('name', None)
        email1 = request.POST.get('email', None)
        message1 = request.POST.get('message', None)
        obj = Message.objects.create(
            name = name1,
            email = email1,
            content = message1
        )

        user = {'id':obj.id,'name':obj.name,'email':obj.email,'content':obj.content}

        data = {
            'user': user
        }
        return JsonResponse(data=data)

class SignUpView(View):
    def  post(self, request):
        name = request.POST.get('name', None)
        surname = request.POST.get('surname', None)
        email = request.POST.get('email', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        address = request.POST.get('address', None)
        phone = request.POST.get('phone', None)

        new_user = User.objects.create_user(username=username,
                                        first_name=name,
                                        last_name=surname,
                                        email=email)

        new_user.set_password(password)
        new_user.save()
        extraInfo=MyUser.objects.create(address=address,
                                        phone=phone,
                                        user=new_user)
        data={
            'a':'b'
        }
        return JsonResponse(data=data)

#2 form in one page

   
class AfterLogin(LoginView):
    redirect_field_name='goods:empty'



class CustomLoginView(LoginView):
    template_name="main.html"
    form_class = Myloginform
    redirect_field_name='goods:goods'

    def dispatch(self, request, *args, **kwargs):
        username=self.request.POST.get('username')
        password=self.request.POST.get('password')
        # user = authenticate(username=self.request.POST.get('username'), password=self.request.POST.get('password'))
        user = authenticate(self.request,username=username, password=password)
        if user is not None:
            login(request, user)
            data={'is_success':'Yonlendilirir'}
            return JsonResponse(data=data)
        elif username=="" or password=="":
            data={'is_error':'Username və ya şifrə boş ola bilməz...'}
            return JsonResponse(data=data)
        else:
            data={'is_error':'Email ve ya şifrə yanlışdır...'}
            return JsonResponse(data=data)
            # Return an 'invalid login' error message.
        
        
        # user=User.objects.filter(username=).first()
        # login(self.request,user)
        # return redirect("goods:goods")
    

# class UploadView(LoginRequiredMixin,CreateView):
#    template_name = 'goods_upload.html'
#    success_url = reverse_lazy('goods:upload')
#    form_class = MyUserForm

#    def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['my_form'] = MyGoodsForm()
#         #-------
#         my_form = MyGoodsForm(self.request.POST)
#         if my_form.is_valid():
#             goods = context['my_form'].save(commit=False)
#             goods.user = self.request.user
#             goods.save()
#         #--------
#         return context

#    def form_valid(self,form):
#       response = super().form_valid(form)


#       my_form = MyGoodsForm(self.request.POST,self.request.FILES)
#       if my_form.is_valid():
#             seller = my_form.save(commit=False)
#             seller.user = self.request.user
#             seller.save()

#       return response

class SettingsView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change.html'
    title = _('Password change')


# class UserProfilView(LoginRequiredMixin,DetailView):
#     model = User
#     template_name = 'user_profile.html'
#     context_object_name = 'user'

def UserProfilUpdateView(request):

    # print("acar kodu",id)
    # print("requestim:",request)
    if request.method == 'POST':

        get_user=User.objects.get(id=request.user.id)
        get_user.username=request.POST['username']
        get_user.first_name=request.POST['first_name']
        get_user.last_name=request.POST['last_name']
        get_user.email=request.POST['email']
        get_user.save()
        return redirect('users:profile')
        # form=MyUserForm(request.POST)
       
        # if form.is_valid():
        #     goods = form.save(commit=False)
        #     goods.owner = request.user
        #     goods.save()
    # return redirect('users:profile')
    return render(request,'user_profile.html')

