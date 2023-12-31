from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model

from SportClubSofia.sport_club_app.forms import LoginUserForm, RegisterUserForm, EditUserForm, SkaterCreateForm, \
    SkaterEditForm, SkaterDeleteForm, CompetitionCreateForm   # CompetitionEditForm, CompetitionDeleteForm
from SportClubSofia.sport_club_app.models import Skater, Competition

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'profile/create-profile.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):

        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'profile/login-page.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('skaters')


class LogoutUserView(auth_views.LogoutView):
    pass


def home_page(request):
    profile = UserModel

    context = {
        'profile': profile
    }
    return render(request, 'base/home-page.html', context)


class ProfileDetailsView(views.DetailView):
    template_name = 'profile/profile-details.html'
    model = UserModel

    profile_image = static('images/default.jpg')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_image'] = self.get_profile_image()
        # context['pets'] = self.request.user.pet_set.all()

        return context


class ProfileEditView(views.UpdateView):
    template_name = 'profile/edit-profile.html'
    model = UserModel
    form_class = EditUserForm

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(views.DeleteView):
    template_name = 'profile/delete-profile.html'
    model = UserModel
    success_url = reverse_lazy('home_page')


def get_skater(pk):
    skater = Skater.objects.filter(pk=pk).get()
    return skater


def get_competition(pk):
    competition = Competition.objects.filter(pk=pk).get()
    return competition


def skaters_list(request):

    skaters = Skater.objects.filter(coach=request.user)

    context = {
        'skaters': skaters,
        'skaters_len': len(skaters),
        # 'profile': profile
    }
    return render(request, 'base/skaters.html', context)


def show_coaches_list(request):
    coaches = UserModel.objects.filter()

    context = {
        'coaches': coaches,
        'coaches_len': len(coaches),
    }
    return render(request, 'base/coaches_list.html', context)


def skater_create(request):

    form = SkaterCreateForm(request.POST or None)  # , request.FILES or None)
    if form.is_valid():
        skater = form.save(commit=False)
        skater.coach = request.user
        skater.save()
        return redirect('skaters')

    context = {
        # 'profile': profile,
        'form': form
    }

    return render(request, 'skaters/create-skater.html', context)


def skater_details(request, pk):

    skater = get_skater(pk)
    profile = UserModel

    context = {
        'skater': skater,
        'profile': profile
    }

    return render(request, 'skaters/skater-details.html', context)


def skater_edit(request, pk):
    profile = UserModel
    skater = get_skater(pk)

    if request.method == 'GET':
        form = SkaterEditForm(instance=skater)
    else:
        form = SkaterEditForm(request.POST, instance=skater)
        if form.is_valid():
            form.save()
            return redirect('skaters')

    context = {
        'profile': profile,
        'skater': skater,
        'form': form
    }
    return render(request, 'skaters/edit-skater.html', context)


def skater_delete(request, pk):
    profile = UserModel
    skater = get_skater(pk)

    if request.method == 'GET':
        form = SkaterDeleteForm(instance=skater)
    else:
        form = SkaterDeleteForm(request.POST, instance=skater)
        if form.is_valid():
            form.save()
            return redirect('skaters')

    context = {
        'profile': profile,
        'skater': skater,
        'form': form
    }
    return render(request, 'skaters/delete-skater.html', context)


def show_competitions_list(request):
    competitions = Competition.objects.all()

    context = {
        'competitions': competitions,
        'competitions_len': len(competitions),
    }
    return render(request, 'base/competitions_list.html', context)


def competition_create(request):

    form = CompetitionCreateForm(request.POST or None)
    if form.is_valid():
        competition = form.save()
        competition.save()
        return redirect('competitions_list')

    context = {

        'form': form
    }

    return render(request, 'competitions/create-competition.html', context)

