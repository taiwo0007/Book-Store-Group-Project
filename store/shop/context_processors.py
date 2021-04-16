from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def managerChecker(request):
    managerCheck = False
    return {'managerCheck':managerCheck}






