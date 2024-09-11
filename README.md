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
    - Mengatur urls.py di aplikasi main untuk memetakan fungsi show_main dari views.py. dengan detail kode sebagai berikut.

    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]

7. **Melakukan Deployment ke PWS**:
    - Mengakses PWS https://pbp.cs.ui.ac.id/
    - Buat proyek baru, dan simpan credetials
    - Tambahkan ALLOWED_HOST pada setting.py dengan URL deployment PWS nobel-julian-shipshop.pbp.cs.ui.ac.id
    - Lalu git add, commit, dan push baik ke PWS maupun github


## Bagan Request Client ke Web Aplikasi Django

![Bagan Django](https://github.com/user-attachments/assets/e365b002-4edc-4e59-8eeb-24e037d4f65e)

Penjelasan Bagan:
- client: Mengirimkan request ke server.
- urls.py: Menerima request dan menentukan view mana yang akan dipanggil berdasarkan URL.
- views.py: Mengambil data yang diperlukan dari model dan memprosesnya.
- models.py: Berinteraksi dengan Database untuk mengambil atau menyimpan data.
- main.html: Menggunakan data dari view untuk menghasilkan HTML yang akan dikirim kembali ke client.

## Fungsi Git dalam Pengembangan Perangkat Lunak

Terdapat beberapa fungsi utama yaitu:
- Version Control: Melacak setiap perubahan yang dilakukan pada kode, jadi dapat diketahui dengan pasti kapan perubahan terjadi dan memungkinkan developer untuk kembali ke versi sebelumnya jika diperlukan.
- Collaboration: Untuk sekarang fungsi ini belum digunakan saat pengerjaan tugas 2 ini, akan tetapi nanti akan memungkinkan beberapa ataupun banyak developer untuk bekerja pada proyek yang sama secara bersamaan tanpa konflik (semoga tugas-tugas selanjutnya berlangsung tanpa konflik).
- Branching and Merging: Memungkinkan developer untuk membuat cabang (branch) dari kode utama untuk mengembangkan fitur baru atau memperbaiki bug, dan kemudian menggabungkannya kembali (merge) ke cabang utama setelah selesai.

## Mengapa Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak

Karena Django framework web yang menggunakan bahasa pemrograman Python, kenapa Python digunakan sebab bahasa pemrograman ini terkenal akan kesederhanaanya, kemudahan pembacaan kode, dan kemampuannya untuk menangani berbagai tugas dengan efisien. Django juga menyediakan fitur bawaan yang memudahkan pengembangan, serta komunitas Django yang besar sehingga banyak sumber-sumber yang dapat dimanfaatkan pemula.

## Mengapa model pada Django disebut sebagai ORM

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena beberapa alasan utama. Pertama, ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa perlu menulis query SQL secara langsung. Ini membuat kode lebih mudah dibaca dan dipelihara. ORM memetakan tabel dalam database ke kelas Python, dan baris dalam tabel ke objek dari kelas tersebut. Setiap atribut dalam kelas Python sesuai dengan kolom dalam tabel database. Selain itu, ORM menyediakan metode untuk membuat, membaca, memperbarui, dan menghapus data dalam database dengan cara yang lebih intuitif dan aman. Misalnya, Anda bisa menggunakan metode seperti `.save()`, `.filter()`, dan `.delete()` untuk mengelola data. Dengan menggunakan ORM, risiko kesalahan seperti SQL Injection dapat diminimalkan karena ORM secara otomatis menangani sanitasi input. Terakhir, ORM membuat aplikasi lebih portabel karena Anda bisa mengganti backend database tanpa perlu mengubah kode Python secara signifikan. Django ORM mendukung berbagai database seperti SQLite, PostgreSQL, MySQL, dan Oracle. Dengan ORM, pengembangan aplikasi menjadi lebih efisien dan aman, serta memudahkan pengelolaan data dalam database.