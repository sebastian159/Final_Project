from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('health_tips', views.health_tips, name="health_tips"),
    path('workout', views.workout, name="workout"),
    path('location', views.location, name="location"),
#    path('', views.Location, name="Location"),

    path('yelp', views.yelp, name="yelp"),
    path('goals', views.goals, name="goals"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('complete/<int:id>', views.complete, name="complete"),

    path('about_us', views.about_us, name="about_us"),
    path('covid_tips', views.covid_tips, name="covid_tips"),
    path('recipes', views.recipes, name="recipes"),

    ]