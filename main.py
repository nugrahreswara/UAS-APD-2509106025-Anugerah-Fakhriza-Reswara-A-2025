import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
df = pd.read_csv('unemployment analysis.csv')

# Tampilkan info dasar dataset
print("Dataset shape:", df.shape)
print("\nContoh data:")
print(df.head())

# --- 1. Bar Chart: Rata-rata pengangguran 2015–2021 untuk 10 negara tertinggi ---
recent_years = [str(year) for year in range(2015, 2022)]
df_recent = df.set_index('Country Name')[recent_years]
df_recent['Avg_2015_2021'] = df_recent.mean(axis=1)
top10_unemployment = df_recent['Avg_2015_2021'].nlargest(10)

plt.figure(figsize=(12, 6))
top10_unemployment.plot(kind='bar', color='steelblue')
plt.title('10 Negara dengan Tingkat Pengangguran Rata-rata Tertinggi (2015–2021)', fontsize=14)
plt.ylabel('Rata-rata Persentase Pengangguran (%)')
plt.xlabel('Negara')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --- 2. Histogram: Distribusi tingkat pengangguran global tahun 2020 ---
plt.figure(figsize=(10, 6))
df_2020 = df['2020'].dropna()
plt.hist(df_2020, bins=20, color='lightcoral', edgecolor='black', alpha=0.7)
plt.title('Distribusi Tingkat Pengangguran Global Tahun 2020', fontsize=14)
plt.xlabel('Persentase Pengangguran (%)')
plt.ylabel('Jumlah Negara/Wilayah')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# --- 3. Scatter Plot: Pengangguran 2010 vs 2020 (untuk melihat perubahan) ---
plt.figure(figsize=(10, 6))
df_scatter = df[['Country Name', '2010', '2020']].dropna()
plt.scatter(df_scatter['2010'], df_scatter['2020'], alpha=0.7, color='teal')
plt.title('Perbandingan Tingkat Pengangguran: 2010 vs 2020', fontsize=14)
plt.xlabel('Pengangguran 2010 (%)')
plt.ylabel('Pengangguran 2020 (%)')
plt.grid(True, linestyle='--', alpha=0.6)
# Tambahkan garis identitas (jika tidak berubah)
min_val = min(df_scatter[['2010', '2020']].min())
max_val = max(df_scatter[['2010', '2020']].max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='Tidak Berubah')
plt.legend()
plt.tight_layout()
plt.show()

# --- 4. Heatmap: Korelasi antar tahun (contoh: 2010–2021) ---
plt.figure(figsize=(12, 8))
years_corr = [str(y) for y in range(2010, 2022)]
corr_matrix = df[years_corr].corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Heatmap Korelasi Tingkat Pengangguran Antar Tahun (2010–2021)', fontsize=14)
plt.tight_layout()
plt.show()
