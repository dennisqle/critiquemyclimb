from django.shortcuts import render, get_object_or_404, redirect
from .models import Climb
from .forms import ClimbForm

# Create your views here.
def climbs_list(request):
    climbs = Climb.objects.all().order_by('-date_posted')
    return render(request, 'climbs/climbs_list.html', {'climbs': climbs})

def climbs_new(request):
    if request.method == 'POST':
        form = ClimbForm(request.POST)
        if form.is_valid():
            climb = form.save(commit=False)
            climb.poster = request.user
            climb.save()
            return redirect('climbs_detail', pk=climb.pk)
    else:
        form = ClimbForm()
    return render(request, 'climbs/climbs_edit.html', {'form': form})

def climbs_detail(request, pk):
    climb = get_object_or_404(Climb, pk=pk)
    return render(request, 'climbs/climbs_detail.html', {'climb': climb})

def climbs_edit(request, pk):
    climb = get_object_or_404(Climb, pk=pk)
    if request.method == 'POST':
        form = ClimbForm(request.POST, instance=climb)
        if form.is_valid():
            climb = form.save(commit=False)
            climb.poster = request.user
            climb.save()
            return redirect('climbs_detail', pk=climb.pk)
    else:
        form = ClimbForm(instance=climb)
    return render(request, 'climbs/climbs_edit.html', {'form': form})

