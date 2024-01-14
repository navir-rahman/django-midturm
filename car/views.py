from django.shortcuts import render
from .models import CarModel
from .form import QuantityUpdateForm
# Create your views here.
def CarDetailsView(request, id):
    car = CarModel.objects.get(id=id)
    if request.method == 'POST':
        form = QuantityUpdateForm(request.POST, instance=car)
        if form.is_valid():
            updated_quantity = car.quantity - 1
            car.quantity = updated_quantity
            form.save()


        return render(request, 'car_details.html', {'car': car, 'form': form})
    else:
        form = QuantityUpdateForm(instance=car)
    return render(request, 'car_details.html', {'car': car, 'form': form})

