from rest_framework_nested.routers import NestedSimpleRouter, SimpleRouter
from sgp.viewsets import UserViewSet, ProjectViewSet, TaskViewSet
from sgp.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from django.urls import path, include

routes = SimpleRouter()
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
routes.register(r'users', UserViewSet, basename='users')
routes.register(r'projects', ProjectViewSet, basename='projects')

project_routes = NestedSimpleRouter(routes, r'projects', lookup='project')
project_routes.register(r'tasks', TaskViewSet, basename='project-tasks')

urlpatterns = [
    path("", include(routes.urls)),
    path("", include(project_routes.urls)),
]