import pandas as pd
import numpy as np

def load_data_warga():
    """Load data warga/UMKM Desa Mekarmanik"""
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
        'Skala': ['Mikro', 'Mikro', 'Kecil', 'Mikro',
                  'Mikro', 'Mikro', 'Mikro', 'Mikro',
                  'Mikro', 'Kecil', 'Mikro', 'Mikro'],
        'Produk Unggulan': ['Gabah Kering', 'Keripik Singkong', 'Telur Ayam Kampung',
                           'Ikan Nila Segar', 'Aneka Kue Basah', 'Tas Eceng Gondok',
                           'Gula Aren Cetak', 'Jamur Tiram Segar', 'Sabun Cuci 1 Liter',
                           'Kopi Bubuk 250gr', 'Seragam/Baju', 'Madu Kelulut 100ml'],
        'Harga Satuan (Rp)': [5500, 10000, 2500, 30000, 2000, 75000,
                             15000, 12000, 8000, 40000, 100000, 60000],
        'Omzet Bulanan (Rp)': [9900000, 4500000, 2750000, 5400000, 1900000, 1875000,
                              4200000, 4200000, 1520000, 8800000, 4500000, 3600000],
        'Unit Terjual': [1800, 450, 1100, 180, 950, 25,
                        280, 350, 190, 220, 45, 60],
        'Tenaga Kerja': [3, 5, 2, 1, 4, 6, 2, 2, 1, 8, 2, 1],
        'Go Digital': ['Belum', 'Ya (WA, FB)', 'Belum', 'Ya (WA)', 
                       'Belum', 'Ya (IG, WA)', 'Ya (WA)', 'Ya (FB)',
                       'Belum', 'Ya (Shopee, WA)', 'Ya (WA)', 'Ya (FB, WA)'],
        'Legalitas': ['Belum Ada', 'PIRT', 'Belum Ada', 'Belum Ada',
                      'PIRT', 'Belum Ada', 'Halal', 'Belum Ada',
                      'Belum Ada', 'NIB, Halal', 'Belum Ada', 'Belum Ada'],
        'Status Penjualan': ['Lunas', 'Lunas', 'Lunas', 'Lunas',
                            'Lunas', 'Tertunda', 'Lunas', 'Lunas',
                            'Lunas', 'Lunas', 'Lunas', 'Lunas']
    }
    
    df = pd.DataFrame(data)
    return df

def load_tren_omzet():
    """Load data tren omzet 6 bulan"""
    data = {
        'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
        'Pak Asep': [8.5, 9.0, 9.5, 9.7, 9.8, 9.9],
        'Bu Entin': [4.0, 4.2, 4.3, 4.4, 4.5, 4.5],
        'Pak Ujang': [2.4, 2.5, 2.6, 2.7, 2.8, 2.75],
        'Mang Oman': [5.0, 5.1, 5.2, 5.3, 5.4, 5.4],
        'Ibu Rohmah': [1.7, 1.8, 1.8, 1.9, 1.9, 1.9],
        'Teh Yanti': [1.5, 1.6, 1.7, 1.8, 1.8, 1.875],
        'Pak Dedi': [3.8, 3.9, 4.0, 4.1, 4.2, 4.2],
        'Pak Jajang': [3.5, 3.8, 4.0, 4.1, 4.2, 4.2],
        'Bu Ai': [1.3, 1.4, 1.4, 1.5, 1.5, 1.52],
        'Pak Aan': [7.5, 8.0, 8.2, 8.5, 8.7, 8.8],
        'Ceu Iis': [3.8, 4.0, 4.2, 4.3, 4.4, 4.5],
        'Bu Yayah': [3.0, 3.2, 3.3, 3.5, 3.6, 3.6]
    }
    
    df = pd.DataFrame(data)
    return df

def load_data_dusun():
    """Load data ringkasan per dusun"""
    data = {
        'Dusun': ['Dusun 1', 'Dusun 2', 'Dusun 3', 'Dusun 4'],
        'Jumlah UMKM': [3, 3, 3, 3],
        'Total Omzet (Rp)': [18600000, 16950000, 8275000, 9320000],
        'Potensi Unggulan': ['Padi, Keripik, Gula Aren', 'Ayam, Ikan, Kopi', 
                            'Kue, Eceng Gondok, Jahit', 'Jamur, Sabun, Madu']
    }
    
    df = pd.DataFrame(data)
    return df