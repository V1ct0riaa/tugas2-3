# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Natanael Pascal Simbolon,
2106751764,
PBP B

## 1. Apa kegunaan `{% csrf_token %}` pada elemen `form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>?`

- Kegunaan `{% csrf_token %}` pada elemen `form>` adalah untuk mencegah serangan CSRF django. Jika kita tidak menggunakan ``{% csrf_token %}`, maka project django kita akan error.

## 2. Apakah kita dapat membuat elemen `<form>` secara manual ?

- Kita bisa membuat elemen `<form>` secara manual dengan tag. Alurnya pun adalah ketika user memencet tombol submit, akan dilakukan https request post dan dicek apakah valid ato tidak datanya. Jika valid, akan dimasukkan ke database, sedangkan jika tidak, user harus input ulang.

## 3. Cara mengimplementasikan

- Pertama-tama kita harus membuat app baru `todolist` dengan perintah `python manage.py startapp todolist` serta menambahkan todolist ke dalam `settings.py` yang berada di `project_django`.
- Kemudian, kita juga harus menambahkan path pada `urls.py` pada `project_django`.
- Lalu, kita buat models yang memiliki beberapa field yang mencakup user,date,title, dan description.
- Kita juga harus membuat user field dengan parameter user dengan `from django.contrib.auth.models import User`.
- Lakukan beberapa hal itu kembali untuk login dll.
- Kemudian kita bikin templates seperti `createTask.html` dll.

# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Natanael Pascal Simbolon,
2106751764,
PBP B

## 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

- Inline CSS sendiri merupakan suatu metode styling pada elemen HTML dengan memberikan style ke tag HTML tertentu dengan `<style>` pada file HTML. Inline CSS memiliki kelebihan ketika kita ingin melakukan perubahan kecil, kita dapat memperbaiki kesalahan style dengan cepat. Kekurangannya, Inline CSS tidak terlalu efektif karena harus diterapkan melalui elemennya satu per satu.
- Internal CSS sendiri merupakan suatu metode styling seperti Inline CSS, namun kode CSS tersebut terletak di tag `<head>` HTML. Internal CSS memiliki kelebihan ketika kita ingin mengubah satu spesifik halaman HTML dan juga class serta ID bisa digunakan oleh internal stylesheet sehingga kita tidak perlu upload banyak file. Akan tetapi, Internal CSS tidak efektif karena jika ingin mengubah satu elemen saja, kita harus merubah full semua elemen dalam halaman tersebut.
- External CSS sendiri merupakan suatu metode styling yang paling layak untuk digunakan karena stylesheetnya diletakkan di file .CSS bukan pada file HTML. Kelebihannya adalah ukuran file HTML menjadi lebih kecil dan stylingnya dapat direuse untuk halaman lain. Akan tetapi, external CSS hanya bisa tampil ketika file .CSS dipanggil juga.

## 2. Jelaskan tag HTML5 yang kamu ketahui.

- `<title>` : untuk membuat judul halaman,
- `<body>` : untuk membuat tubuh halaman,
- `<th>` : untuk membuat header untuk cell dalam table
- `<tr>` : untuk membuat baris dalam table
- `<td>` : untuk membuat cell dalam table
- `<form>` : untuk membuat form
- `<button>` : untuk membuat tombol yang berinteraksi dengan user
- `<p>` : untuk membuat paragraf
- `<div>` : untuk membuat sebuah bagian dokumen
- `<style>` : untuk membuat informasi style untuk dokumen

## 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.

- `<class>` : untuk menerapkan styling elemen class
- `#<id elemen>` : untuk menerapkna styling ke elemen id
- `:link` : untuk menerapkan styling semua link
- `*:` : untuk menerapkan styling ke semua elemen

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

- Pada kali ini, kita hanya perlu menghias app `todolist` yang sudah dibuat pada tugas04 sehingga kita hanya perlu mengedit file templates html.
- Contoh pengimplementasian bootstrap pada file `base.html` :

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link rel="stylesheet" href="{% static 'css/style.css' %}" />
    <link rel=”stylesheet” href=”css/bootstrap-responsive.css”>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
  </body>
</html>
```
