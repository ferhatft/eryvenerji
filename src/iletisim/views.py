from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Contact


def contacview(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name        = form.cleaned_data['name']
            email       = form.cleaned_data['email']
            message     = form.cleaned_data['message']

# # dev
#             send_mail (
#                 name , # subject
#                 'Gönderen = ' + email + '\n' + message , #message
#                 'oref.tasarim@gmail.com', #from email
#                 ['oref.tasarim@gmail.com',], # To email    
#             )
# # live 
            
            # send_mail (
            #     name , # subject
            #     'Gönderen = ' + email + '\n' + message , #message
            #     'oref.tasarim@gmail.com', #from email
            #     ['oref.tasarim@gmail.com',], # To email    
            # )

            form.save()
            
            messages.success(request, 'Form başarılı bir şekilde gönderildi!')
            return redirect('anasayfa')
    else:
        form = ContactForm()

    pagetitle = 'İletişim'


    context = {
        'form': form,
        'pagetitle':pagetitle,
    }
    return render(request, "contact.html", context)



