from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, MenuItem
from .forms import RestaurantForm, MenuItemForm
from django.http import JsonResponse

# Restaurant Views
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    menu_items = restaurant.menu_items.all()
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant, 'menu_items': menu_items})

def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/restaurant_form.html', {'form': form})

def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurants/restaurant_form.html', {'form': form})

def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'GET':
        restaurant.delete()
        return JsonResponse({
            'success': True
        })

    return JsonResponse({
        'success': False
    })

# MenuItem Views
def menu_item_create(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant = restaurant
            menu_item.save()
            return redirect('restaurant_detail', pk=restaurant_id)
    else:
        form = MenuItemForm()
    return render(request, 'restaurants/menu_item_form.html', {'form': form, 'restaurant': restaurant})

def menu_item_update(request, restaurant_id, pk):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu_item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('restaurant_detail', pk=restaurant_id)
    else:
        form = MenuItemForm(instance=menu_item)
    return render(request, 'restaurants/menu_item_form.html', {'form': form, 'restaurant': restaurant})

def menu_item_delete(request, restaurant_id, pk):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu_item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'GET':
        menu_item.delete()
        return JsonResponse({
            'success': True
        })

    return JsonResponse({
        'success': False
    })
