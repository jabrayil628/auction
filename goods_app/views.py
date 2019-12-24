from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,TemplateView,UpdateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from time import strftime
from .models import Goods
from .forms import GoodsUploadForm
from user_app.views import MyUser



def goods_create_view(request):
    if request.method == 'POST':
        print("Yuklenen fayl: ",request.FILES)
        form=GoodsUploadForm(request.POST,request.FILES)
       
        if form.is_valid():
            goods = form.save(commit=False)
            goods.owner = request.user
            goods.save()
            return render(request,'user_profile.html')

    return redirect(reverse_lazy('users:user-detail',  kwargs={'pk': request.user.id}))

class AboutView(TemplateView):
    template_name='about.html'
    
class IndexView(TemplateView):
    template_name='main.html'
   
class ContactView(TemplateView):
    template_name='contact.html'
    
    


class RaiseView(UpdateView):
    model = Goods
    fields = ['price']
    success_url=reverse_lazy('goods:goods')
    def post(self, request, *args, **kwargs):
        price=Goods.objects.get(id=kwargs['pk']).price
        my_user = MyUser.objects.get(user=request.user.id)
        budget=my_user.budget

        # before_person=Goods.objects.get(id=kwargs['pk'])
        # print(my_user)
        # print(before_person)
        offer=int(request.POST['price'])
        if offer>price and offer<=budget:
            good = self.get_object()
            son_teklif_eden_id=good.offer_person.user.id
            aktiv_id=request.user.id
           
            if son_teklif_eden_id==aktiv_id:
                data={'error':'Hal-hazırda ən yüksək təklif sizindir'}
                return JsonResponse(data=data)
            
            good.offer_person.budget+=price
            good.offer_person.save()
            my_user.budget-=offer
            my_user.save()
            # print(my_user.budget)

            # my_user.budget+=price
            # print(my_user.budget)
            super().post(request, *args, **kwargs)
            good.offer_person = my_user
            good.price  = offer
            good.save()
            data={'price':offer}
            # print(kwargs)
            # person=Goods.objects.get(id=kwargs['pk'])
            # print(person)


          
        elif offer>budget:
            data={'error':'Kifayət qədər pulunuz yoxdur...'}
           
        elif offer<=price:
            data={'error':'Təklif etdiyiniz məbləğ daha yüksək olmalıdır...'}
        else:
            data={'error':'Bilinməyən bir xəta baş verdi...'}
        return JsonResponse(data=data)
def AjaxGetInfoView(request,pk):
    if request.method == 'POST':
        obj=Goods.objects.get(id=pk)
     
        return JsonResponse(data={'obj':obj.price})

class GoodsDetails(DetailView):
    model=Goods
    context_object_name='goods'
    template_name='detailed.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     good = self.get_object()
    #     zaman=good.auctionDeadLine
    #     convert=zaman.strftime('%d %b %Y').upper()+ " " +zaman.strftime('%H:%M:%S')
    #     context["deadline"] = convert
    #     return context

# class GoodsCategories(ListView):
#     model=Goods
#     context_object_name='goods'
#     template_name='goods_categories.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["categories"] = Category.objects.all()
#         return context
        
#     def get_queryset(self,**kwargs):

#         #print(self.kwargs)
#         return Goods.objects.filter(category=self.kwargs['pk'])
class GoodsView(ListView):
    model=Goods
    context_object_name='goods'
    template_name='store.html'
    paginate_by=6
    
    def get_queryset(self):
        sorgu = self.request.GET.get('word')
        if type(sorgu).__name__ == 'NoneType':
            return Goods.objects.all()
        else:
            return Goods.objects.filter(name__icontains=sorgu)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context
# class SearchView(ListView):
#     model=Goods
#     context_object_name='goods'
#     template_name='search_list.html'
#     def get_queryset(self,**kwargs):
#         query=self.request.GET.get('q')
#         print(query)
#         if query:
#             print(Goods.objects.filter(name=query))
#             return Goods.objects.filter(name=query)
#         else:
#             return Goods.objects.all()
