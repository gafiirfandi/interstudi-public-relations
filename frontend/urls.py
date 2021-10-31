from django.urls import path

from .views import index,programlainnya,pendaftaranonline,hubungikami,gallery,biayastudi

urlpatterns = [
    path('', index, name='index'),
    path('programlainnya', programlainnya, name="programlainnya"),
    path('pendaftaranonline', pendaftaranonline, name="pendaftaranonline"),
    path('hubungikami', hubungikami, name="hubungikami"),
    path('gallery', gallery, name="gallery"),
    path('biayastudi', biayastudi, name="biayastudi"),
]
