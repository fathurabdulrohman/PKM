import pandas as pd
import numpy as np

def calculate_kpis(df):
    """Menghitung Key Performance Indicators"""
    kpis = {
        'total_umkm': len(df),
        'total_omzet': df['Omzet Bulanan (Rp)'].sum(),
        'rata_omzet': df['Omzet Bulanan (Rp)'].mean(),
        'total_tenaga_kerja': df['Tenaga Kerja'].sum(),
        'go_digital_pct': (df['Go Digital'] != 'Belum').sum() / len(df) * 100,
        'berlegalitas_pct': (df['Legalitas'] != 'Belum Ada').sum() / len(df) * 100,
        'omzet_tertinggi': df.loc[df['Omzet Bulanan (Rp)'].idxmax(), 'Nama Usaha'],
        'omzet_tertinggi_nilai': df['Omzet Bulanan (Rp)'].max(),
        'kategori_terbanyak': df['Kategori'].mode()[0],
        'total_unit_terjual': df['Unit Terjual'].sum()
    }
    return kpis

def format_rupiah(nilai):
    """Format angka ke Rupiah"""
    if nilai >= 1000000:
        return f"Rp {nilai/1000000:.2f} Jt"
    elif nilai >= 1000:
        return f"Rp {nilai/1000:.0f} Rb"
    else:
        return f"Rp {nilai:,.0f}"

def get_warna_kategori(kategori):
    """Mapping warna untuk kategori"""
    warna = {
        'Pertanian': '#27ae60',
        'Kuliner': '#e74c3c',
        'Peternakan': '#f39c12',
        'Perikanan': '#3498db',
        'Kriya': '#9b59b6',
        'Perkebunan': '#1abc9c',
        'Fashion': '#e67e22',
        'Jasa/Kimia': '#95a5a6'
    }
    return warna.get(kategori, '#34495e')