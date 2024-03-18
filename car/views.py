from django.shortcuts import render
from .models import CarModel, OrderHistory, Comment
from .form import QuantityUpdateForm, CommentForm
# Create your views here.
def CarDetailsView(request, id):
    car = CarModel.objects.get(id=id)
    all_comments = Comment.objects.all()
    print(all_comments)
    if request.method == 'POST':
        form = QuantityUpdateForm(request.POST, instance=car)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            print(comment_form)
            comment = comment_form.save(commit=False)
            comment.car = car
            comment.save()
            
        return render(request, 'car_details.html', {'car': car, 'form': form, 'comment_form': comment_form, 'all_comments': all_comments})
    else:
        form = QuantityUpdateForm(instance=car)
        comment_form = CommentForm(instance=car)
    return render(request, 'car_details.html', {'car': car, 'form': form, 'comment_form': comment_form, 'all_comments': all_comments})


def update_quantity(request, id):
    car = CarModel.objects.get(id=id)
    form = QuantityUpdateForm(instance=car)
    updated_quantity = car.quantity - 1
    car.quantity = updated_quantity
    car.save()
    OrderHistory.objects.get_or_create(user=request.user, car=car, quantity=1)
    return render(request, 'car_details.html', {'car': car, 'form': form})