"""framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  pathd('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView as BaseGraphQLView
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

class GraphQLView(BaseGraphQLView):

    @staticmethod
    def format_error(error):
        formatted_error = super(GraphQLView, GraphQLView).format_error(error)
        del formatted_error['locations']
        del formatted_error['path']
        try:
            formatted_error['context'] = error.original_error.context
        except AttributeError:
            pass

        return formatted_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view( html_email_template_name='registration/password_reset_email.html'),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]

admin.site.index_title = 'Member Dashboard'
admin.site.site_title = 'amFOSS CMS'