from .models import Category
from accounts.models import UserProfile

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def managerChecker(request):
    managerCheck = False
    return {'managerCheck':managerCheck}

def profileImage(request):
    profile = UserProfile.objects.filter()
    return dict(profile=profile)







