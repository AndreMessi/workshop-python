##Pengenalan Python Flask

Flask adalah kerangka (framework) Python untuk membuat aplikasi web. Dari situs aslinya,

    "Flask adalah microframework untuk Python berbasis Werkzeug, Jinja 2 dan "niat baik"".

Ketika kita memikirkan Python, kerangka de facto yang muncul di benak kita adalah framework Django. Tapi dari perspektif pemula Python, Flask lebih mudah, jika dibandingkan dengan Django.
Menyiapkan Flask

Menyiapkan Flask sangat sederhana dan cepat. Dengan package manager pip, semua yang perlu kita lakukan adalah:

pip install flask

Setelah anda selesai meng-install Flask, buat folder dengan nama FlaskApp. Masuk ke folder FlaskApp dan buat sebuah file dengan nama app.py. Import modul flask dan buat aplikasi menggunakan Flask seperti ditunjukkan berikut:

from flask import Flask
app = Flask(__name__)

Sekarang tentukan basic route / dan handler yang sesuai:

@app.route("/")
def main():
    return "Welcome!"

Berikutnya, periksa jika file yang dieksekusi adalah program utama dan jalankan app-nya

if __name__ == "__main__":
    app.run()

Simpan perubahan dan eksekusi app.py:

python app.py

Arahkan browser Anda ke http://localhost: 5000/ dan Anda pasti memiliki pesan pembuka, "welcome".