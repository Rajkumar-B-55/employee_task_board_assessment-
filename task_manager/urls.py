from django.urls import path

from .views import CustomAuthToken, UserListCreateView, UserRetrieveUpdateDeleteView, TaskListCreateView, \
    TaskRetrieveUpdateDeleteView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('api/token/', CustomAuthToken.as_view()),
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('api/users/', UserListCreateView.as_view()),
    path('api/users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view()),
    path('api/tasks/', TaskListCreateView.as_view()),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view()),
]
