from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
    path('home', views.index_page,name='home'),
    path('add', views.add_snippet_page,name='snippets-add'),
    path('list', views.snippets_page,name='snippets-list'),
    path('snippet/<int:id>',views.snippet_page, name='snippet-page'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
