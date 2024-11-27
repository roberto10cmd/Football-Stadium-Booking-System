from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.http import JsonResponse
from .forms import StadiumForm, EquipmentForm,CreateUseForm
from .models import Stadium
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='user_login')
def About(request):
    return render(request,'about.html')

def AdminPage(request):
    return render(request,'adminpage.html')


@login_required(login_url='user_login')
def all_stadiums(request):
    return render(request,'all_stadiums.html')

@login_required(login_url='user_login')
def Home(request):
    return render(request,'home.html')

@login_required(login_url='user_login')
def Contact(request):
    return render(request,'contact.html')

@login_required(login_url='user_login')
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')


def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
            if request.method == "POST":
                u = request.POST.get('username')
                p = request.POST.get('password')
                user = authenticate(username=u, password=p)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                     messages.info(request,'Username or Password is incorrect!')
            
    context={}
    return render(request,'user_login.html',context)

@login_required(login_url='user_login')
def Logout_user(request):
    logout(request)
    return redirect('user_login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUseForm()
        if request.method == 'POST':
            form = CreateUseForm(request.POST)
            if form.is_valid():
                user = form.save()
                Customer.objects.create(
            user=user,
            firstname=form.cleaned_data['firstname'],
            lastname=form.cleaned_data['lastname'],
            address=form.cleaned_data['address'],
            phone=form.cleaned_data['phone']
            # alte câmpuri necesare
        )
                messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
                return redirect('user_login')
        context = {'form': form}
        return render(request, 'register.html', context)


def add_stadium(request):
    if request.method == 'POST':
        form = StadiumForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Stadium added successfully!"})
        else:
            return JsonResponse({"error": "Invalid data"}, status=400)
        
def update_stadium(request):
    if not request.user.is_staff:
        return HttpResponse('Unauthorized', status=401)

    if request.method == 'POST':
        stadium_id = request.POST.get('stadium_id')
        stadium = get_object_or_404(Stadium, id=stadium_id)
        form = StadiumForm(request.POST, instance=stadium)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Stadium updated successfully"})
        else:
            return JsonResponse({"error": form.errors}, status=400)



def delete_stadium(request, id):
    if not request.user.is_staff:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    stadium = get_object_or_404(Stadium, id=id)
    stadium.delete()
    return JsonResponse({'message': 'Stadium deleted successfully'})

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Equipment added successfully!"})
        else:
            return JsonResponse({"error": "Invalid data"}, status=400)

def update_equipment(request):
    if not request.user.is_staff:
        return HttpResponse('Unauthorized',status=401)
    
    if request.method=='POST':
        equipment_id=request.POST.get('equipment_id')
        equipment = get_object_or_404(Equipment,id=equipment_id)
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Equipment updated successfully"})
        else:
            return JsonResponse({"error": form.errors}, status=400)
        
def delete_equipment(request, id):
    if not request.user.is_staff:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    # Schimbă de la Customer la Equipment
    equipment = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        equipment.delete()
        return JsonResponse({'message': 'Equipment deleted successfully'})

def add_customer(request):
    if not request.user.is_staff:
        return HttpResponse('Unauthorized', status=401)

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Customer added successfully!"})
        else:
            return JsonResponse({"error": form.errors}, status=400)
    else:
        form = CustomerForm()
        return render(request, 'add_customer.html', {'form': form})

def update_customer(request):
    print("Request received: ", request.POST)  # Debug: vezi datele primite
    if not request.user.is_staff:
        return HttpResponse('Unauthorized', status=401)

    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        print("Customer ID: ", customer_id)  # Debug: vezi ID-ul clientului

        customer = get_object_or_404(Customer, id=customer_id)
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Customer updated successfully"})
        else:
            print("Form errors: ", form.errors)  # Debug: vezi erorile formularului
            return JsonResponse({"error": form.errors}, status=400)

def delete_customer(request, id):
    if not request.user.is_staff:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.delete()
        return JsonResponse({'message': 'Customer deleted successfully'})


def stadium_list(request):
    stadia = Stadium.objects.all().values('id', 'name', 'location', 'description')
    return JsonResponse(list(stadia), safe=False)

def equipment_list(request):
    equipment = Equipment.objects.all().values('id', 'name', 'description')
    return JsonResponse(list(equipment), safe=False)

def customer_list(request):
    customers = Customer.objects.all().values(
        'id', 'user__username', 'firstname', 'lastname', 
        'wallet_balance', 'address', 'phone'
    )
    return JsonResponse(list(customers), safe=False)

