from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.
def func1(request):
    return render(request, 'blog/index.html', {})
def func2(request):
    return render(request, 'blog/index1.html', {})
def func3(request):
    return render(request, 'blog/index2.html', {})
def add(request):
    return HttpResponse("Added")

def account_logout(request):
      """
      Logout and redirect to the main page.
      """
      logout(request)
      return redirect('/shop3')

@csrf_exempt
def paypal_success(request):
      """
      Tell user we got the payment.
      """
      return HttpResponse("Money is mine. Thanks.")
  
  
@login_required
def paypal_pay(request):
      """
      Page where we ask user to pay with paypal.
      """
      paypal_dict = {
          "business": "ruslan_cimbalyuk-facilitator@mail.ru",
          "amount": "1000.00",
          "currency_code": "RUB",
          "item_name": "T-Shirt",
          "invoice": "INV-00312",
          "notify_url": reverse('paypal-ipn'),
          "return_url": "http://localhost:8000/payment/success/",
          "cancel_return": "http://localhost:8000/payment/cart/",
          "custom": str(request.user.id)
      }
  
      # Create the instance.
      form = PayPalPaymentsForm(initial=paypal_dict)
      context = {"form": form, "paypal_dict": paypal_dict}
      return render(request, "blog/payment.html", context) 
