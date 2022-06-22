from django.contrib.auth.models import User
from django.shortcuts import  render, redirect
from django.views.generic import TemplateView, View
from price_app.models import Comments, Registration


def IndexView(request):
    return render(request, 'admin/admin_index.html', {})

class View_Comment(TemplateView):
    template_name='admin/comments.html'
    def get_context_data(self, **kwargs):
        context = super(View_Comment,self).get_context_data(**kwargs)

        commen = Comments.objects.filter(status='added')

        context['commen'] = commen
        return context
    def post(self , request,*args,**kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id = request.POST['id']
        reply = request.POST['reply']
        rep = Comments.objects.get(id=id)
        # act.complaint=complaint
        rep.reply= reply
        rep.status = 'replied'
        rep.save()
        return redirect(request.META['HTTP_REFERER'])

class User_Approve(TemplateView):
    template_name = 'admin/user_approve.html'
    def get_context_data(self, **kwargs):
        context = super(User_Approve,self).get_context_data(**kwargs)

        user_approve = Registration.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['user_approve'] = user_approve
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class Approve_User_View(TemplateView):
    template_name = 'admin/approve_view.html'
    def get_context_data(self, **kwargs):
        context = super(Approve_User_View,self).get_context_data(**kwargs)

        user_view = Registration.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['user_view'] = user_view
        return context
