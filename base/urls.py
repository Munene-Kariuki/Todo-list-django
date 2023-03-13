from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, SignupPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),
]
