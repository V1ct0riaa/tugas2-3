# Tugas 02

Pada tugas kali ini, saya ditugaskan untuk :
- Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
- Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
- Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
- Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

# Diagram flow

![messageImage_1663167515662](https://user-images.githubusercontent.com/112412752/190198816-9df37882-4de6-4896-8378-86fd231bdcff.jpg)


## Mengapa kita menggunakan virtual environment? Apakah membuat aplikasi web berbasis Django tanpa virtual environment tetap dapat terwujud?
Pertama-tama, virtual environment sendiri merupakan wadah  environment yang dipergunakan oleh Django untuk menjalankan aplikasi. Penggunaan virtual environment sendiri sangatlah penting untuk menghindari terjadinya permasalahaan dalam proses pengembangan, proses maintenance dan bahkan proses berjalannya aplikasi. Dengan penggunaan virtual environment, aplikasi bisa dikembangkan secara flexibel atau bisa dibilang dapat dikembangkan secara portabel karena tidak memiliki ketergantungan terhadap hardware yang digunakan. Jikalau tidak menggunakan virtual environment, semua proses pengembangan,proses maintenance dan proses berjalannya sebuah aplikasi akan tidak efisien dibandingkan menggunakan virtual environment. Jadi, walaupun tidak menggunakan virtual environment, pembuatan aplikasi web berbasis Django tanpa menggunakan virtual environment tetap dapat terwujud.

## Implementasi aplikasi
- Pertama-tama kita harus menyalakan virtual environment pada directory project dimana kita akan bekerja serta menginstall semua requirements yang dibutuhkan. 
- Lalu, lakukan migration dan load data yang tersedia pada ```initial_catalog_data.json``` .
- Pada file ```views.py```, saya membuat function ```show_katalog``` untuk menerima parameter request dan return fungsi render yang memiliki fungsi untuk menampilkan html yang terisi oleh data yang diambil oleh fungsi tersebut dan disimpan dalam variabel ```data_barang_katalog```. Berikut merupakan petikan codenya:
``` 
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_katalog,
    'nama': 'Natanael Pascal Simbolon',
    'StudentID' : '2106751764'
    
    }

    return render(request, "katalog.html",context) 
```
- Selanjutnya, untuk melakukan routing, saya menambahkan elemen pada variabel ```urlpatterns``` pada file ``` project_django\urls.py ``` untuk program mengambil data sesuai dengan request client. Berikut merupakan petikan codenya:
``` 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/',include('katalog.urls')),
]
```
Saya juga menambahkan elemen pada variabel ```urlpatterns``` yang berada di file ```katalog\urls.py``` untuk memanggil fungsi ```show_katalog``` agar menampilkan data yang telah terkumpul dan disimpan di variabel. Berikut merupakan petikan codenya:
```
urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```
- Lalu, pada template yang berada pada file katalog, saya menambahkan loop dalam table yang melakukan iterasi pada variabel ```list_barang``` sehingga variabel ```list_barang``` dapat menyimpan data-data yang akan ditampilkan pada web. Hal tersebut memungkinkan data barang dapat ditambilkan. Berikut merupakan petikan codenya:
```
{% for barang in list_barang %}
      <tr>
          <th>{{barang.item_name}}</th>
          <th>{{barang.item_price}}</th>
          <th>{{barang.item_stock}}</th>
          <th>{{barang.rating}}</th>
          <th>{{barang.description}}</th>
          <th>{{barang.item_url}}</th>
      </tr>
```
- Terakhir, saya melakukan deployment dengan melakukan perintah ```git add```, ```git commit```, dan ```git push``` untuk mentransfer proyek yang telah dikerjakan ke repository pribadi github. Lalu, saya mengambil API key yang ada pada Heroku dan ditaruh ke dalam repository secret agar aplikasi dapat dibuka di web browser dengan perantara Heroku.


### Link aplikasi
https://victoriatugas02.herokuapp.com/katalog/
