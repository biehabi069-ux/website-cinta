from flask import Flask, render_template_string, request
from datetime import date

app = Flask(__name__)

DAFTAR_NAMA = ["Farzan Habibie", "Puji Astuti"]
TANGGAL_JADIAN = "09 Desember 2025"
TANGGAL_MULAI = date(2025, 12, 9)

HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Cinta Sehidup Semati ❤️</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #ff758c, #ffb6c1, #ffc3a0);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.kotak {
    width: 100%;
    max-width: 440px;
    padding: 28px;
    border-radius: 25px;
    background: rgba(255,255,255,0.96);
    box-shadow: 0 10px 35px #8e254455;
    text-align: center;
    position: relative;
    z-index: 2;
}

h1 {
    color: #e91e63;
}

.hati-utama {
    font-size: 65px;
    animation: detak 1s infinite;
}

@keyframes detak {
    50% { transform: scale(1.18); }
}

label {
    display: block;
    text-align: left;
    margin-top: 18px;
    font-weight: bold;
}

select, input {
    width: 100%;
    padding: 12px;
    margin-top: 8px;
    border: 1px solid pink;
    border-radius: 10px;
    font-size: 15px;
    background: white;
}

button {
    width: 100%;
    padding: 13px;
    margin-top: 20px;
    border: none;
    border-radius: 12px;
    background: #e91e63;
    color: white;
    font-size: 15px;
    cursor: pointer;
}

button:hover {
    background: #c2185b;
}

.pesan {
    padding: 18px;
    margin-top: 20px;
    background: #fff0f5;
    color: #c2185b;
    border-radius: 15px;
    line-height: 1.8;
}

.error {
    color: red;
}

.hati-jatuh {
    position: fixed;
    top: -30px;
    z-index: 1;
    pointer-events: none;
    animation: jatuh linear forwards;
}

@keyframes jatuh {
    to {
        transform: translateY(110vh) rotate(360deg);
        opacity: 0;
    }
}

.timer {
    background: #ffe4ec;
    padding: 12px;
    border-radius: 12px;
    font-weight: bold;
}

footer {
    font-size: 12px;
    color: #888;
    margin-top: 25px;
}
</style>
</head>

<body>

<div class="kotak">

    <div class="hati-utama">❤️</div>

    {% if berhasil %}

        <h1>Cinta Sehidup Semati</h1>

        <div class="pesan">
            <h2>{{ nama_anda }} ❤️ {{ nama_pasangan }}</h2>

            <p>
                Dua hati, satu cerita.
                Semoga selalu saling menyayangi,
                saling memahami, dan saling menguatkan.
            </p>

            <div class="timer">
                ❤️ Sudah bersama selama {{ lama_hari }} hari ❤️
            </div>

            <h3>
                Semoga sampai menikah dan
                sakinah, mawaddah, warahmah. 💍
            </h3>

            <p>Tanggal jadian: {{ tanggal }}</p>
        </div>

        <button onclick="putarMusik()">
            🎵 Putar Musik
        </button>

        <audio id="musik" loop>
            <source src="/static/dunia-yang-nanti.mp3" type="audio/mpeg">
        </audio>

        <p id="statusMusik" style="font-size:12px;color:#888">
            Tekan tombol untuk memutar musik.
        </p>

        <button onclick="hatiTambahan()">
            💕 Kirim Hati
        </button>

        <p>
            <a href="/" style="color:#e91e63">
                Kembali ke halaman awal
            </a>
        </p>

    {% else %}

        <h1>Love Forever 💕</h1>

        <p>Masukkan identitas kalian untuk membuka pesan cinta!</p>

        <form method="POST">

            <label>Nama Anda</label>
            <select name="nama_anda" required>
                <option value="">-- Pilih nama --</option>
                {% for nama in daftar_nama %}
                <option value="{{ nama }}">{{ nama }}</option>
                {% endfor %}
            </select>

            <label>Nama Pasangan</label>
            <select name="nama_pasangan" required>
                <option value="">-- Pilih pasangan --</option>
                {% for nama in daftar_nama %}
                <option value="{{ nama }}">{{ nama }}</option>
                {% endfor %}
            </select>

            <label>Tanggal Jadian</label>
            <input
                type="text"
                name="tanggal"
                value="09 Desember 2025"
                required
            >

            <button type="submit">
                Buka Pesan Cinta ❤️
            </button>

        </form>

        {% if error %}
        <p class="error">{{ error }}</p>
        {% endif %}

    {% endif %}

    <footer>Dibuat dengan cinta ❤️</footer>

</div>

<script>
function buatHati() {
    const hati = document.createElement("div");
    hati.className = "hati-jatuh";
    hati.textContent = ["❤️", "💕", "💗", "💖", "💘"][
        Math.floor(Math.random() * 5)
    ];

    hati.style.left = Math.random() * 100 + "vw";
    hati.style.fontSize = (15 + Math.random() * 20) + "px";
    hati.style.animationDuration = (3 + Math.random() * 4) + "s";

    document.body.appendChild(hati);

    setTimeout(() => hati.remove(), 7000);
}

setInterval(buatHati, 350);

function hatiTambahan() {
    for (let i = 0; i < 25; i++) {
        setTimeout(buatHati, i * 100);
    }
}

async function putarMusik() {
    const musik = document.getElementById("musik");
    const status = document.getElementById("statusMusik");

    try {
        await musik.play();
        status.textContent = "Musik sedang diputar ❤️";
    } catch (error) {
        status.textContent =
            "Musik belum tersedia. Periksa file musik di folder static.";
    }
}
</script>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def halaman_utama():
    berhasil = False
    error = ""
    nama_anda = ""
    nama_pasangan = ""
    tanggal = ""
    lama_hari = 0

    if request.method == "POST":
        nama_anda = request.form.get("nama_anda", "").strip()
        nama_pasangan = request.form.get("nama_pasangan", "").strip()
        tanggal = request.form.get("tanggal", "").strip()

        if nama_anda not in DAFTAR_NAMA:
            error = "Nama Anda tidak valid."

        elif nama_pasangan not in DAFTAR_NAMA:
            error = "Nama pasangan tidak valid."

        elif nama_anda == nama_pasangan:
            error = "Nama Anda dan pasangan harus berbeda."

        elif tanggal != TANGGAL_JADIAN:
            error = "Tanggal jadian harus 09 Desember 2025."

        else:
            berhasil = True
            lama_hari = (date.today() - TANGGAL_MULAI).days

    return render_template_string(
        HTML,
        daftar_nama=DAFTAR_NAMA,
        berhasil=berhasil,
        error=error,
        nama_anda=nama_anda,
        nama_pasangan=nama_pasangan,
        tanggal=tanggal,
        lama_hari=lama_hari
    )


if __name__ == "__main__":
    app.run(debug=True)