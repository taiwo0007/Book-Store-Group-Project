from .models import Category
from accounts.models import UserProfile
from vouchers.models import Voucher


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def managerChecker(request):
    managerCheck = False
    return {'managerCheck':managerCheck}

def profileImage(request):

    if request.user.is_authenticated:
        profile = UserProfile.objects.filter(user=request.user)
    else:
        profile = {}
    return {'profile':profile}

def annouceFunction(request):
    
   
    anouncemnets = Voucher.objects.filter(anounce=True)
    anouncemnet = anouncemnets.last()
    

    return{'anouncemnets':anouncemnets}
    


    








