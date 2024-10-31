from django.urls import path
from .views import UsuariosView, UsuarioQueryApiView
#url de publicacion
urlpatterns = [
    path('list', UsuariosView.as_view()),
    path('crear-usuario', UsuariosView.as_view()),
    path ('actualizar-usuario/<int:pkid>', UsuariosView.as_view(), name="actulizar_usuario"),
    path ('eliminar-usuario/<int:pkid>', UsuariosView.as_view(), name="eliminar_usuario"),
    path ('consultar/<int:pkid>', UsuarioQueryApiView.as_view(), name ="consultar")
]
