import streamlit as st
from datetime import datetime

# --- 1. KONFIGURASI HALAMAN WEB ---
st.set_page_config(
    page_title="CeritaKita - Berbagi Cerita & Pengalaman",
    page_icon="📖",
    layout="wide"
)

# --- 2. FITUR PILIHAN TEMA SIANG / MALAM DI SIDEBAR ---
with st.sidebar:
    st.title("⚙️ Pengaturan")
    # Membuat radio button untuk memilih tema
    pilihan_tema = st.radio(
        "Pilih Mode Tampilan:",
        ("🌙 Malam (Dark Mode)", "☀️ Siang (Light Mode)")
    )
    st.markdown("---")
    st.caption("Aplikasi CeritaKita v2.0 - © 2026")

# --- 3. LOGIKA PENGATURAN WARNA DAN BACKGROUND ---
if pilihan_tema == "🌙 Malam (Dark Mode)":
    # Gambar abstrak gelap, teks kuning/putih, kotak transparan hitam
    URL_BG = "https://unsplash.com"
    WARNA_TEKS_UTAMA = "#ffffff"
    WARNA_JUDUL = "#ffeb3b"  # Kuning Cerah
    WARNA_KOTAK = "rgba(15, 23, 42, 0.8)"  # Hitam Kaca
    WARNA_SUB_TEKS = "#94a3b8"
else:
    # Gambar abstrak terang, teks hitam/gelap, kotak transparan putih
    URL_BG = "https://unsplash.com"
    WARNA_TEKS_UTAMA = "#1e293b"
    WARNA_JUDUL = "#1e3a8a"  # Biru Tua
    WARNA_KOTAK = "rgba(255, 255, 255, 0.85)"  # Putih Kaca
    WARNA_SUB_TEKS = "#475569"

# Menerapkan gaya CSS secara dinamis berdasarkan tema yang dipilih
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{URL_BG}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        transition: background 0.5s ease;
    }}

    /* Pewarnaan Teks Komponen Streamlit */
    .stMarkdown, .stTextArea, .stTextInput, .stSelectbox, label {{
        color: {WARNA_TEKS_UTAMA} !important;
    }}

    /* Judul Utama */
    h1, h2, h3 {{
        color: {WARNA_JUDUL} !important; 
        text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.2);
    }}

    /* Desain Formulir Kaca Dinamis */
    div[data-testid="stForm"] {{
        background-color: {WARNA_KOTAK};
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 16px;
        padding: 30px;
        backdrop-filter: blur(15px);
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 4. PENYIMPANAN DATA SEMENTARA ---
if 'data_cerita' not in st.session_state:
    st.session_state.data_cerita = [
        {
            "Judul": "Pengalaman Pertama Magang di Perusahaan Besar",
            "Kategori": "Pengalaman Kerja",
            "Penulis": "Rian Amanda",
            "Tanggal": "2026-08-25",
            "Isi": "Awalnya sangat gugup dan merasa tidak tahu apa-apa. Namun kuncinya adalah jangan takut bertanya kepada senior. Di bulan kedua, saya sudah bisa memegang proyek kecil sendiri. Semangat buat yang baru mulai magang!"
        },
        {
            "Judul": "Solo Traveling ke Labuan Bajo dengan Budget Minim",
            "Kategori": "Travel & Liburan",
            "Penulis": "Siska Putri",
            "Tanggal": "2026-08-24",
            "Isi": "Liburan sendirian itu membuka mata banget. Saya menginap di hostel ransel (backpacker) dan menyewa motor warga lokal. Pemandangan dari puncak Pulau Padar membuat semua rasa lelah perjalanan langsung hilang seketika."
        }
    ]

# --- 5. TAMPILAN UTAMA WEB ---
st.title("📖 CERITAkita JQ")
st.write(
    "Wadah hangat untuk saling berbagi cerita hidup, curahan hati, petualangan, dan pengalaman berharga dari semua kalangan.")
st.markdown("<br>", unsafe_allow_html=True)

kolom_kiri, kolom_kanan = st.columns(2)

with kolom_kiri:
    st.subheader("🔍 Jelajahi Cerita")
    cari_teks = st.text_input("Cari cerita berdasarkan judul atau kata kunci...", "")
    st.markdown("---")

    # Menampilkan daftar cerita di dalam kotak kontras transparan
    for cerita in st.session_state.data_cerita:
        if cari_teks.lower() in cerita["Judul"].lower() or cari_teks.lower() in cerita["Isi"].lower():
            st.markdown(
                f"""
                <div style="
                    background-color: {WARNA_KOTAK}; 
                    padding: 24px; 
                    border-radius: 14px; 
                    border-left: 6px solid {WARNA_JUDUL};
                    margin-bottom: 22px;
                    backdrop-filter: blur(10px);
                    box-shadow: 0px 6px 15px rgba(0,0,0,0.15);
                ">
                    <h3 style="margin:0; color:{WARNA_JUDUL}; text-shadow:none;">{cerita['Judul']}</h3>
                    <p style="font-size:13px; color:{WARNA_SUB_TEKS}; margin-top:6px; margin-bottom:12px;">
                        📁 Kategori: <b>{cerita['Kategori']}</b> | ✍️ Oleh: {cerita['Penulis']} | 📅 {cerita['Tanggal']}
                    </p>
                    <p style="color:{WARNA_TEKS_UTAMA}; line-height:1.7; margin-bottom:0; font-size:15px;">{cerita['Isi']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

with kolom_kanan:
    st.subheader("✍️ Tulis Ceritamu")
    with st.form("form_cerita", clear_on_submit=True):
        input_judul = st.text_input("Judul Cerita / Pengalaman:")
        input_kategori = st.selectbox("Pilih Kategori:",
                                      ["Cerita Inspiratif", "Pengalaman Kerja", "Travel & Liburan", "Tips Kehidupan"])
        input_penulis = st.text_input("Nama Anda (Bisa Anonim):")
        input_isi = st.text_area("Tuliskan cerita lengkap Anda di sini:")

        tombol_kirim = st.form_submit_button("Bagikan Cerita Sekarang")

        if tombol_kirim:
            if input_judul and input_penulis and input_isi:
                cerita_baru = {
                    "Judul": input_judul,
                    "Kategori": input_kategori,
                    "Penulis": input_penulis,
                    "Tanggal": datetime.today().strftime('%Y-%m-%d'),
                    "Isi": input_isi
                }
                st.session_state.data_cerita.insert(0, cerita_baru)
                st.success("Hebat! Cerita Anda telah sukses diterbitkan.")
            else:
                st.error("Gagal! Mohon isi semua kolom formulir terlebih dahulu.")
