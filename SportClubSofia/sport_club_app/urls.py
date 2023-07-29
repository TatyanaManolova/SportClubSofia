from django.urls import path, include

from SportClubSofia.sport_club_app.views import home_page, RegisterUserView, LoginUserView, \
    ProfileDetailsView, ProfileEditView, ProfileDeleteView, LogoutUserView, skaters_list, skater_create, skater_details, \
    skater_edit, skater_delete

urlpatterns = [
    path('', home_page, name='home_page'),
    path('register/', RegisterUserView.as_view(), name="register"),
    path('login/', LoginUserView.as_view(), name="login"),
    path('logout/', LogoutUserView.as_view(), name="logout"),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile_details'),
        path('edit/', ProfileEditView.as_view(), name='profile_edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile_delete')
    ])),
    path('skaters/', skaters_list, name='skaters'),
    path('create/', skater_create, name='skater_create'),
    path('details/<int:pk>/', skater_details, name='skater_details'),
    path('edit/<int:pk>/', skater_edit, name='skater_edit'),
    path('delete/<int:pk>/', skater_delete, name='skater_delete'),
]
