from django.shortcuts import render,HttpResponse, redirect ,get_object_or_404
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import GroceryList, Item
from .forms import GroceryListForm, ItemForm
from django.http import HttpResponseNotAllowed


# Create your views here.

# def index(request):
    
#     return HttpResponse("this is homepage.")
def index(request):
    # context={
    # 'x':"Hi"
    # }
    return render(request, 'index.html')
def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact= Contact(name=name, email=email, phone =phone , desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Thank you for contacting us!')
    return render(request, 'contactus.html')

def about(request):
    return render(request,'aboutus.html')

def mylist(request):

    return render(request,'list_detail.html')

def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pswd1=request.POST.get('password')
        user=authenticate(request,username=uname,password=pswd1)
        if user is not None:
            auth_login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request,'Invalid username or password')
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pswd1=request.POST.get('password1')
        pswd2=request.POST.get('password2')
        if pswd1!=pswd2:
            messages.warning(request,'Password does not match with confirm password!')
            return redirect('signup')
            
        else:
            my_user=User.objects.create_user(uname,email,pswd1)
            my_user.save()
            return redirect('login')


    return render(request,'signup.html')


# Dashboard view to list all grocery lists for the logged-in user
def dashboard(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    lists = GroceryList.objects.filter(user=request.user)
    form = GroceryListForm()
    return render(request, 'dashboard.html', {'lists': lists, 'form': form})

# Detail view for a specific grocery list and its items
def list_detail(request, list_id):
    grocery_list = get_object_or_404(GroceryList, id=list_id, user=request.user)
    items = grocery_list.items.all()
    return render(request, 'list_detail.html', {'list': grocery_list, 'items': items})

# Create a new grocery list
def create_list(request):
    if request.method == 'POST':
        form = GroceryListForm(request.POST)
        if form.is_valid():
            grocery_list = form.save(commit=False)
            grocery_list.user = request.user  # Associate with current user
            grocery_list.save()
            return redirect('dashboard')
    else:
        form = GroceryListForm()
    return render(request, 'dashboard.html', {'form': form})
# Add a new item to a grocery list

def add_item(request, list_id):
    grocery_list = GroceryList.objects.get(id=list_id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            Item.objects.create(name=name, quantity=quantity, grocery_list=grocery_list)
            return redirect('list_detail', list_id=list_id)
    else:
        form = ItemForm()
    return render(request, 'list_detail.html', {'form': form})

# Delete an item from a grocery list
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, grocery_list__user=request.user)
    list_id = item.grocery_list.id
    item.delete()
    return redirect('list_detail', list_id=list_id)

# def edit_item(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     if request.method == 'POST':
#         item.name = request.POST.get('name')
#         item.quantity = request.POST.get('quantity')
#         item.save()
#         return redirect('list_detail', list_id=item.grocery_list.id)
#     return render(request, 'list_detail.html', {'item': item})



def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list_detail', list_id=item.grocery_list.id)
    else:
        form = ItemForm(instance=item)
    return render(request, 'list_detail.html', {'form': form})

# @login_required
# def dashboard(request):
#     lists = GroceryList.objects.filter(user=request.user)
#     form = GroceryListForm()
#     return render(request, 'dashboard.html', {'lists': lists, 'form': form})

# @login_required
# def list_detail(request, list_id):
#     grocery_list = get_object_or_404(GroceryList, id=list_id, user=request.user)
#     items = Item.objects.filter(grocery_list=grocery_list)
#     return render(request, 'list_detail.html', {'list': grocery_list, 'items': items})

# @login_required
# def create_list(request):
#     if request.method == 'POST':
#         form = GroceryListForm(request.POST)
#         if form.is_valid():
#             grocery_list = form.save(commit=False)
#             grocery_list.user = request.user
#             grocery_list.save()
#             return redirect('dashboard')
#     return redirect('dashboard')

# @login_required


# def add_item(request, list_id):
#     if request.method == 'POST':
#         grocery_list = get_object_or_404(GroceryList, id=list_id)
#         name = request.POST.get('name')
#         quantity = request.POST.get('quantity')
#         if name and quantity:
#             Item.objects.create(name=name, quantity=quantity, grocery_list=grocery_list)
#         return redirect('list_detail', list_id=list_id)
#     return redirect('list_detail', list_id=list_id)


# @login_required
# def delete_item(request, item_id):
#     item = get_object_or_404(Item, id=item_id, grocery_list__user=request.user)
#     item.delete()
#     return redirect('list_detail', list_id=item.grocery_list.id)

# @login_required
# def edit_item(request, item_id):
#     item = get_object_or_404(Item, id=item_id, grocery_list__user=request.user)
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         item.name = data.get('name', item.name)
#         item.quantity = data.get('quantity', item.quantity)
#         item.save()
#     return JsonResponse({'success': True})
