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