#  Tugas 03 : Pengimplementasian Data Delivery Menggunakan Django

Natanael Pascal Simbolon, 
2106751764,
PBP B

## 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
- JSON sendiri memiliki cara yang berbeda dalam menyimpan elemen. Walaupun efisien, JSON tidak menyimpan elemen tidak secara rapi. JSON menyimpan data dalam bentuk array sehingga transfer data lebih mudah. Sedangkan XML dapat menyimpan elemen secara terstruktur sehingga terlihat rapi dan mudah dibaca. Untuk HTML sendiri, Ia hanya berfungsi sebagai tampang dalam website.
## 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
-  Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena platform terbuat oleh data. Oleh karena itu data delivery sangatlah penting agar platform bisa dimanfaatkan secara keseluruhan oleh pengguna.
## 3. Cara pengimplementasikan aplikasi
- Seperti biasa, langkah pertama yang dilakukan adalah dengan menyalakan virtual environment pada directory project. Lalu, kita add app baru mywatchlist dengan perintah ``` manage.py startapp mywatchlist ```.
- Selanjutnya, kita harus menambahkan elemen mywatchlist ke dalam variable ``` INSTALLED_APPS ``` yang terdapat pada ```project_django/settings.py```.
- Setelah itu, kita akan membuat fixtures yang berisi JSON dengan nama ```initial_watchlist_data.json``` dan lakukan perintah ``` python manage.py loaddata initial_watchlist_data.json``` untuk load data dari fixtures.
- Lalu, kita isi file ```views.py``` dengan fungsi ```show_watchlist``` yang akan menerima request user dan memuat data di HTML sehingga menampilkan HTML berisi film yang sudah dan belum ditonton serta rating dll.
- Selanjutnya, kita buat folder baru ```templates``` yang berisikan file hmtml ```mywatchlist.html``` untuk dapat memanggil setiap data film.
- Kita juga harus menambahkan routing dengan membuat file baru ```urls.py``` pada folder ```mywatchlist``` dan pada file ```project_django/urls.py```, kita akan menambahkan path yang memanggil ```urls.py```.
- Akhirnya, unit testing akan dilakukan ddcengan mengisi file ```tests.py``` dengan sebanyak empat fungsi untuk cek url bisa diakses atau tidak. Setelah itu, lakukan ```git add```, ```git commit``` , dan ```git push origin main```

## Screenshot Postman pasca deployment
### HTML
 ![postmanhtml](https://user-images.githubusercontent.com/112412752/191656839-7df723f2-9aa4-4e8f-acac-670c4b09c4fe.jpg)
 
### JSON
    
![postmanjson](https://user-images.githubusercontent.com/112412752/191656938-92a9f631-076e-47d9-8a14-b664ae7e2e59.jpg)

### XML
![postmanxml](https://user-images.githubusercontent.com/112412752/191656991-c80246eb-c49d-4e3e-8058-2f231b235a94.jpg)



### Link app Heroku : 
- HTML : [https://victoriatugas03.herokuapp.com/mywatchlist/
- JSON : https://victoriatugas03.herokuapp.com/mywatchlist/json/
- XML : https://victoriatugas03.herokuapp.com/mywatchlist/xml/
