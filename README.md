# PWS Application

## Tautan Aplikasi
Aplikasi PWS yang sudah di-deploy dapat diakses melalui tautan berikut:
http://nobel-julian-shipshop.pbp.cs.ui.ac.id

## Implementasi Checklist
### Step-by-Step
1. **Membuat Proyek Django Baru**:
    - Membuat direktori baru dengan nama ship-shop
    - Menjalankan perintah `git init` untuk nanti mengunggah ship-shop ke repositori github
    - Buat dan mengaktifkan virtual environment dengan `py -m venv env` dan `env\Scripts\activate`
    - Menyiapkan dan instalasi komponen yang diperlukan atau Dependencies, dengan membuat file requirements.txt dan menjalankan perintah `pip install -r requirements.txt`
    - Membuat proyek Django bernama ship_shop dengan perintah `django-admin startproject mental_health_tracker .`
    - Konfigurasi proyek dan mencoba menjalankan server dengan mengisi ALLOWED_HOST pada setting.py dengan `"localhost", "127.0.0.1"`, menjalankan perintah 'py manage.py runserver', dan melihat apakah proyek berjalan pada http://localhost:8000/.
   
2. **Membuat Aplikasi dengan Nama `main`**:
    - Menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru bernama `main` dan muncul directori baru bernama main.

3. **Melakukan Routing pada Proyek**:
    - Menambahkan aplikasi `main` ke dalam `INSTALLED_APPS` di `settings.py`.
    - Pastikan `urls.py` di proyek utama untuk mengarahkan ke aplikasi `main`.
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')), #check this
    ]

4. **Membuat Model `Product`**:
    - Mendefinisikan model `Product` di `models.py` aplikasi `main` dengan atribut `name`, `price`, `description`, dan `quantity`. dengan detail kode sebagai berikut.
   
   ```python
   from django.db import models

   class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()

    @property
    def is_in_stock(self):
        return self.quantity > 0

5. **Membuat Fungsi pada views.py**:
    - Membuat fungsi index di views.py yang mengembalikan template HTML dengan nama aplikasi serta nama dan kelas. dengan detail kode sebagai berikut.
   
   ```python
   from django.shortcuts import render

    def show_main(request):
        context = {
            'appname' : 'SHIP SHOP',
            'name': 'Nobel Julian Bintang (2306202826)',
            'class': 'PBP F',
        }

        return render(request, "main.html", context)

6. **Membuat Routing pada urls.py pada directori main**:
    - Mengatur urls.py di aplikasi main untuk memetakan fungsi show_main dari views.py.

    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]

