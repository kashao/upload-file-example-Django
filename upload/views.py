from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import time
from numpy import genfromtxt
from django.http import JsonResponse, HttpResponse

# Imaginary function to handle an uploaded file.
def handle_uploaded_file(f, current_time):
    with open('media/upload/sample/'+current_time+'.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        print (current_time)
        if form.is_valid():  
            filename = str(request.FILES['file'])
            handle_uploaded_file(request.FILES['file'], current_time)
            if filename == 'sample.csv':
                try:
                    return result(request, current_time)
                except:
                    return render(request, 'upload/upload.html', {'form': form})
            else:
                form = UploadFileForm()
                return render(request, 'upload/upload.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})

def result(request, current_time):
    """ view function for sales app """
    my_data = genfromtxt('media/upload/sample/'+ current_time +'.csv', delimiter=',')
    #...
    context = {"index": current_time}
    return render(request, 'upload/result.html', context=context)