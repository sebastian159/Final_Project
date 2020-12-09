from django.shortcuts import render, redirect
from .forms import GoalForm
from .models import Goals, models



from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'FitnessPage/Home.html')


def health_tips(request):

    return render(request, 'FitnessPage/Health_Tips.html')


def workout(request):

    return render(request, 'FitnessPage/Workout.html')


def location(request):

    return render(request, 'FitnessPage/Location.html')


def yelp(request):
    return render(request, 'FitnessPage/yelp.html')

def about_us(request):
    return render(request, 'FitnessPage/about_us.html')


def covid_tips(request):
    return render(request, 'FitnessPage/covid_tips.html')

def recipes(request):
    return render(request, 'FitnessPage/recipes.html')

def goals(request):
    goal = Goals.objects.all()

    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GoalForm()

    context = {'goals': goal, 'form': form}
    return render(request, 'FitnessPage/goals.html', context)


def update(request, id):
    goal = Goals.objects.get(id=id)

    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
    else:
        form = GoalForm(instance=goal)

    context = {'form': form}
    return render(request, 'FitnessPage/update.html', context)


def delete(request, id):
    goal = Goals.objects.get(id=id)
    if request.method == 'POST':
        goal.delete()
        return redirect('goals')
    context = {'goals': goal}
    return render(request, 'FitnessPage/delete.html', context)


def complete(request, id):
    goal = Goals.objects.get(id=id)
    goal.completed = True
    goal.save()
    return redirect('goals')




#def AboutUs(request):
#def CovidTips(request):
#def FoodTips(request):
#def Resolution(request):
#def Membership(request):