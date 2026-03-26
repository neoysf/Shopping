from rest_framework import viewsets
from .models import Product, ContactMessage, SocialLinks, UserEmail, SiteInfo, Big_slider, Small_slider, Categories, Comment
from .serializers import ProductSerializer, ContactMessageSerializer, SocialLinksSerializer,UserEmailSerializer, SiteInfoSerializer, BigSliderSerializer, SmallSliderSerializer, CategoriesSerializer, CommentSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

class SocialLinksViewSet(viewsets.ModelViewSet):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer

class UserEmailViewSet(viewsets.ModelViewSet):
    queryset = UserEmail.objects.all()
    serializer_class = UserEmailSerializer

class SiteInfoViewSet(viewsets.ModelViewSet):
    queryset = SiteInfo.objects.all()
    serializer_class = SiteInfoSerializer

class BigSliderViewSet(viewsets.ModelViewSet):
    queryset = Big_slider.objects.all()
    serializer_class = BigSliderSerializer

class SmallSliderViewSet(viewsets.ModelViewSet):
    queryset = Small_slider.objects.all()
    serializer_class = SmallSliderSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# from django.core.mail import send_mail
# from django.shortcuts import render, redirect
# from .forms import ContactForm, ProductForm, EmailForm
# from django.contrib import messages
# from .models import Product, Big_slider, Small_slider, Categories, Comment
# from django.conf import settings
# from django.db.models import Q
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.core.paginator import Paginator
#
# def home_view(request):
#     big_sliders = Big_slider.objects.filter(is_activate=True).order_by('-created_date')
#     small_sliders = Small_slider.objects.filter(is_activate=True).order_by('-created_date')
#     categories = Categories.objects.filter()
#
#     context = {
#         'big_sliders': big_sliders,
#         'small_sliders': small_sliders,
#         'categories': categories
#     }
#     return render(request, 'index.html', context)
#
#
# def product_list(request):
#     products = Product.objects.filter(is_active=True)
#
#     paginator = Paginator(products, 6)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'shop.html', {'page_obj': page_obj})
#
# def shopdetail_view(request):
#     products = Product.objects.all()
#     comments = Comment.objects.all()
#
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")
#         Comment.objects.create(name=name, email=email, message=message)
#         return redirect("core:detail")
#
#     return render(request, "detail.html", {"products": products, "comments": comments})
#
#
# def contact_view(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             send_mail(
#                 'Yeni Əlaqə Mesajı',
#                 'Siz yeni mesaj aldınız.',
#                 settings.EMAIL_HOST_USER,
#                 ['nerminyusifova1100@example.com']
#             )
#             messages.success(request, "Mesajınız uğurla göndərildi!")
#             return redirect("core:contact")
#     else:
#         form = ContactForm()
#     return render(request, "contact.html", {'form': form})
#
#
# def footer_email_view(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'E-poçt uğurla əlavə edildi!')
#             return redirect('core:footer_email')
#     else:
#         form = EmailForm()
#
#     return render(request, 'base.html', {'form': form})
#
#
# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('core:shop')
#     else:
#         form = ProductForm()
#     return render(request, 'add_product.html', {'form': form})
#
# def submit_comment(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         review = request.POST.get("review")
#
#         Comment.objects.create(name=name, email=email, review=review)
#         return redirect("success_page")
#
#     return render(request, "comment_form.html")
#
# def discount_offers(request):
#     return render(request, 'yeniteklif_readmore.html')
#
# def search_view(request):
#     query = request.GET.get('q')
#     print(query)
#     results = []
#     if query:
#         results = Product.objects.filter(
#             Q(name__icontains=query) | Q(description__icontains=query),
#             is_active=True
#         )
#     context = {
#         'query': query,
#         'results': results
#     }
#     return render(request, 'search_results.html', context)
#
#
#
# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         if password1 != password2:
#             messages.error(request, 'Şifrələr uyğun deyil')
#             return redirect('register')
#
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'İstifadəçi adı artıq mövcuddur')
#             return redirect('register')
#
#         user = User.objects.create_user(username=username, email=email, password=password1)
#         user.save()
#         messages.success(request, 'Uğurla qeydiyyatdan keçdiniz. Giriş edə bilərsiniz.')
#         return redirect('login')
#     return render(request, 'register.html')
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('core:home')
#         else:
#             messages.error(request, 'İstifadəçi adı və ya şifrə yalnışdır')
#             return redirect('core:login')
#     return render(request, 'login.html')
#
# def logout_view(request):
#     logout(request)
#     return redirect('core:login')
