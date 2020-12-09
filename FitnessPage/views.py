from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import GoalForm, UserRegistrationForm
from .models import Goals, models
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# from django.contrib import messages


# @login_required decorator allows to limit access to the index page and check whether the user is authenticated
# if so, index page is rendered. If not, the user is redirected to the login page via login_url
@login_required(login_url='login')


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





def register_view(request):
   # This function renders the registration form page and create a new user based on the form data
   if request.method == 'POST':
       # We use Django's UserCreationForm which is a model created by Django to create a new user.
       # UserCreationForm has three fields by default: username (from the user model), password1, and password2.
       # If you want to include email as well, switch to our own custom form called UserRegistrationForm
       form = UserCreationForm(request.POST)
       # check whether it's valid: for example it verifies that password1 and password2 match
       if form.is_valid():
           form.save()
           # if you want to login the user directly after saving, use the following two lines instead, and redirect to index
           # user = form.save()
           # login(user)
           # redirect the user to login page so that after registration the user can enter the credentials
           return redirect('login')
   else:
       # Create an empty instance of Django's UserCreationForm to generate the necessary html on the template.
       form = UserCreationForm()
   return render(request, 'FitnessPage/registers.html', {'form': form})


def login_view(request):
   # this function authenticates the user based on username and password
   # AuthenticationForm is a form for logging a user in.
   # if the request method is a post
   if request.method == 'POST':
       # Plug the request.post in AuthenticationForm
       form = AuthenticationForm(data=request.POST)
       # check whether it's valid:
       if form.is_valid():
           # get the user info from the form data and login the user
           user = form.get_user()
           login(request, user)
           # redirect the user to index page
           return redirect('home')
   else:
       # Create an empty instance of Django's AuthenticationForm to generate the necessary html on the template.
       form = AuthenticationForm()
   return render(request, 'FitnessPage/login.html', {'form': form})


def logout_view(request):
   # This is the method to logout the user
   logout(request)
   # redirect the user to index page
   return redirect('home')


