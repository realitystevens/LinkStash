from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Link
from .serializers import LinkSerializer
from .forms import LinkForm
import pytz





def index(request):
    return render(request, 'index.html')


def dashboard(request):
    links = Link.objects.all()

    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = LinkForm()


    context = {
        'links': links,
        'form': form
    }


    return render(request, 'dashboard.html', context)


def account(request):
    if request.method == 'POST':
        request.session['user_timezone'] = request.POST['timezone']

        return redirect('dashboard')
    
    context = {
        'timezones': pytz.common_timezones,
    }

    
    return render(request, 'account.html', context)




class LinkCreate(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    
class LinkRetrieve(generics.ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class LinkUpdate(generics.RetrieveUpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = 'pk'
    
class LinkDelete(generics.RetrieveDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = 'pk'
