from django.core.files.storage import FileSystemStorage
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .models import *
from .price_comp import *
from price_app.models import Comments



# Create your views here.


def IndexView(request):
    return render(request, 'user/user_index.html', {})


def result(request):
    if request.method == 'GET':
        return redirect('home')
    elif request.method == 'POST':
        product_name = request.POST['product_name']
        id1= models.User.objects.get(id=request.user.id)
        products = price_comp(id1.id,product_name)

        print(id1.id)
        # return JsonResponse(context)
        return render(request, 'user/result.html', {"product_name": product_name, "products": products,})

class Add_comment(TemplateView):
    template_name='user/add_comments.html'

    def post(self , request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)

        comment =request.POST['comment']
        com = Comments()
        com.user=user
        com.comment=comment
        com.status='added'
        com.save()
        return render(request, 'user/user_index.html')

class View_comment(TemplateView):
    template_name='user/view_comment.html'
    def get_context_data(self, **kwargs):
        context = super(View_comment,self).get_context_data(**kwargs)

        commen = Comments.objects.filter(user_id=self.request.user.id)

        context['commen'] = commen
        return context

class Add_Wish_List(TemplateView):
    template_name = 'user/result.html'

    def dispatch(self, request, *args, **kwargs):
        pid = request.GET['id']
        print("222222222222222222222",pid)
        site_na= request.GET['sitename']
        ti = request.GET['title']
        img = request.GET['images']
        ur = request.GET['url']
        pri = request.GET['price']
        na = request.GET['nam']
        view_wish =View_Wish_list_values()
        view_wish.site=site_na
        view_wish.title = ti
        view_wish.image = img
        view_wish.url = ur
        view_wish.price = pri
        view_wish.user_id= pid
        view_wish.status="added"
        view_wish.nam= na
        view_wish.save()
        return render(request,'user/user_index.html',{'message': "Add to cart"})
        # if flip== "Amazon":
        #     print(55555555555555555555555555555)
        #     amazon =Amazon_Wish.objects.filter(user_id = pid)
        #     for i in amazon:
        #         i.status= 'added'
        #         i.save()
        #     return render(request,'user/result.html',{'message': "Add to cart"})
        #
        # else:
        #     print(66666666666666666666666666666)
        #     lis= Wish_List.objects.filter(user_id = pid)
        #     for i in lis:
        #         i.status= 'added'
        #         i.save()

class View_Wish_List(TemplateView):
    template_name = 'user/wish_list.html'
    def get_context_data(self, **kwargs):
        context = super(View_Wish_List,self).get_context_data(**kwargs)
        user=User.objects.get(id=self.request.user.id)
        wish = View_Wish_list_values.objects.filter(user_id=user,status="added")
        context['wish'] = wish
        return context

class Remove(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        remove = View_Wish_list_values.objects.get(id=id)
        remove.status = 'remove'
        remove.save()
        return render(request,'user/user_index.html',{'message':"Photo Removed"})

class statistics(TemplateView):
    template_name='user/statistics.html'
    def get_context_data(self, **kwargs):
        context = super(statistics,self).get_context_data(**kwargs)

class laptop_statistics(TemplateView):
    template_name='user/laptop_statistics.html'
    def get_context_data(self, **kwargs):
        context = super(laptop_statistics,self).get_context_data(**kwargs)
































