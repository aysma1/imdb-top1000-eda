import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)
pd.set_option("display.float_format", "{:.2f}".format)

veri = pd.read_excel("imdb_top_1000_clean.xlsx")
sayisal_veri = veri.select_dtypes(include=["int64", "float64"])

veri.info()

print("\n\nSayısal Değişkenler\n")
print(sayisal_veri.describe())


print("\n\nKategorik Değişkenler")
kategorik_veri_sutunlari = veri.select_dtypes(include=["object"]).columns

for sutun in kategorik_veri_sutunlari:
    print(f"\nDeğişken: {sutun}")

    sinif_sayisi = veri[sutun].nunique()
    print(f"Toplam Benzersiz Sınıf Sayısı: {sinif_sayisi}")

    if sutun == 'Series_Title':
        print("Bu sütun film adları (ID) olduğu için frekans listesi atlanıyor.")
        continue

    frekanslar = veri[sutun].value_counts(dropna=False)

    if sinif_sayisi > 25:
        print("En Sık Görülen İlk 10 Sınıf ve Frekansları:")
        print(frekanslar.head(10))
    else:
        print("Tüm Sınıflar ve Frekansları:")
        print(frekanslar)



print("\n\nEksik Veri Analizi\n")

eksik_veri = veri.isnull().sum().to_frame("Eksik Sayi")
eksik_veri["Eksik Yuzde"] = (eksik_veri["Eksik Sayi"] / len(veri)) * 100
print(eksik_veri)

sns.set_theme(style="whitegrid")

# Histogram (Tek Değişkenli)
plt.figure(figsize=(10, 6))
sns.histplot(veri['IMDB_Rating'], bins=20, kde=True, color='blue')
plt.title("Grafik 1: IMDB Puanı Dağılımı (Tek Değişkenli Histogram)", fontsize=16)
plt.xlabel("IMDB Puanı (IMDB_Rating)", fontsize=12)
plt.ylabel("Film Sayısı (Frekans)", fontsize=12)
plt.savefig('grafik_1_histogram_imdb_rating.png')
plt.show()
plt.close()

# Kutu Grafiği (Çok Değişkenli)
top_certificates = veri['Certificate'].value_counts().head(5).index
veri_filtrelenmis = veri[veri['Certificate'].isin(top_certificates)]

plt.figure(figsize=(12, 7))
sns.boxplot(x='Certificate', y='IMDB_Rating', data=veri_filtrelenmis, order=top_certificates)
plt.title("Grafik 2: IMDB Puanının Sertifika Türüne Göre Dağılımı (Kutu Grafiği)", fontsize=16)
plt.xlabel("Sertifika (Certificate) - En Yaygın 5", fontsize=12)
plt.ylabel("IMDB Puanı (IMDB_Rating)", fontsize=12)
plt.savefig('grafik_2_kutu_grafik_rating_vs_sertifika.png')
plt.show()
plt.close()

# Scatter Plot (Çok Değişkenli)
plt.figure(figsize=(10, 6))
sns.regplot(x='Meta_score', y='IMDB_Rating', data=veri,
            scatter_kws={'s': 50, 'alpha': 0.6},
            line_kws={'color': 'red', 'linewidth': 2})
plt.title("Grafik 3: İzleyici Puanı vs. Eleştirmen Puanı (Scatter Plot)", fontsize=16)
plt.xlabel("Eleştirmen Puanı (Meta_score)", fontsize=12)
plt.ylabel("İzleyici Puanı (IMDB_Rating)", fontsize=12)
plt.savefig('grafik_3_scatterplot_rating_vs_metascore.png')
plt.show()
plt.close()

# Heatmap (Korelasyon Matrisi - Çok Değişkenli)
sayisal_veri = veri.select_dtypes(include=["int64", "float64"])
corr_matrix = sayisal_veri.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, annot_kws={"size": 10})
plt.title("Grafik 4: Sayısal Değişkenler Arası Korelasyon Matrisi (Heatmap)", fontsize=16)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.tight_layout()
plt.savefig('grafik_4_heatmap_korelasyon.png')
plt.show()
plt.close()

