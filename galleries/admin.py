from django.contrib import admin
from galleries.models import ImageModel, Gallery, UserGallery, UserPublicGallery

admin.site.register(ImageModel)
admin.site.register(Gallery)
admin.site.register(UserGallery)
admin.site.register(UserPublicGallery)