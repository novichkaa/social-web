from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


from django.shortcuts import render
from django.http import HttpResponseRedirect


def upload_images(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = CustomUserCreationForm

    return render(request, 'files/images.html', {'form': form})


# Create your views here.
from django.shortcuts import render


def upload_images(request):
    if request.method == 'GET':
        images = CustomUser.objects.order_by('title')
        return render(request, "files/images.html", {"images": images})
