Nama : Rafa Darussalam

NPM : 2506538924

Kelas : PBP F (Bismillah A nilainya)

### Tugas 1

Pada tugas ini, dikarenakan pembuat tidak bisa mendesain, maka AI digunakan untuk membantu pembuat mendesain websitenya, dan juga memberi ide fungsi mana yang mungkin akan berguna untuk pembuatan website.

1. Untuk elemen semantik, saya menggunakan `<header>`, `<nav>`, `<main>`, `<section>`, dan `<footer>`. Elemen-elemen tersebut membuat struktur halaman lebih jelas dibaca oleh *screen reader* dan memudahkan proses pembacaan ulang kode. Selain itu, elemen seperti `<section id="experience">` memudahkan penautan navigasi serta pengelompokkan gaya CSS tanpa perlu tambahan *class* yang berulang. 
Saat ini, saya belum menggunakan `<aside>` karena belum ada konten tambahan yang perlu ditampilkan di bagian samping. Saya juga lebih memilih menggunakan `<div class="card">` dibandingkan `<article>` karena fokus awal saya adalah penataan *grid* melalui *class* dan belum terlalu mendalami makna semantiknya. Hal ini menjadi catatan perbaikan untuk pengembangan ke depannya.

2. Tantangan yang signifikan belum saya rasakan secara langsung, karena bagian yang seharusnya paling kompleks adalah menyusun tata letak foto di samping profil. Namun, sebagai antisipasi terhadap kendala responsivitas, berikut adalah pendekatan yang saya lakukan:
    *   Mengecek elemen mana yang membutuhkan lebar penuh agar tetap terbaca (teks bio, judul nama) dan elemen mana yang dapat menyusut atau dipindah posisinya tanpa merusak makna (foto, kotak aksen dekoratif).
    *   Untuk *class* `.experience-grid`, saya mengimplementasikan properti CSS `repeat(auto-fit, minmax(280px, 1fr))`. Pendekatan ini memastikan jumlah kolom kartu dapat menyesuaikan secara otomatis dengan lebar layar tanpa perlu menulis *breakpoint* secara manual.

3. Sejauh ini, batasan utama yang dirasakan adalah penulisan daftar konten secara manual (hardcoded) di dalam HTML. Jika terdapat kebutuhan untuk menambah, mengedit, atau mengurutkan ulang entri pengalaman, file HTML harus diedit secara langsung. Pendekatan ini tidak *scalable* untuk jangka panjang. Oleh karena itu, rencana pengembangan selanjutnya meliputi:
    *   Merender konten menggunakan struktur data eksternal, sehingga modifikasi entri *Experience* tidak perlu menyentuh *markup* HTML secara langsung.
    *   Menambahkan filter atau kategori sederhana menggunakan JavaScript untuk memisahkan pengalaman berdasarkan jenis (organisasi, magang, proyek pribadi), mengingat saat ini semua kartu data masih ditampilkan sekaligus tanpa pengelompokan.

### Tugas 2

Pada tugas ini, AI digunakan untuk mendesain page education, dan juga membantu saya mempelajari field ImageField dari sebuah model.

1. Alur yang terjadi ketika pengguna membuka halaman portofolio baru adalah sebagai berikut:
    * User mengetikkan URL ke web, kemudian browser mengirimkan request HTTP ke server Django.
    * Django membaca `urls.py` pertama kali pada level proyek. File tersebut berfungsi untuk mengarahkan request ke `urls.py` milik aplikasi yang tepat menggunakan fungsi `include`.
    * Nah di dalam aplikasi (`main/urls.py`), Django mencocokkan URL dengan rute yang tersedia. Jka cocok, akan memanggil fungsi *view* yang terhubung dengan rute tersebut.
    * Ketika `view.py` menerima request, *view* akan meminta data kepada model jika halaman tersebut memerlukan data.
    * Permintaan dari *view* diterjemahkan oleh `models.py` menjadi perintah SQL untuk mengambil data langsung dari database. Setelah ditemukan, model mengirimkannya kembali ke *view* dalam bentuk objek python.
    * Pada *template*, data objek dari *view* disatukan ke dalam sebuah variabel konteks dan mengirimkannya ke *template* HTML. *Template* kemudian memasukkan data dinamis tersebut ke dalam struktur HTML menggunakan *template tags* (seperti `{{ }}` atau `{% %}`).
    * Setelah *template* selesai di-*render* menjadi dokumen HTML utuh, *view* membungkusnya menjadi HTTP Response dan mengirimkannya kembali ke *browser* pengguna untuk ditampilkan.

2. Ada 2 alasan utama mengapa data portofolio dimasukkan ke dalam model dan bukan *hardcod* di *template*, yaitu:
    * Kemudahan pemeliharaan: ketika suatu saat mau mengubah data yang ada, maka kita hanya perlu mengubah *object* dari suatu model saja tanpa perlu mengambil risiko untuk merusak kode HTML secara tidak sengaja.
    * Skalabilitas pengembangan: Saat data berada di dalam model, kita dapat dengan mudah menambahkan fitur baru tanpa merombak *template*, seperti menambahkan fitur *sort*, *filter*, dll.

3. Perbedaan dari `makemigrations` dengan `migrate` adalah sebagai berikut:
    * `makemigrations` berfungsi untuk memeriksa perubahan pada file `models.py` dan membuat sebuah file instruksi baru yang berisi langkah-langkah bagaimana database harus diubah. Nah perintah ini belum mengubah database sungguhan.
    * `migrate` berfungsi untuk membaca file instruksi yang dibuat oleh makemigrations dan secara fisik menerapkannya ke dalam sistem database.
    
    Kedua peritah ini dijalankan ketika kita menambah atau menghapus atau mengubah sebuah model pada file `models.py`.