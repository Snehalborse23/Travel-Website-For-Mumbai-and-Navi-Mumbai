from django.shortcuts import render
from django.http import  HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import  Location, Review
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg



# Create your views here.
def about(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/about.html')

def contact(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/contact.html')

def index(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/index.html')

def locations(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/locations.html')

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
    

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password1"]
        confirmation = request.POST["password2"]
        phone_number = request.POST["phone_number"]
        if password != confirmation:
            return render(request, "ANYWHEREEVERYWHERE/html/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            User = get_user_model()
            user = User.objects.create_user(username, email, password, phone_number=phone_number)
            user.save()
            print(user)
            print("User created.")
        except IntegrityError:
            print("Username already taken.")
            return render(request, "ANYWHEREEVERYWHERE/html/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "ANYWHEREEVERYWHERE/html/register.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "ANYWHEREEVERYWHERE/html/login.html")
    
@login_required
def rate(request):
        stars=3
        # location = Location.objects.get(pk=location_id)
        rating = Rating(user=request.user, rating=stars, feedback= "hey this was ggood")
        rating.save()
        return JsonResponse({'success': True})

def bandra(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/bandra.html')

def nerul(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/nerul.html')

def mumbai(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/mumbai.html')

'''def bandra(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/bandra.html')'''

def vashi(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/vashi.html')

def kharghar(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/kharghar.html')

def westernmumbai(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/westernmumbai.html')

def kurla(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/kurla.html')

def southmumbai(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/southmumbai.html')

def uran(request):
    return render(request, 'ANYWHEREEVERYWHERE/html/uran.html')

@csrf_exempt
def save_rating(request,location,rating):
        print(location, rating)
        # user = request.user
        # location, created = Location.objects.get_or_create(name=location)
        # rating_obj, created = Rating.objects.get_or_create(location=location, user=user)
        # rating_obj.rating = rating
        # rating_obj.save()
        # # avg_rating = Rating.objects.filter(location=location).aggregate(avg_rating=Avg('rating'))['avg_rating']
        # return JsonResponse({'avg_rating': avg_rating})

@login_required
def save_review(request, location, review, rating):
    user = request.user
    if rating < 0 or rating > 5:
        return JsonResponse({'success': False, 'error': 'Rating should be between 0 and 5.'})
    
    review_exists = Review.objects.filter(user=user, review_text=review).exists()
    
    if review_exists:
        return JsonResponse({'success': False, 'error': 'You have already submitted a review for this location.'})
    
    review = Review(location=location, rating=rating, review_text=review, user=user)
    review.save()
    return JsonResponse({'success': True})


