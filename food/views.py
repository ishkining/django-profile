from django.shortcuts import render


def show_food_stats(request):
    return render(request, 'food/show-stats.html')
