import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Digital - Desa Mekarmanik",
    page_icon="🏘️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data langsung (tanpa import terpisah)
@st.cache_data
def load_data():
    data = {
        'ID': ['MK-001', 'MK-002', 'MK-003', 'MK-004', 'MK-005', 'MK-006', 
               'MK-007', 'MK-008', 'MK-009', 'MK-010', 'MK-011', 'MK-012'],
        'Nama Usaha': [
            'Tani Makmur (Padi & Palawija)', 'Keripik Singkong Rasa', 
            'Peternakan Ayam Kampung', 'Kolam Ikan Nila & Lele',
            'Kue Basah & Katering Kecil', 'Kerajinan Eceng Gondok',
            'Gula Aren Merah', 'Budidaya Jamur Tiram',
            'Sabun Cuci Piring Isi Ulang', 'Kopi Robusta Mekarmanik',
            'Jahit & Bordir', 'Madu Kelulut Trigona'
        ],
        'Pemilik': ['Pak Asep', 'Bu Entin', 'Pak Ujang', 'Mang Oman', 
                    'Ibu Rohmah', 'Teh Yanti', 'Pak Dedi', 'Pak Jajang',
                    'Bu Ai', 'Pak Aan', 'Ceu Iis', 'Bu Yayah'],
        'Dusun': ['Dusun 1', 'Dusun 1', 'Dusun 2', 'Dusun 2', 
                  'Dusun 3', 'Dusun 3', 'Dusun 1', 'Dusun 4',
                  'Dusun 4', 'Dusun 2', 'Dusun 3', 'Dusun 4'],
        'Kategori': ['Pertanian', 'Kuliner', 'Peternakan', 'Perikanan',
                     'Kuliner', 'Kriya', 'Pertanian', 'Pertanian',
                     'Jasa/Kimia', 'Perkebunan', 'Fashion', 'Peternakan'],
        'Omzet (Rp)': [9900000, 4500000, 2750000, 5400000, 1900000, 1875000,
                      4200000, 4200000, 1520000, 8800000, 4500000, 3600000],
        'Unit Terjual': [1800, 450, 1100, 180, 950, 25, 280, 350, 190, 220, 45, 60],
        'Go Digital': ['Belum', 'Ya', 'Belum', 'Ya', 'Belum', 'Ya', 
                       'Ya', 'Ya', 'Belum', 'Ya', 'Ya', 'Ya']
    }
    return pd.DataFrame(data)

df = load_data()

# Sidebar
with st.sidebar:
    st.title("🏘️ Desa Mekarmanik")
    st.markdown("---")
    
    # Filter
    dusun_filter = st.multiselect(
        "Pilih Dusun",
        options=df['Dusun'].unique(),
        default=df['Dusun'].unique()
    )
    
    kategori_filter = st.multiselect(
        "Pilih Kategori",
        options=df['Kategori'].unique(),
        default=df['Kategori'].unique()
    )
    
    df_filtered = df[
        (df['Dusun'].isin(dusun_filter)) &
        (df['Kategori'].isin(kategori_filter))
    ]
    
    st.markdown(f"**Data Tampil:** {len(df_filtered)} UMKM")

# Main Content
st.title("📊 Dashboard Digital Desa Mekarmanik")
st.markdown("*Pemetaan Potensi Ekonomi, Produksi, dan Pemasaran*")
st.markdown("---")

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Total UMKM", len(df_filtered))

with col2:
    total_omzet = df_filtered['Omzet (Rp)'].sum()
    st.metric("💰 Total Omzet", f"Rp {total_omzet/1000000:.1f} Jt")

with col3:
    go_digital = (df_filtered['Go Digital'] == 'Ya').sum()
    st.metric("🌐 Go Digital", f"{go_digital} UMKM")

with col4:
    total_terjual = df_filtered['Unit Terjual'].sum()
    st.metric("📦 Total Terjual", f"{total_terjual} unit")

st.markdown("---")

# Charts
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("📊 Omzet per Dusun")
    omzet_dusun = df_filtered.groupby('Dusun')['Omzet (Rp)'].sum().reset_index()
    st.bar_chart(omzet_dusun.set_index('Dusun'))

with col_chart2:
    st.subheader("🏪 Kategori Usaha")
    kategori_count = df_filtered['Kategori'].value_counts()
    st.bar_chart(kategori_count)

# Table
st.markdown("---")
st.subheader("📋 Data Pelaku Usaha")

# Format currency
df_display = df_filtered.copy()
df_display['Omzet (Rp)'] = df_display['Omzet (Rp)'].apply(lambda x: f"Rp {x:,.0f}")

st.dataframe(
    df_display[['ID', 'Nama Usaha', 'Pemilik', 'Dusun', 'Kategori', 'Omzet (Rp)', 'Go Digital']],
    use_container_width=True,
    hide_index=True
)

# Footer
st.markdown("---")
st.markdown("*Dashboard PKM 2026 | Desa Mekarmanik*")