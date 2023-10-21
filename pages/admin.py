from django.contrib import admin
from .models import Image

admin.site.register(Image)

# Rene's note : I imported the custom Image class form the models library
# then I register it to make if available on admin.
