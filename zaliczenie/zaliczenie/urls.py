from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from photography_app import views as ex_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ex_views.Homepage.as_view(), name='home'),
    path('create_contact/<int:pk>', ex_views.AddContactView.as_view(), name='create_contact'),
    path('edit_contact/<int:pk>/', ex_views.EditContactView.as_view(), name='edit-contact'),
    path('create_gallery/<int:pk>', ex_views.CreateGalleryView.as_view(), name='create-gallery'),
    path('gallery/<int:pk>', ex_views.GalleryDetailView.as_view(), name='gallery'),
    path('gallery_list/', ex_views.GalleryListView.as_view(), name='gallery-list'),
    path('edit_gallery/<int:pk>/', ex_views.EditGalleryView.as_view(), name='edit-gallery'),
    path('delete/<int:pk>/', ex_views.GalleryViewDelete.as_view(), name='delete-gallery'),
    path('members/', include('django.contrib.auth.urls')),
    path('register/', ex_views.RegisterView.as_view(), name='user-register'),
    path('create_profile/<int:pk>', ex_views.CreateProfileView.as_view(), name='create-profile'),
    path('profile/<int:pk>/', ex_views.ProfileView.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', ex_views.ProfileEditView.as_view(), name='edit-profile'),
    path('add_availability/<int:pk>', ex_views.AddAvailabilityView.as_view(), name='add-availability'),
    path('create_message/', ex_views.CreateMessage.as_view(), name='create_message'),
    path('message_box/<int:pk>/', ex_views.MessageBox.as_view(), name='message-box'),
    path('message/<int:pk>', ex_views.MessageDetail.as_view(), name='message'),
    path('events/<int:pk>', ex_views.EventsList.as_view(), name='events'),
    path('add_photo/', ex_views.AddPhoto.as_view(), name='add_photo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
