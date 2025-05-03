from django.shortcuts import render
from cars.models import Car
from users.models import CustomUser, Comment

# Create your views here.
def index(request):
    cars = Car.objects.all()
    comments = Comment.objects.filter(
        user__is_active = True,
        user__is_superuser = False,
        user__is_staff = False
    )
    users = CustomUser.objects.filter(
        is_active = True,
        is_superuser = False,
        is_staff = True
    )
    return render(request=request,
                template_name='index.html', 
                context={
                    'cars':cars,
                    'users':users,
                    'comments':comments
                    },
                )