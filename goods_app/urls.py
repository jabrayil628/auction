from django.urls import path
from .views import (IndexView,
                    AboutView,
                    ContactView,
                    GoodsView,
                    GoodsDetails,
                    AjaxGetInfoView,goods_create_view)
# from user_app.views import UploadView

app_name='goods_app'

urlpatterns = [
    
    path('goods/',GoodsView.as_view(),name='empty'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('about/',AboutView.as_view(),name='about'),
    path('',IndexView.as_view(),name='goods'),
    # path('categories/<pk>/',GoodsCategories.as_view(),name='categories'),
    path('goods/<int:pk>/',GoodsDetails.as_view(),name='detail'),
    path('ajax/<int:pk>/',AjaxGetInfoView,name='ajax-detail'),
    path('upload/',goods_create_view, name='upload'),

]

