from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(Video)


