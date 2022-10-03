from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, AddPhotoForm
from .models import (User,
                     Profile,
                     Contact,
                     Gallery,
                     Availability,
                     Message,
                     Photos
                     )


# Create your views here.


class Homepage(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class CreateProfileView(View):
    template_name = 'create_profile.html'

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        ctx = {'user': user}

        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        user_id = request.POST.get('user')
        description = request.POST.get('description')
        profile = User.objects.get(id=pk)
        id_error = "Don't mess with my code ;)"
        if int(user_id) == profile.id:
            Profile.objects.create(user_id=user_id, description=description)
            return redirect('/')
        else:
            ctx = {'id_error': id_error}
            return render(request, self.template_name, ctx)


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'edit_profile.html'
    fields = ['description', 'image']

    def get_success_url(self):
        return f'/gallery_list/'


class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)
        galleries = Gallery.objects.filter(profile=pk)
        try:
            contact = Contact.objects.get(profile=pk)
            ctx = {'profile': profile,
                   'galleries': galleries,
                   'contact': contact}
        except:
            ctx = {'profile': profile,
                   'galleries': galleries}

        return render(request, self.template_name, ctx)


class AddContactView(View):
    template_name = 'contact_info.html'

    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)
        ctx = {'profile': profile}

        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        profile = User.objects.get(id=pk)
        profile_id = request.POST.get('profile_id')
        city = request.POST.get('city')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        instagram = request.POST.get('instagram')
        facebook = request.POST.get('facebook')
        website = request.POST.get('website')
        error = "Don't mess with my code ;)"
        if not profile_id or not city or not country or not phone or not email:
            error = "Fill all * inputs"
            ctx = {'profile': profile,
                   'error': error}
            return render(request, 'contact_info.html', ctx)
        if int(profile_id) == profile.id:
            Contact.objects.create(profile_id=profile_id,
                                   city=city,
                                   country=country,
                                   phone=phone,
                                   email=email,
                                   instagram=instagram,
                                   facebook=facebook,
                                   website=website)
            return redirect('/profile/{}'.format(profile.id))
        else:
            ctx = {'profile': profile,
                   'error': error}
            return render(request, 'contact_info.html', ctx)


class EditContactView(View):
    template_name = 'edit_contact.html'

    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)
        ctx = {'profile': profile}

        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        profile = User.objects.get(id=pk)
        profile_id = request.POST.get('profile_id')
        city = request.POST.get('city')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        instagram = request.POST.get('instagram')
        facebook = request.POST.get('facebook')
        website = request.POST.get('website')
        error = "Don't mess with my code ;)"
        if len(phone) > 9:
            error = 'wrong number'
            return render(request, 'edit_contact.html', {'profile': profile, 'error': error})
        if not profile_id or not city or not country or not phone or not email:
            error = "Fill all * inputs"
            ctx = {'profile': profile,
                   'error': error}
            return render(request, 'edit_contact.html', ctx)
        if int(profile_id) == profile.id:
            Contact.objects.update(profile_id=profile_id,
                                   city=city,
                                   country=country,
                                   phone=phone,
                                   email=email,
                                   instagram=instagram,
                                   facebook=facebook,
                                   website=website)
            return redirect('/profile/{}'.format(profile.id))
        else:
            ctx = {'profile': profile,
                   'error': error}
            return render(request, 'edit_contact.html', ctx)


class CreateGalleryView(View):
    template_name = 'create_gallery.html'

    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)
        ctx = {'profile': profile}
        return render(request, 'create_gallery.html', ctx)

    def post(self, request, pk):
        profile = Profile.objects.get(id=pk)
        profile_id = request.POST.get('user')
        title = request.POST.get('title')
        content = request.POST.get('content')
        teaser = request.POST.get('teaser')
        id_error = "Don't mess with my code ;)"
        if not profile_id or not title or not content or not teaser:
            error = "Fill all places"
            ctx = {'profile': profile,
                   'error': error}
            return render(request, 'create_gallery.html', ctx)
        if int(profile_id) == profile.id:
            Gallery.objects.create(profile_id=profile_id, title=title, content=content, teaser=teaser)
            return redirect('/profile/{}'.format(profile.id))
        else:
            ctx = {'id_error': id_error,
                   'profile': profile}
            return render(request, 'create_gallery.html', ctx)


class EditGalleryView(UpdateView):
    model = Gallery
    template_name = 'edit_gallery.html'
    fields = ['title', 'content', 'teaser']

    def get_success_url(self):
        return f'/gallery_list/'


class GalleryDetailView(View):
    model = Gallery
    template_name = "gallery.html"

    def get(self, request, pk):
        gallery = Gallery.objects.get(id=pk)
        photos = Photos.objects.filter(gallery=pk)

        ctx = {'gallery': gallery,
               'photos': photos}
        return render(request, self.template_name, ctx)

    def post(self, request):
        return render(request, self.template_name)


class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery_list.html'
    ordering = ['id']


class DeleteGalleryView(DeleteView):
    model = [Gallery, Profile]
    template_name = 'gallery_confirm_delete.html'
    success_url = reverse_lazy('gallery-list')


class CreateMessage(CreateView):
    model = Message
    template_name = 'create_message.html'
    fields = '__all__'

    def get_success_url(self):
        return f'/gallery_list'


class AddPhoto(CreateView):
    model = Photos
    # fields = '__all__'
    template_name = 'add_photos.html'
    form_class = AddPhotoForm

    def get_success_url(self):
        return f'/gallery_list'


class MessageBox(View):
    template_name = 'message_list.html'

    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)
        communication = Message.objects.filter(profile=pk).order_by('-created')

        ctx = {'profile': profile,
               'messages': communication}
        return render(request, self.template_name, ctx)


class MessageDetail(DetailView):
    model = Message
    template_name = 'message_detail.html'


class AddAvailabilityView(View):
    template_name = 'add_availability.html'

    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)
        ctx = {'profile': profile}

        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        profile = User.objects.get(id=pk)
        profile_id = request.POST.get('profile_id')
        date = request.POST.get('date')
        start = request.POST.get('start')
        end = request.POST.get('end')
        error = "Don't mess with my code ;)"
        if not profile_id or not start or not date or not end:
            error = "Fill all places"
            ctx = {'profile': profile,
                   'error': error}
            return render(request, 'add_availability.html', ctx)
        if int(profile_id) == profile.id:
            Availability.objects.create(profile_id=profile_id, date=date, start=start, end=end)
            return redirect('/add_availability/{}'.format(profile.id))
        else:
            ctx = {'profile': profile,
                   'error': error}
            return render(request, 'add_availability.html', ctx)


class EventsList(View):
    template_name = 'events.html'
    model = Availability

    def get(self, request, pk):
        profile = Profile.objects.get(id=pk)
        event_list = Availability.objects.filter(profile=pk).order_by('date').order_by('start')
        ctx = {'profile': profile,
               'event_list': event_list}

        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        profile = Profile.objects.get(id=pk)
        booked_list = request.POST.getlist('boxes')
        accepted_list = request.POST.getlist('accepted_box')
        short_message = request.POST.get('short_message')

        for x in booked_list:
            Availability.objects.filter(pk=int(x)).update(booked=True, short_message=short_message)

        for y in accepted_list:
            Availability.objects.filter(pk=int(y)).update(reserved=True)

        return redirect('/events/{}'.format(profile.id))
