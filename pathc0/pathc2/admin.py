from django.contrib import admin
from pathc2.models import Testimonial, Promoter, Faqs, Subscribe

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'designation', 'description']

admin.site.register(Testimonial, TestimonialAdmin)


class PromoterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']

admin.site.register(Promoter, PromoterAdmin)


class FaqsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'faq_type']

admin.site.register(Faqs, FaqsAdmin)




admin.site.register(Subscribe)
