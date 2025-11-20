🎬 IMDB Top 1000 – Keşifsel Veri Analizi (EDA) ve Görselleştirme

Bu proje, IMDB Top 1000 film veri seti üzerinde kapsamlı bir Keşifsel Veri Analizi (EDA) gerçekleştirmektedir.
Amaç, veri setindeki sayısal ve kategorik özellikleri incelemek, eksik veri durumunu belirlemek ve çeşitli grafiklerle ilişkileri görselleştirmektir.

📌 İçerik

Kod içerisinde aşağıdaki adımlar vardır:

1️⃣ Veri Yükleme ve Temel İnceleme

Veri seti okunur

info(), sayısal özet istatistikler, kategorik sınıf sayıları görüntülenir

ID niteliği taşıyan “Series_Title” için frekans analizi yapılmaz

2️⃣ Sayısal Değişkenlerin Analizi

Tüm int64 ve float64 değişkenlerin özet istatistikleri

Minimum, maksimum, çeyrek değerler (Q1, Q3), standart sapma

3️⃣ Kategorik Değişkenlerin Analizi

Tüm kategorik sütunların benzersiz sınıf sayısı

Sınıf sayısı 25’ten fazlaysa en sık görülen 10 kategori

Daha azsa tüm değerlerin frekansı listelenir

4️⃣ Eksik Veri Analizi

Her sütundaki eksik gözlem sayısı ve yüzdesi

Eksik veri tablosu (Eksik Sayi, Eksik Yuzde)

5️⃣ Görselleştirmeler

Aşağıdaki grafikler otomatik olarak oluşturulur ve .png olarak kaydedilir:

📊 Histogram

IMDB_Rating dağılımı

KDE eğrisi ile desteklenmiş histogram

📦 Kutu Grafiği (Boxplot)

En yaygın 5 sertifika türüne göre IMDB puanı dağılımı

Ayırt edici outlier yapısını görselleştirir

🔵 Scatter Plot + Regresyon Çizgisi

Meta_score vs IMDB_Rating

Eleştirmen puanı ile izleyici puanı arasındaki ilişki

🔥 Korelasyon Heatmap

Tüm sayısal değişkenler arası korelasyon matrisi

Veri içi ilişkileri görselleştirir

📁 Çıktılar

Kod çalıştırıldığında aşağıdaki görsel dosyaları oluşur:

grafik_1_histogram_imdb_rating.png

grafik_2_kutu_grafik_rating_vs_sertifika.png

grafik_3_scatterplot_rating_vs_metascore.png

grafik_4_heatmap_korelasyon.png

🛠️ Kullanılan Kütüphaneler
pandas
matplotlib
seaborn

(Dosya adını sen belirleyebilirsin.)

📝 Amaç

Bu çalışma, veri bilimine giriş aşamasında EDA uygulamaları, grafiksel yorumlama, veriyi tanıma ve istatistiksel dağılımları inceleme becerilerini geliştirmek amacıyla hazırlanmıştır.
