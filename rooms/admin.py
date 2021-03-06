from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass