import pandas as pd

veri_seti = pd.DataFrame({
    'Tarih': pd.date_range(start='2026-01-01', periods=6, freq='ME'),
    'Kategori': ['Elektronik', 'Giyim', 'Elektronik', 'Kozmetik', 'Giyim', 'Elektronik'],
    'Satis': [1200, 800, 1500, 400, 950, 2000]
})

veri_seti['Ay'] = veri_seti['Tarih'].dt.month
veri_seti['Ceyrek'] = veri_seti['Tarih'].dt.quarter

# VERİ SETİNİN SON HALİNİ EKRANA YAZDIR
print(veri_seti)

kategori_ozeti = veri_seti.groupby('Kategori').agg(
    Toplam_Satis=('Satis', 'sum'),
    Ortalama_Satis=('Satis', 'mean'),
    Islem_Sayisi=('Satis', 'count')
).reset_index()

print(kategori_ozeti)