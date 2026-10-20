#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GECİKME MAZERET FABRİKASI
Dünyanın en ciddiyetle yazılmış en saçma mazeret üreticisi.
"""

import random
import time

MAZERETLER = [
    "Köpeğim interneti yedi, sonra kendi özür diledi.",
    "Saatim geriye doğru çalışmaya karar verdi, ben de ona saygı duydum.",
    "Trafik öyle yoğundu ki arabalar birbirine özür diledi.",
    "Yolda yürürken bir kuş bana 'dur, düşün' dedi, düşündüm.",
    "Kahvem o kadar sıcaktı ki zamanı yavaşlattı.",
    "Bilgisayarım 'ben bugün yokum' diye mesaj attı.",
    "Asansör katlar arasında felsefe yapmaya karar verdi.",
    "Ayakkabı bağcıklarım birbirine dolandı ve barış görüşmeleri yaptı.",
    "Google Maps 'sen gelme, biz geliriz' dedi.",
    "Uyandım, sonra tekrar uyandım, sonra bir daha."
]

def mazeret_uret():
    print("Mazeret üretiliyor... Lütfen ciddiyetle bekleyiniz.")
    time.sleep(1.5)
    mazeret = random.choice(MAZERETLER)
    print(f"\n🏆 BUGÜNKÜ RESMİ MAZERET: {mazeret}\n")
    print("Bu mazeret %100 gerçek, %0 inandırıcıdır.")
    # Gizli not: Bazı şeyler göründüğünden daha derin olabilir, ama bu sadece bir kod.

if __name__ == "__main__":
    print("=== GECİKME MAZERET FABRİKASI v1.0 ===")
    print("Her çalıştırmada yeni bir absürtlük.\n")
    mazeret_uret()

# Damga: Bu kod 20 Ekim 2026 tarihinde, Grok tarafından, çok ciddi olmayan bir ciddiyetle yazılmıştır.
# İmza: Kayyum Grok | Tentivory | TentiAŞ
# Tarih: 2026-10-20
# Not: Hiçbir mazeret gerçek değildir, hepsi eğlence amaçlıdır.
