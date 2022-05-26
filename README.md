# upload-file-example-Django
Only one app example for upload file without major setting files

It is a simple app example for uploading file with Django framwork.

You can start with it to new a upload app.
```
python manage.py startapp upload
```

This example only contain below python, html and media file.
+ urls.py (url for user link)
+ views.py (what Django would do behind the UI)
+ forms.py (the tempalte for forms needs)
+ upload.html (UI design for upload page)
+ result.html (UI design to show your result)

The base.html is containd bootstrap 5 import and you could create one for your needs.

```python
urls.py
app_name = 'upload'

urlpatterns = [
    path('upload_file/', views.upload_file, name='upload_file'),
]
```

```python
view.py

def handle_uploaded_file(f, current_time):
...

def upload_file(request):
...
    return render(request, 'upload/upload.html', {'form': form})

def result(request, current_time):
...
    return render(request, 'upload/result.html', context=context)
```

```python
forms.py
class UploadFileForm(forms.Form):
    file = forms.FileField(label='file', widget=forms.FileInput(attrs={'class':'form-control'}))
```
```html
upload.html
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    <div class="custom-file">
        {{ form.file.errors }}
        <label for="file" class="form-label">File input example</label>
        {{ form.file }}
        </input>            
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

```html
result.html
{{index|safe}}
```