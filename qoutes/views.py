from django.shortcuts import render,redirect
from .models import stock
from django.contrib import messages
from .forms import Stockform

# Create your views here.
def home(request):
	import requests
	import json
	# pk_4b920ec599354bdb9e1e36962ad9599c
	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_4b920ec599354bdb9e1e36962ad9599c")
		
		try:
			api= json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		return render(request,'home.html',{'api': api })
	else:
		return render(request, 'home.html' ,{'ticker': "Enter some ticker"})

def about(request):
	return render(request,"about.html",{})

def add_stock(request):
	import requests
	import json
	if request.method == 'POST':
		form = Stockform(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request,"Stock has been added")
			return redirect('addstock')
	else:
		ticker = stock.objects.all()
		output=[]
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_4b920ec599354bdb9e1e36962ad9599c")
			try:
				api= json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."
		return render(request,"add_stock.html",{'ticker':ticker,'output':output})


def delete(request, stock_id):
	item = stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request,"Stock has been deleted!")
	return redirect('addstock')

def deletes(request, stock_id):
	item = stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request,"Stock has been deleted!")
	return redirect('deletestock')

def delete_stock(request):
	ticker = stock.objects.all()
	return render(request,"delete_stock.html",{'ticker':ticker})
