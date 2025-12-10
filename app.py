from flask import Flask, render_template, request, jsonify

# Buat instance Flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"].lower()

    # ====== KERUSAKAN: PANAS / OVERHEAT ======
    if any(word in user for word in ["panas", "overheat", "kok panas", "ga dingin", "cepet panas"]):
        reply = (
            "Laptop kamu overheat.\n"
            "Solusi:\n"
            "- Bersihkan kipas & ventilasi\n"
            "- Ganti thermal paste\n"
            "- Gunakan cooling pad\n"
            "- Hindari penggunaan di kasur/sofa"
        )

    # ====== LEMOT / LAMBAT ======
    elif any(word in user for word in ["lemot", "lambat", "slow", "ngelag"]):
        reply = (
            "Laptop lemot biasanya karena RAM kecil atau HDD rusak.\n"
            "Solusi: Upgrade ke SSD + tambah RAM minimal 8GB."
        )

    # ====== MATI TOTAL ======
    elif any(word in user for word in ["mati total", "ga nyala", "tidak nyala"]):
        reply = (
            "Mati total bisa disebabkan:\n"
            "- Power IC rusak\n"
            "- Charger rusak\n"
            "- Motherboard short"
        )

    # ====== LAYAR TIDAK TAMPIL ======
    elif any(word in user for word in ["layar gelap", "ga nampil", "tidak tampil", "no display", "blank"]):
        reply = (
            "Layar tidak tampil bisa karena:\n"
            "- Kabel fleksibel rusak/lepas\n"
            "- LCD rusak\n"
            "- Backlight mati\n"
            "Tes dengan monitor eksternal untuk memastikan."
        )

    # ====== DEFAULT ======
    else:
        reply = (
            "Maaf, saya belum menemukan solusi untuk masalah itu.\n"
            "Coba jelaskan lebih detail ya."
        )

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
