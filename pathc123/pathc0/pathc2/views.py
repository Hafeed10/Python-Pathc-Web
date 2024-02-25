import json 

from django.shortcuts import render, redirect
from pathc2.models import Testimonial, Promoter, Faqs, Subscribe 
from django.http.response import HttpResponse  
from django.urls import reverse
def index(request):
    testimonials = Testimonial.objects.all() 
    promoters = Promoter.objects.all()
    rent_tracking_faqs = Faqs.objects.filter(faq_type="rent_tracking")
    new_deposit_faqs = Faqs.objects.filter(faq_type="new_deposit")
    existing_deposit_faqs = Faqs.objects.filter(faq_type="existing_deposit")

    context = {
        "name":"pathc2",
        "testimonials": testimonials,
        "promoters": promoters,
        "rent_tracking_faqs": rent_tracking_faqs,
        "new_deposit_faqs": new_deposit_faqs,
        "existing_deposit_faqs": existing_deposit_faqs
        
    }
    return render(request, 'index.html', context=context)



def subscribe(request):
    email = request.POST.get('email')
    Subscribe.objects.create(email=email)

    # response_data = {
    #     "status": "success",
    #     "message": "Your subscription has been successfully"
    # }
    return redirect(reverse("pathc2:pathc2"))