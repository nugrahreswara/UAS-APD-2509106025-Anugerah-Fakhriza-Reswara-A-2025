import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('unemployment analysis.csv')

years = [str(y) for y in range(1991, 2022)]
df_numeric = df.set_index('Country Name')[years]

plt.figure(figsize=(20, 14))
plt.suptitle("Visualisasi Analisis Pengangguran Global", fontsize=22, fontweight='bold')

ax1 = plt.subplot(2, 2, 1)
recent_years = [str(y) for y in range(2015, 2022)]
avg_unemp = df_numeric[recent_years].mean(axis=1).nlargest(10)
avg_unemp.plot(kind='bar', ax=ax1, color='steelblue')
ax1.set_title('10 Negara dengan Rata-rata Pengangguran Tertinggi (2015–2021)', fontsize=14)
ax1.set_ylabel('Rata-rata (%)')
ax1.tick_params(axis='x', rotation=45)


ax2 = plt.subplot(2, 2, 2)
data_2020 = df['2020'].dropna()
ax2.hist(data_2020, bins=20, color='lightcoral', edgecolor='black', alpha=0.8)
ax2.set_title('Distribusi Tingkat Pengangguran Global Tahun 2020', fontsize=14)
ax2.set_xlabel('Persentase (%)')
ax2.set_ylabel('Jumlah Negara/Wilayah')
ax2.grid(axis='y', linestyle='--', alpha=0.6)


ax3 = plt.subplot(2, 2, 3)
scatter_df = df[['Country Name', '2010', '2020']].dropna()
ax3.scatter(scatter_df['2010'], scatter_df['2020'], alpha=0.7, color='teal')
ax3.set_title('Perbandingan Pengangguran: 2010 vs 2020', fontsize=14)
ax3.set_xlabel('2010 (%)')
ax3.set_ylabel('2020 (%)')
min_val = min(scatter_df[['2010', '2020']].min())
max_val = max(scatter_df[['2010', '2020']].max())
ax3.plot([min_val, max_val], [min_val, max_val], 'r--', label='Tidak Berubah')
ax3.legend()
ax3.grid(True, linestyle='--', alpha=0.5)


ax4 = plt.subplot(2, 2, 4)
corr_years = [str(y) for y in range(2010, 2022)]
corr_matrix = df[corr_years].corr()

sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap='RdYlBu_r',
    linewidths=0.5,
    cbar_kws={"shrink": 0.8},
    annot_kws={"size": 9},
    ax=ax4
)
ax4.set_title('Heatmap Korelasi (2010–2021)', fontsize=14)
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=0)
ax4.set_yticklabels(ax4.get_yticklabels(), rotation=0)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
