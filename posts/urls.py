from django.urls import path
from . import views # . 으로 적은 이유는 내가 위치하고 있는 곳에서 가져오기 위해

app_name = 'posts' # 장고 내부에서 정해 놓은 것이며, 각각의 핼동을 지정해줄수 있다?

urlpatterns = [
    
    # Read
    path('', views.index, name='index'), #여떤 데이터를 넣어도 posts의 데이터를 가져온다.
    path('<int:id>/', views.detail, name='detail'),

    # Create
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # Delete
    path('<int:id>/delete/', views.delete, name='delete'),

    # Update
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update'),

]