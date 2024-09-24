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
    - Membuat proyek Django bernama ship_shop dengan perintah `django-admin startproject ship_shop .`
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

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery penting untuk memastikan bahwa data dapat diakses dan digunakan oleh berbagai komponen dalam platform, termasuk frontend, backend, dan layanan pihak ketiga. Ini memungkinkan integrasi yang mulus dan pengalaman pengguna yang lebih baik.

## Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON lebih baik dalam hal kesederhanaan dan efisiensi. JSON lebih populer karena lebih mudah dibaca dan ditulis oleh manusia, serta lebih ringan dan cepat diproses oleh mesin dibandingkan XML.

## Fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang telah ditentukan. Kita membutuhkan method ini untuk memastikan bahwa data yang disimpan ke dalam database adalah valid dan tidak menyebabkan error.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

CSRF token digunakan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Jika kita tidak menambahkan CSRF token, penyerang dapat mengirimkan permintaan palsu atas nama pengguna yang sah, yang dapat menyebabkan tindakan yang tidak diinginkan seperti perubahan data atau pencurian informasi.

## Implementasi Checklist
1. Buatlah folder bernama templates di direktori utama (root folder) dan buat file HTML baru dengan nama base.html. File base.html ini akan berfungsi sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya dalam proyek.
2. Mengisi settings.py pada direktori proyek dengan `'DIRS': [BASE_DIR / 'templates'],` agar django mencari template pada direktori templates
3. Jadikan base.html template utama pada template lainnya
4. Mengubah Primary Key menjadi UUID pada object Product `id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)`
5. Dan migrasi modelnya
6. Membuat forms.py didalam direktori main agar dapat menerima data Product baru, sebagai berikut.
    ```python
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description", "quantity"]
7. Mengimpor beberapa fungsi dan kelas penting dari Django dan aplikasi main. Fungsi render dan redirect dari django.shortcuts digunakan untuk merender template HTML dan mengarahkan pengguna ke URL lain. ProductForm dari main.forms adalah formulir yang digunakan untuk membuat atau memperbarui objek Product, sementara Product dari main.models adalah model yang mewakili tabel dalam basis data yang menyimpan informasi produk.
    ```python
    from django.shortcuts import render, redirect
    from main.forms import ProductForm
    from main.models import Product
8. Lalu membuat Fungsi create_product pada views.py yang menangani pembuatan produk baru dengan menampilkan formulir ProductForm, memvalidasi data yang dikirimkan melalui metode POST, menyimpan data ke dalam basis data jika valid, dan mengarahkan pengguna ke halaman utama setelah operasi berhasil. Jika formulir tidak valid atau metode bukan POST, fungsi ini akan merender template create_product.html dengan formulir yang ada. sebagai berikut.
    ```python
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product.html", context)
9. Mengubah fungsi show_main pada file yang sama, dengan menambahkan daftar product, sebagai berikut.
    ```python
    def show_main(request):
        product_ship = Product.objects.all()

        context = {
            'appname': 'Ship Shop',
            'name': 'Nobel Julian Bintang',
            'class': 'PBP F',
            'product': product_ship
        }

        return render(request, "main.html", context)
10. Import fungsi create_product ke urls.py pada direktori main, sebagai berikut `from main.views import show_main, create_product`
11. Menambahkan path URL ke variabel urlpatterns yang ada pada urls.py agar bisa mengakses fungsi yang telah diimport, sebagai berikut `path('create-mood-entry', create_product, name='create_product'),`
12. Buat berkas HTML `create_product.html` pada direktori main/templates, isi sebagai berikut
    ```html
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
13. Menambahkan isi main.html dengan daftar product dan tombol add new product yang redirect ke halaman create_product, sebagai berikut
    ```html
    {% extends 'base.html' %}
    {% block content %}

    <h1>{{ appname }}</h1>

    <h4>Name: {{ name }}</h4>
    <h4>Class: {{ class }}</h4>

    {% if not product %}
    <p>Belum ada product pada ship shop.</p>
    {% else %}
    <table class="table table-striped">
    <thead class="thead-dark">
        <tr>
        <th>Product Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Quantity</th>
        </tr>
    </thead>
    <tbody>
        {% for product_ship in product %}
        <tr>
        <td>{{ product_ship.name }}</td>
        <td>{{ product_ship.price }}</td>
        <td>{{ product_ship.description }}</td>
        <td>{{ product_ship.quantity }}</td>
        </tr>
        {% endfor %}
    </tbody>
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:create_product' %}">
    <button class="btn btn-primary">Add New Product</button>
    </a>

    {% endblock content %}
14. Mengembalikan Data dalam bentuk XML dan JSON
    - import HttpResponse dan Serializer pada views.py, sebagai berikut
        ```python
        from django.http import HttpResponse
        from django.core import serializers
    - buat fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id pada views.py. sebagai berikut
        ```python
        def show_xml(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        def show_json(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

        def show_xml_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        def show_json_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    - import semua fungsi ke urls.py
        ```python
        from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
    - tambahkan semua path url ke urlpatterns, sehingga isi urlpatternsnya sebagai berikut
        ```python
        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product', create_product, name='create_product'),
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
            path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        ]
    - cek semua berjalan dengan baik

## Mengakses URL
1. /xml
![Screenshot 2024-09-18 091053](https://github.com/user-attachments/assets/4d9343f1-c162-41bc-a850-d7f6d7616ef9)
2. /json
![Screenshot 2024-09-18 091014](https://github.com/user-attachments/assets/408be6de-e2eb-4f51-b818-9aa21972c257)
3. /xml/:id
![Screenshot 2024-09-18 103306](https://github.com/user-attachments/assets/276be38f-e83c-43b4-ab49-81743a7c7d33)
4. /json/:id
![Screenshot 2024-09-18 103323](https://github.com/user-attachments/assets/67006c70-8df2-4598-9f4f-ff80351dbaec)

## Perbedaan antara HttpResponseRedirect() dan redirect()
1. HttpResponseRedirect(): Mengembalikan objek HttpResponse yang mengarahkan ke URL tertentu. Digunakan untuk mengarahkan pengguna ke halaman lain.
2. redirect(): Fungsi shortcut yang mengembalikan HttpResponseRedirect ke URL yang diberikan. Lebih mudah digunakan karena dapat menerima nama URL atau objek model.

## Cara Kerja Penghubungan Model Product dengan User
Penghubungan dilakukan dengan menambahkan ForeignKey pada model Product yang mengacu pada model User. Ini memungkinkan setiap produk terkait dengan pengguna tertentu.

## Perbedaan antara Authentication dan Authorization
1. Authentication: Proses verifikasi identitas pengguna (misalnya, melalui username dan password).
2. Authorization: Proses menentukan hak akses pengguna setelah mereka terautentikasi.
Saat login, Django memverifikasi kredensial pengguna (authentication) dan kemudian menentukan hak akses mereka (authorization).

## Bagaimana Django Mengingat Pengguna yang Telah Login
Django menggunakan sesi dan cookies untuk mengingat pengguna yang telah login. Saat pengguna login, Django membuat sesi dan menyimpan ID sesi dalam cookie di browser pengguna. Cookie ini kemudian digunakan untuk mengidentifikasi pengguna pada setiap permintaan berikutnya.

Cookies dapat digunakan untuk menyimpan preferensi pengguna, melacak aktivitas, dan mengelola sesi. Tidak semua cookies aman, cookies harus dienkripsi dan memiliki atribut keamanan.

## Implementasi Checklist Secara Step-by-Step
Berikut adalah versi yang lebih singkat dengan penjelasan dan mengganti `mood_entry` menjadi `product`:

**Langkah Membuat Fungsi Registrasi, Login, Logout, dan Pembatasan Akses**

1. **Aktifkan Virtual Environment**.
2. Buka *views.py* di folder *main*, tambahkan:
   ```python
   from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
   from django.contrib import messages
   from django.contrib.auth import authenticate, login, logout
   ```
   - **Penjelasan**: Mengimpor form bawaan Django untuk pembuatan akun, login, dan pesan notifikasi.

3. **Fungsi Registrasi**:
   ```python
   def register(request):
       form = UserCreationForm()
       if request.method == "POST" and form.is_valid():
           form.save()
           messages.success(request, 'Akun berhasil dibuat!')
           return redirect('main:login')
       return render(request, 'register.html', {'form': form})
   ```
   - **Penjelasan**: Fungsi ini menampilkan form registrasi dan membuat akun baru setelah validasi form.

4. **Template `register.html`**:
   - Buat file baru dengan form registrasi:
   ```html
   <h1>Register</h1>
   <form method="POST">{% csrf_token %}{{ form.as_table }}<input type="submit" value="Daftar"></form>
   ```

5. **URL**: Di *urls.py*, tambahkan:
   ```python
   path('register/', register, name='register')
   ```
   - **Penjelasan**: Menambahkan URL untuk akses halaman registrasi.

6. **Fungsi Login**:
   ```python
   def login_user(request):
       form = AuthenticationForm(data=request.POST or None)
       if form.is_valid():
           login(request, form.get_user())
           return redirect('main:show_main')
       return render(request, 'login.html', {'form': form})
   ```
   - **Penjelasan**: Form login yang memvalidasi pengguna dan melakukan autentikasi.

7. **Template `login.html`**:
   - Buat file untuk form login:
   ```html
   <h1>Login</h1>
   <form method="POST">{% csrf_token %}{{ form.as_table }}<input type="submit" value="Login"></form>
   <a href="{% url 'main:register' %}">Register</a>
   ```

8. **URL**: Di *urls.py*, tambahkan:
   ```python
   path('login/', login_user, name='login')
   ```

9. **Logout**: 
   - Tambahkan fungsi di *views.py*:
   ```python
   def logout_user(request):
       logout(request)
       return redirect('main:login')
   ```
   - Di *urls.py*, tambahkan:
   ```python
   path('logout/', logout_user, name='logout')
   ```
   - Di *main.html*, tambahkan tombol:
   ```html
   <a href="{% url 'main:logout' %}"><button>Logout</button></a>
   ```
   - **Penjelasan**: Fungsi logout untuk keluar dari sesi pengguna.

10. **Restriksi Halaman Utama**: Tambahkan:
    ```python
    from django.contrib.auth.decorators import login_required

    @login_required(login_url='/login')
    def show_main(request):
        ...
    ```
    - **Penjelasan**: Menambahkan pembatasan akses agar hanya pengguna yang login bisa mengakses halaman utama.

11. **Cookies Last Login**: Modifikasi fungsi *login_user*:
    ```python
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
    ```
    - Tambahkan di *show_main*:
    ```python
    'last_login': request.COOKIES.get('last_login', 'Tidak ada data login')
    ```
    - **Penjelasan**: Menyimpan informasi terakhir kali pengguna login di *cookies* dan menampilkannya di halaman utama.

12. **Hubungkan Model Product dengan User**:
    - Di *models.py*, tambahkan:
    ```python
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```
    - **Penjelasan**: Setiap `product` akan dikaitkan dengan pengguna yang membuatnya.
   
    - Modifikasi *create_product*:
    ```python
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main:show_main')

        return render(request, "create_product.html", {'form': form})
    ```
    - **Penjelasan**: Setiap produk baru yang dibuat akan otomatis dikaitkan dengan pengguna yang sedang login.

13. **Filter Produk per Pengguna**: Ubah value dari *product* di *show_main*:
    ```python
    def show_main(request):
        products = Product.objects.filter(user=request.user)

        context = {
            'appname': 'Ship Shop',
            'name': request.user.username,
            'class': 'PBP F',
            'product': product_ship,
            'last_login': request.COOKIES['last_login'],
        }
        return render(request, "main.html", context)
    ```
    - **Penjelasan**: Menampilkan hanya produk yang dibuat oleh pengguna yang sedang login.

14. **Migrate**: Jalankan:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

14. **Membuat 2 akun dengan masing-masing 3 dummy data**:
    Mengakses aplikasi di lokal dan membuat 2 akun serta 3 dummy data untuk setiap akun