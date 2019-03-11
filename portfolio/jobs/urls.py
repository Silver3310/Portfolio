
from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.homepage,
        name='home'
    ),
    path(
        'jobs/<int:job_id>',
        views.detail,
        name='detail'
    )
]
