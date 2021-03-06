from django.urls import path

from ad.views import AdIndexView, AdCreateView, AdDetailView, AdDeleteView, AdUpdateView, AdModerateView

app_name = 'ad'

urlpatterns = [
    path('', AdIndexView.as_view(), name="index"),
    path('create/ad/', AdCreateView.as_view(), name="create_ad"),
    path('update/ad/<int:pk>/', AdUpdateView.as_view(), name="update_ad"),
    path('detail/ad/<int:pk>/', AdDetailView.as_view(), name="detail_ad"),
    path('delete/ad/<int:pk>/', AdDeleteView.as_view(), name="delete_ad"),
    path('moderated/', AdModerateView.as_view(), name="moderated_ad"),
]

