import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="ID101 - Bahasa Indonesia", page_icon="📝", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .course-header {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .course-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .materi-box {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        border-left: 5px solid #ef4444;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .contoh-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .latihan-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .tips-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">ID101</div>
    <div class="course-title">Bahasa Indonesia</div>
    <div>📝 2 Credits | Semester 1 | General Education</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "2")
with col2:
    st.metric("Semester", "1")
with col3:
    st.metric("Difficulty", "2/7")
with col4:
    st.metric("Hours/Week", "3")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "✍️ Penulisan Ilmiah",
    "📄 EYD & Tata Bahasa",
    "💼 Surat Resmi",
    "🎤 Presentasi",
    "📊 Latihan"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Gambaran Umum Mata Kuliah")
    
    st.markdown("""
    <div class="materi-box">
        <h3>Deskripsi Mata Kuliah</h3>
        <p>Mata kuliah Bahasa Indonesia untuk mahasiswa teknik yang mencakup penulisan akademik, 
        komunikasi formal, penulisan karya ilmiah, dan korespondensi profesional. Mahasiswa akan 
        belajar menulis dengan baik dan benar sesuai kaidah Bahasa Indonesia baku.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Capaian Pembelajaran")
    
    outcomes = [
        "Menulis karya ilmiah (makalah, laporan, skripsi) dengan struktur yang benar",
        "Menyampaikan presentasi efektif dalam Bahasa Indonesia",
        "Menyusun surat resmi dan korespondensi profesional",
        "Memahami dan menerapkan tata bahasa Indonesia yang baik dan benar",
        "Menggunakan EYD (Ejaan Yang Disempurnakan) dengan tepat"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Materi Pembelajaran")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Bagian 1: Penulisan Akademik**
        - Struktur karya ilmiah
        - Paragraf efektif
        - Kutipan dan daftar pustaka
        - Abstrak dan ringkasan
        - Penulisan laporan teknis
        """)
    
    with col2:
        st.markdown("""
        **Bagian 2: Komunikasi Profesional**
        - EYD dan tata bahasa
        - Surat resmi dan memo
        - Email profesional
        - Presentasi ilmiah
        - Diskusi dan argumentasi
        """)
    
    st.markdown("### 📚 Referensi")
    
    references = [
        {"title": "Pedoman Umum Ejaan Bahasa Indonesia (PUEBI)", "author": "Kemendikbud", "type": "Panduan Resmi"},
        {"title": "Bahasa Indonesia untuk Perguruan Tinggi", "author": "Dr. Abdul Chaer", "type": "Buku Teks"},
        {"title": "Penulisan Karya Ilmiah", "author": "Prof. Gorys Keraf", "type": "Buku Referensi"},
        {"title": "Kamus Besar Bahasa Indonesia (KBBI)", "author": "Kemendikbud", "type": "Kamus Online"}
    ]
    
    for ref in references:
        st.markdown(f"📖 **{ref['title']}** oleh {ref['author']} ({ref['type']})")

# ==================== TAB 2: PENULISAN ILMIAH ====================
with tabs[1]:
    st.markdown("## ✍️ Penulisan Karya Ilmiah")
    
    st.markdown("### 1️⃣ Struktur Karya Ilmiah")
    
    st.markdown("""
    <div class="materi-box">
        <strong>Struktur Standar Makalah/Laporan:</strong><br><br>
        1. <strong>Halaman Judul</strong> - Judul, nama penulis, institusi<br>
        2. <strong>Abstrak</strong> - Ringkasan singkat (150-250 kata)<br>
        3. <strong>Pendahuluan</strong> - Latar belakang, rumusan masalah, tujuan<br>
        4. <strong>Tinjauan Pustaka</strong> - Teori dan penelitian terkait<br>
        5. <strong>Metodologi</strong> - Cara penelitian/pengembangan<br>
        6. <strong>Hasil dan Pembahasan</strong> - Temuan dan analisis<br>
        7. <strong>Kesimpulan</strong> - Ringkasan dan saran<br>
        8. <strong>Daftar Pustaka</strong> - Referensi yang digunakan
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 2️⃣ Menulis Paragraf Efektif")
    
    st.markdown("""
    <div class="tips-box">
        <strong>💡 Tips Paragraf yang Baik:</strong><br>
        • Satu paragraf = satu ide utama<br>
        • Kalimat topik di awal paragraf<br>
        • Kalimat penjelas mendukung ide utama<br>
        • Kalimat penutup merangkum atau transisi<br>
        • Panjang ideal: 3-5 kalimat (100-150 kata)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contoh-box">
        <strong>📝 Contoh Paragraf Efektif:</strong><br><br>
        <em>Kalimat Topik:</em> Kecerdasan buatan (AI) telah mengubah cara kerja industri teknologi modern.<br><br>
        <em>Kalimat Penjelas 1:</em> Algoritma machine learning memungkinkan komputer untuk belajar dari data tanpa pemrograman eksplisit.<br><br>
        <em>Kalimat Penjelas 2:</em> Penerapan AI dapat ditemukan dalam berbagai bidang, mulai dari pengenalan wajah hingga mobil otonom.<br><br>
        <em>Kalimat Penutup:</em> Dengan perkembangan yang pesat ini, AI diperkirakan akan terus mendominasi inovasi teknologi di masa depan.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 3️⃣ Kutipan dan Daftar Pustaka")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Kutipan Langsung:**
        
        Menurut Chaer (2015:45), "Bahasa Indonesia adalah bahasa resmi dan bahasa persatuan Republik Indonesia."
        
        **Kutipan Tidak Langsung:**
        
        Bahasa Indonesia merupakan bahasa resmi negara dan alat pemersatu bangsa (Chaer, 2015).
        """)
    
    with col2:
        st.markdown("""
        **Format Daftar Pustaka (APA):**
        
        **Buku:**
        Chaer, A. (2015). *Bahasa Indonesia untuk Perguruan Tinggi*. Jakarta: Rineka Cipta.
        
        **Jurnal:**
        Santoso, B. (2020). Penerapan AI dalam Pendidikan. *Jurnal Teknologi Pendidikan*, 15(2), 123-135.
        """)
    
    # Interactive citation generator
    st.markdown("---")
    st.markdown("### 🔧 Generator Kutipan")
    
    citation_type = st.selectbox("Jenis Sumber", ["Buku", "Jurnal", "Website"])
    
    if citation_type == "Buku":
        col1, col2, col3 = st.columns(3)
        with col1:
            author = st.text_input("Nama Penulis", "Chaer, A.")
        with col2:
            year = st.text_input("Tahun", "2015")
        with col3:
            title = st.text_input("Judul Buku", "Bahasa Indonesia")
        
        city = st.text_input("Kota Terbit", "Jakarta")
        publisher = st.text_input("Penerbit", "Rineka Cipta")
        
        if st.button("Generate Kutipan"):
            citation = f"{author} ({year}). *{title}*. {city}: {publisher}."
            st.success(f"**Daftar Pustaka:** {citation}")
            st.info(f"**Kutipan dalam teks:** ({author.split(',')[0]}, {year})")

# ==================== TAB 3: EYD & TATA BAHASA ====================
with tabs[2]:
    st.markdown("## 📄 EYD & Tata Bahasa Indonesia")
    
    st.markdown("### 1️⃣ Ejaan Yang Disempurnakan (EYD)")
    
    eyd_topics = {
        "Huruf Kapital": [
            "Awal kalimat: **B**ahasa Indonesia",
            "Nama orang: **S**oekarno, **M**egawati",
            "Nama tempat: **J**akarta, **S**urabaya",
            "Nama institusi: **U**niversitas **I**ndonesia",
            "Judul: *Pengantar **T**eknologi **I**nformasi*"
        ],
        "Tanda Baca": [
            "Titik (.) - Akhir kalimat berita",
            "Koma (,) - Pemisah unsur dalam kalimat",
            "Titik koma (;) - Pemisah kalimat setara",
            "Titik dua (:) - Sebelum perincian",
            "Tanda hubung (-) - Kata ulang: anak-anak"
        ],
        "Penulisan Kata": [
            "Kata depan: **di** rumah, **ke** sekolah, **dari** kantor",
            "Imbuhan: **me**nulis, **ber**main, **ter**baik",
            "Kata ulang: buku-buku, bolak-balik",
            "Kata asing: *software*, *hardware* (miring)",
            "Singkatan: DPR, ASEAN, dll., dsb."
        ]
    }
    
    for topic, rules in eyd_topics.items():
        with st.expander(f"📌 {topic}", expanded=False):
            for rule in rules:
                st.markdown(f"• {rule}")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Kalimat Efektif")
    
    st.markdown("""
    <div class="tips-box">
        <strong>Ciri-ciri Kalimat Efektif:</strong><br>
        ✅ Memiliki subjek dan predikat yang jelas<br>
        ✅ Hemat kata (tidak berlebihan)<br>
        ✅ Logis dan mudah dipahami<br>
        ✅ Sesuai dengan kaidah tata bahasa<br>
        ✅ Menggunakan kata baku
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive sentence checker
    st.markdown("### 🔍 Pemeriksa Kalimat")
    
    sentence_input = st.text_area(
        "Masukkan kalimat untuk diperiksa:",
        "Saya sedang belajar tentang bahasa Indonesia yang baik dan benar."
    )
    
    if st.button("Periksa Kalimat"):
        words = sentence_input.split()
        word_count = len(words)
        
        # Simple checks
        has_capital = sentence_input[0].isupper()
        has_period = sentence_input.endswith('.')
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Jumlah Kata", word_count)
        with col2:
            st.metric("Huruf Kapital", "✅" if has_capital else "❌")
        with col3:
            st.metric("Tanda Titik", "✅" if has_period else "❌")
        
        if word_count > 25:
            st.warning("⚠️ Kalimat terlalu panjang. Pertimbangkan untuk memecah menjadi 2 kalimat.")
        elif word_count < 5:
            st.warning("⚠️ Kalimat terlalu pendek. Tambahkan informasi yang diperlukan.")
        else:
            st.success("✅ Panjang kalimat sudah ideal!")

# ==================== TAB 4: SURAT RESMI ====================
with tabs[3]:
    st.markdown("## 💼 Surat Resmi dan Korespondensi")
    
    st.markdown("### 1️⃣ Format Surat Resmi")
    
    st.markdown("""
    <div class="materi-box">
        <strong>Bagian-bagian Surat Resmi:</strong><br><br>
        1. <strong>Kepala Surat (Kop Surat)</strong> - Logo dan nama institusi<br>
        2. <strong>Nomor Surat</strong> - Nomor urut surat<br>
        3. <strong>Tanggal Surat</strong> - Tempat dan tanggal pembuatan<br>
        4. <strong>Lampiran</strong> - Jumlah lampiran (jika ada)<br>
        5. <strong>Perihal</strong> - Topik/maksud surat<br>
        6. <strong>Alamat Tujuan</strong> - Nama dan alamat penerima<br>
        7. <strong>Salam Pembuka</strong> - "Dengan hormat,"<br>
        8. <strong>Isi Surat</strong> - Paragraf pembuka, isi, penutup<br>
        9. <strong>Salam Penutup</strong> - "Hormat kami,"<br>
        10. <strong>Tanda Tangan dan Nama</strong> - Pengirim surat
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 2️⃣ Contoh Surat Lamaran Kerja")
    
    st.markdown("""
    <div class="contoh-box">
        <pre style="background: white; padding: 1rem; border-radius: 8px; font-size: 0.9rem;">
                                                    Jakarta, 15 Januari 2026

Kepada Yth.
HRD Manager PT Teknologi Maju
Jl. Sudirman No. 123
Jakarta Selatan

Perihal: Lamaran Pekerjaan sebagai Software Engineer

Dengan hormat,

Saya yang bertanda tangan di bawah ini:
    Nama    : Ahmad Fauzi
    Tempat/Tgl Lahir : Jakarta, 15 Mei 2002
    Pendidikan : S1 Teknik Informatika
    Alamat  : Jl. Kebon Jeruk No. 45, Jakarta Barat

Dengan ini mengajukan lamaran pekerjaan sebagai Software Engineer di perusahaan 
yang Bapak/Ibu pimpin. Saya memiliki pengalaman dalam pengembangan aplikasi web 
menggunakan React dan Node.js, serta menguasai bahasa pemrograman Python dan Java.

Sebagai bahan pertimbangan, saya lampirkan:
1. Curriculum Vitae
2. Fotokopi Ijazah dan Transkrip Nilai
3. Sertifikat Pelatihan
4. Portofolio Proyek

Demikian surat lamaran ini saya buat. Besar harapan saya untuk dapat bergabung 
dengan perusahaan Bapak/Ibu. Atas perhatiannya, saya ucapkan terima kasih.

                                                    Hormat saya,


                                                    Ahmad Fauzi
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 3️⃣ Email Profesional")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **✅ DO (Lakukan):**
        - Gunakan subject yang jelas
        - Sapa dengan sopan
        - Langsung ke pokok bahasan
        - Gunakan bahasa formal
        - Periksa ejaan sebelum kirim
        - Sertakan tanda tangan email
        """)
    
    with col2:
        st.markdown("""
        **❌ DON'T (Jangan):**
        - Subject yang tidak jelas
        - Bahasa terlalu santai
        - Bertele-tele
        - Typo dan kesalahan ejaan
        - Lupa lampiran
        - Kirim tanpa membaca ulang
        """)

# ==================== TAB 5: PRESENTASI ====================
with tabs[4]:
    st.markdown("## 🎤 Presentasi Ilmiah")
    
    st.markdown("### 1️⃣ Struktur Presentasi")
    
    presentation_structure = {
        "Pembukaan (10%)": [
            "Salam dan perkenalan",
            "Judul presentasi",
            "Outline/agenda presentasi",
            "Tujuan presentasi"
        ],
        "Isi (80%)": [
            "Latar belakang masalah",
            "Metodologi/pendekatan",
            "Hasil dan temuan",
            "Analisis dan pembahasan",
            "Gunakan visual (grafik, diagram)"
        ],
        "Penutup (10%)": [
            "Kesimpulan utama",
            "Rekomendasi/saran",
            "Terima kasih",
            "Sesi tanya jawab"
        ]
    }
    
    for section, points in presentation_structure.items():
        with st.expander(f"📊 {section}", expanded=True):
            for point in points:
                st.markdown(f"• {point}")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Tips Presentasi Efektif")
    
    tips_col1, tips_col2 = st.columns(2)
    
    with tips_col1:
        st.markdown("""
        <div class="tips-box">
            <strong>🎯 Persiapan:</strong><br>
            • Latihan berkali-kali<br>
            • Kuasai materi dengan baik<br>
            • Siapkan slide yang menarik<br>
            • Antisipasi pertanyaan<br>
            • Cek peralatan sebelumnya
        </div>
        """, unsafe_allow_html=True)
    
    with tips_col2:
        st.markdown("""
        <div class="tips-box">
            <strong>🎤 Saat Presentasi:</strong><br>
            • Bicara dengan jelas dan lantang<br>
            • Jaga kontak mata dengan audiens<br>
            • Gunakan bahasa tubuh yang baik<br>
            • Kelola waktu dengan baik<br>
            • Tetap tenang dan percaya diri
        </div>
        """, unsafe_allow_html=True)
    
    # Presentation timer
    st.markdown("---")
    st.markdown("### ⏱️ Timer Presentasi")
    
    duration = st.slider("Durasi presentasi (menit)", 5, 30, 15)
    
    if st.button("Mulai Timer"):
        st.info(f"⏰ Waktu presentasi: {duration} menit")
        st.markdown(f"""
        - **Pembukaan**: {duration * 0.1:.1f} menit
        - **Isi**: {duration * 0.8:.1f} menit
        - **Penutup**: {duration * 0.1:.1f} menit
        """)

# ==================== TAB 6: LATIHAN ====================
with tabs[5]:
    st.markdown("## 📊 Latihan dan Evaluasi")
    
    st.markdown("""
    <div class="latihan-box">
        <strong>💡 Latihan untuk meningkatkan kemampuan Bahasa Indonesia!</strong><br>
        Kerjakan soal-soal berikut untuk menguji pemahaman Anda.
    </div>
    """, unsafe_allow_html=True)
    
    exercises = [
        {
            "title": "Latihan 1: EYD",
            "question": "Perbaiki penulisan kalimat berikut:\n\n'saya sedang belajar di universitas indonesia tentang teknologi informasi'",
            "hint": "Perhatikan huruf kapital dan tanda baca",
            "solution": "Saya sedang belajar di Universitas Indonesia tentang teknologi informasi."
        },
        {
            "title": "Latihan 2: Kalimat Efektif",
            "question": "Perbaiki kalimat tidak efektif berikut:\n\n'Pada hari ini saya akan pergi ke kampus untuk mengikuti kuliah'",
            "hint": "Hilangkan kata yang tidak perlu",
            "solution": "Hari ini saya akan pergi ke kampus untuk mengikuti kuliah.\natau\nSaya akan mengikuti kuliah di kampus hari ini."
        },
        {
            "title": "Latihan 3: Paragraf",
            "question": "Buat paragraf efektif (3-5 kalimat) tentang 'Pentingnya Bahasa Indonesia dalam Dunia Kerja'",
            "hint": "Gunakan struktur: kalimat topik → kalimat penjelas → kalimat penutup",
            "solution": "Contoh:\nBahasa Indonesia memiliki peran penting dalam dunia kerja profesional. Kemampuan berkomunikasi dengan baik dalam bahasa Indonesia menunjukkan profesionalisme dan kredibilitas seseorang. Dalam konteks bisnis, penggunaan bahasa Indonesia yang baik memudahkan penyampaian ide dan negosiasi. Oleh karena itu, penguasaan bahasa Indonesia yang baik menjadi salah satu keterampilan yang dicari oleh perusahaan."
        },
        {
            "title": "Latihan 4: Surat Resmi",
            "question": "Buat surat permohonan izin tidak masuk kuliah karena sakit (minimal 3 paragraf)",
            "hint": "Gunakan format surat resmi yang benar",
            "solution": "Lihat contoh format surat resmi di Tab 4"
        },
        {
            "title": "Latihan 5: Kutipan",
            "question": "Buat daftar pustaka untuk buku:\nPenulis: Gorys Keraf\nJudul: Komposisi\nPenerbit: Nusa Indah\nKota: Ende\nTahun: 2010",
            "hint": "Gunakan format APA",
            "solution": "Keraf, G. (2010). Komposisi. Ende: Nusa Indah."
        }
    ]
    
    for idx, exercise in enumerate(exercises, 1):
        with st.expander(f"📝 {exercise['title']}", expanded=False):
            st.markdown(f"**Soal:**\n\n{exercise['question']}")
            
            if st.button(f"Lihat Petunjuk", key=f"hint_{idx}"):
                st.info(f"💡 {exercise['hint']}")
            
            if st.button(f"Lihat Jawaban", key=f"sol_{idx}"):
                st.success(f"✅ **Jawaban:**\n\n{exercise['solution']}")
    
    # Quiz
    st.markdown("---")
    st.markdown("### 🎯 Kuis Singkat")
    
    quiz_score = 0
    
    q1 = st.radio(
        "1. Penulisan yang benar adalah:",
        ["di rumah", "dirumah", "di-rumah"],
        key="q1"
    )
    if q1 == "di rumah":
        quiz_score += 1
    
    q2 = st.radio(
        "2. Singkatan yang benar adalah:",
        ["D.P.R", "DPR", "D.P.R."],
        key="q2"
    )
    if q2 == "DPR":
        quiz_score += 1
    
    q3 = st.radio(
        "3. Kalimat efektif adalah:",
        [
            "Pada hari ini saya akan pergi ke kampus",
            "Saya akan pergi ke kampus hari ini",
            "Hari ini pada saat sekarang saya akan pergi ke kampus"
        ],
        key="q3"
    )
    if q3 == "Saya akan pergi ke kampus hari ini":
        quiz_score += 1
    
    if st.button("Cek Nilai"):
        percentage = (quiz_score / 3) * 100
        st.metric("Nilai Anda", f"{percentage:.0f}%")
        
        if percentage >= 80:
            st.success("🎉 Excellent! Anda menguasai materi dengan baik!")
        elif percentage >= 60:
            st.info("👍 Good! Terus belajar untuk meningkatkan pemahaman!")
        else:
            st.warning("💪 Keep learning! Pelajari kembali materi yang belum dikuasai!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>ID101 - Bahasa Indonesia</strong><br>
    <small>UTel University | General Education</small>
</div>
""", unsafe_allow_html=True)
