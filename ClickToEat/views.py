from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import CreateUserForm
from ClickToEat.models import Client
from ClickToEat.models import Order
from ClickToEat.models import Rider
from .models import *
from .forms import *

# Create your views here.


def registrationpage_view(request):
	
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('/login')

		context = {'form':form}
		return render(request, 'registration.html', context)

def loginpage_view(request):
	
	
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def homepage_view(request):
	
	context = {}
	return render(request, "home.html", context)

def termpage_view(request):
	
	context = {}
	return render(request, "terms.html", context)

def privacypage_view(request):
	
	context = {}
	return render(request, "privacy.html", context)

def partnerpage_view(request):
	
	context = {}
	return render(request, "partner.html", context)


def aboutpage_view(request):
	context = {}
	return render(request, "about.html", context)

def featurespage_view(request):
	context = {}
	return render(request, "features.html", context)

def contactpage_view(request):
	context = {}
	return render(request, "contact.html", context)

def clientpage_view(request):
	return render(request, "client.html")

def dashboardpage_view(request):
	client = Client.objects.all()
	order = Order.objects.all()
	rider = Rider.objects.all()
	store = Store.objects.all()
	context = {
		'clients' : client,
		'orders' : order,
		'riders' : rider,
		'stores' : store
	}
	if request.method == 'POST':
		if 'btnUpdate' in request.POST:	
				print('update profile button clicked')
				cid = request.POST.get("cclient-id")			
				fname = request.POST.get("client-fname")
				lname = request.POST.get("client-lname")
				hnumber = request.POST.get("client-hnumber")
				brgy = request.POST.get("client-barangay")
				munipality = request.POST.get("client-municipality")
				prov = request.POST.get("client-province")
				city = request.POST.get("client-city")
				pnumber = request.POST.get("client-pnumber")
				email = request.POST.get("client-email")
				print(email)
				update_client = Client.objects.filter(id = cid).update(Firstname = fname, Lastname = lname, House_number = hnumber,
									  Barangay = brgy, Municipality = munipality, Province = prov, City = city, Phone_Number = pnumber, Email = email)
				print(update_client)
				print('profile updated')	
		elif 'btnDelete' in request.POST:	
			print('delete button clicked')
			cid = request.POST.get("cclient-id")
			client = Client.objects.filter(id=cid).delete()
			print('recorded deleted')

		#order
		if 'btnOrderUpdate' in request.POST:	
				print('update profile button clicked')
				oid = request.POST.get("oorder-id")			
				desc = request.POST.get("order-desc")
				orderr = request.POST.get("order-type")
				hnumber = request.POST.get("order-hnumber")
				quan = request.POST.get("order-quantity")
				print(quan)
				update_order = Order.objects.filter(id = oid).update(Order_Description = desc, Order_Type = orderr, House_number = hnumber,
									  Quantity = quan)
				print(update_order)
				print('profile updated')	
		elif 'btnOrderDelete' in request.POST:	
			print('delete button clicked')
			oid = request.POST.get("oorder-id")
			order = Order.objects.filter(id=oid).delete()
			print('recorded deleted')

		#rider
		if 'btnRiderUpdate' in request.POST:	
				print('update profile button clicked')
				rid = request.POST.get("rrider-id")			
				fname = request.POST.get("rider-fname")
				lname = request.POST.get("rider-lname")
				pnumber = request.POST.get("rider-pnumber")
				plnumber = request.POST.get("rider-plnumber")
				make = request.POST.get("rider-make")
				print(make)
				update_rider = Rider.objects.filter(id = rid).update(Firstname = fname, Lastname = lname, Phone_Number = pnumber,
									  Plate_Number = plnumber, Make = make)
				print(update_rider)
				print('profile updated')	
		elif 'btnRiderDelete' in request.POST:	
			print('delete button clicked')
			rid = request.POST.get("rrider-id")
			rider = Rider.objects.filter(id=rid).delete()
			print('recorded deleted')

		#store
		if 'btnStoreUpdate' in request.POST:	
				print('update profile button clicked')
				sid = request.POST.get("sstore-id")			
				name = request.POST.get("store-name")
				add = request.POST.get("store-address")
				tnumber = request.POST.get("store-tnumber")
				print(tnumber)
				update_store = Store.objects.filter(id = sid).update(Name = name, Address = add, Telephone_Number = tnumber)
				print(update_store)
				print('profile updated')	
		elif 'btnStoreDelete' in request.POST:	
			print('delete button clicked')
			sid = request.POST.get("sstore-id")
			store = Store.objects.filter(id=sid).delete()
			print('recorded deleted')

	return render(request, "report.html", context)



def InsertClient(request):
	if request.method== 'POST':
		if request.POST.get('Firstname') and request.POST.get('Lastname') and request.POST.get('House_number') and request.POST.get('Barangay') and request.POST.get('Municipality') and request.POST.get('Province') and request.POST.get('City') and request.POST.get('Phone_Number') and request.POST.get('Email'):
			saverecord=Client()
			saverecord.Firstname=request.POST.get('Firstname')
			saverecord.Lastname=request.POST.get('Lastname')
			saverecord.House_number=request.POST.get('House_number')
			saverecord.Barangay=request.POST.get('Barangay')
			saverecord.Municipality=request.POST.get('Municipality')
			saverecord.Province=request.POST.get('Province')
			saverecord.City=request.POST.get('City')
			saverecord.Phone_Number=request.POST.get('Phone_Number')
			saverecord.Email=request.POST.get('Email')
			saverecord.save()
			messages.success(request, "Record Saved  Successfully")
			return redirect('/report')

	else:
			return render(request, 'client.html')

def InsertOrders(request):
	if request.method== 'POST':
		if request.POST.get('Order_Description') and request.POST.get('Order_Type') and request.POST.get('House_number') and request.POST.get('Quantity'):
			saverecord=Order()
			saverecord.Order_Description=request.POST.get('Order_Description')
			saverecord.Order_Type=request.POST.get('Order_Type')
			saverecord.House_number=request.POST.get('House_number')
			saverecord.Quantity=request.POST.get('Quantity')
			saverecord.save()
			messages.success(request, "Record Saved  Successfully")
			return redirect('/report')

	else:
			return render(request, 'orders.html')

def InsertRider(request):
	if request.method== 'POST':
		if request.POST.get('Firstname') and request.POST.get('Lastname') and request.POST.get('Phone_Number') and request.POST.get('Plate_Number') and request.POST.get('Make'):
			saverecord=Rider()
			saverecord.Firstname=request.POST.get('Firstname')
			saverecord.Lastname=request.POST.get('Lastname')
			saverecord.Phone_Number=request.POST.get('Phone_Number')
			saverecord.Plate_Number=request.POST.get('Plate_Number')
			saverecord.Make=request.POST.get('Make')
			saverecord.save()
			messages.success(request, "Record Saved  Successfully")
			return redirect('/report')

	else:
			return render(request, 'rider.html')

def InsertStore(request):
	if request.method== 'POST':
		if request.POST.get('Name') and request.POST.get('Address') and request.POST.get('Telephone_Number'):
			saverecord=Store()
			saverecord.Name=request.POST.get('Name')
			saverecord.Address=request.POST.get('Address')
			saverecord.Telephone_Number=request.POST.get('Telephone_Number')
			saverecord.save()
			messages.success(request, "Record Saved  Successfully")
			return redirect('/report')

	else:
			return render(request, 'store.html')

