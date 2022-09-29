#  Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Natanael Pascal Simbolon, 
2106751764,
PBP B

## 1. Apa kegunaan ```{% csrf_token %}``` pada elemen ```form>```?  Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ```<form>?```
- Kegunaan ```{% csrf_token %}``` pada elemen ```form>``` adalah untuk mencegah serangan CSRF django. Jika kita tidak menggunakan ```{% csrf_token %}``, maka project django kita akan error.
## 2. Apakah kita dapat membuat elemen ```<form>``` secara manual ?
- Kita bisa membuat elemen ```<form>```  secara manual dengan tag. Alurnya pun adalah ketika user memencet tombol submit, akan dilakukan https request post dan dicek apakah valid ato tidak datanya. Jika valid, akan dimasukkan ke database, sedangkan jika tidak, user harus input ulang.
## 3. Cara mengimplementasikan
- Pertama-tama kita harus membuat app baru ```todolist``` dengan perintah ```python manage.py startapp todolist``` serta menambahkan todolist ke dalam ```settings.py``` yang berada di ```project_django```.
- Kemudian, kita juga harus menambahkan path pada ```urls.py``` pada ```project_django```.
- Lalu, kita buat models yang memiliki beberapa field yang mencakup user,date,title, dan description.
- Kita juga harus membuat user field dengan parameter user dengan ```from django.contrib.auth.models import User```.
- Lakukan beberapa hal itu kembali untuk login dll.
- Kemudian kita bikin templates seperti ```createTask.html``` dll.

