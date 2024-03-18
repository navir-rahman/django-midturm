

from django.shortcuts import render
from .forms import ProfileForm
from car.models import OrderHistory


def ProfileView(request):
    user_instance = request.user
    all_orders = OrderHistory.objects.filter(user=user_instance)


    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
        return render(request, 'profile.html', {'form': form, 'btn_text': 'submit', 'all_orders': all_orders})

    else:
        form = ProfileForm(instance=user_instance)

    return render(request, 'profile.html', {'form': form, 'btn_text': 'submit', 'all_orders': all_orders})

