from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from AppShortStories.views import (Inicio,
                                    BuscarGenero,GeneroCreate,GeneroDetail,GeneroUpdate,GeneroDelete,
                                    BuscarShortStories,ShortStoriesCreate,ShortStoriesDetail,ShortStoriesUpdate,ShortStoriesDelete,
                                    SignUp,Login,Logout,ProfileDetail,ProfileCreate,ProfileUpdate,MensajeCreate,MensajeList,MensajeUpdate)

urlpatterns =[
    path('',Inicio, name="inicio"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('mensaje/enviar', MensajeCreate.as_view(), name="mensaje-send"),
    path('mensaje/<pk>/edit', MensajeUpdate.as_view(), name="mensaje-edit"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('profile/<pk>/detail', ProfileDetail.as_view(), name="profile-detail"),
    path('profile/<pk>/edit', ProfileUpdate.as_view(), name="profile-edit"),
    path('profile/create',ProfileCreate.as_view(),name="profile-create"),
    path('genero/list', BuscarGenero.as_view(), name="genero-list"),
    path('genero/create', GeneroCreate.as_view(), name="genero-create"),
    path('genero/<pk>/detail', GeneroDetail.as_view(), name="genero-detail"),
    path('genero/<pk>/edit', GeneroUpdate.as_view(), name="genero-edit"),
    path('genero/<pk>/delete', GeneroDelete.as_view(), name="genero-delete"),
    path('stories/list', BuscarShortStories.as_view(), name="cuento-list"),
    path('stories/create', ShortStoriesCreate.as_view(), name="cuento-create"),
    path('stories/<pk>/detail', ShortStoriesDetail.as_view(), name="cuento-detail"),
    path('stories/<pk>/edit', ShortStoriesUpdate.as_view(), name="cuento-edit"),
    path('stories/<pk>/delete', ShortStoriesDelete.as_view(), name="cuento-delete"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)