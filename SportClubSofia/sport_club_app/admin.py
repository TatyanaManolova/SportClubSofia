from django.contrib import admin
from django.contrib.auth import get_user_model

from SportClubSofia.sport_club_app.models import Skater, Competition

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')


@admin.register(Skater)
class SkaterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'coach', 'category')
    fields = ['first_name', 'last_name', 'coach', 'category']
    list_filter = ['category', 'coach']


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_city')
    search_fields = ['name']
