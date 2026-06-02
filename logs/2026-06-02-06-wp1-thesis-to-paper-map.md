# WP1 Tamamlandı — Thesis-to-Paper Map + IMRaD Spine

**Tarih:** 2026-06-02
**Tür:** milestone
**WP bağı:** WP1
**Yazar:** Korcan Ünal
**Skill:** superpowers:writing-plans (primary) + doc-coauthoring (support)

## Ne oldu

WP1 başlatıldı. Tez (`Docs/KUnal_tez_org_tr.md`, 1960 satır) baştan sona okundu; tüm teknik sayılar (38 FEA noktası, D/t=73.1, LD-SCF formülü R²=0.916, Markl C'=1126 MPa, karma spektrum %68.6 bulgusu) metinden birebir teyit edildi. Tez bölümleri IJPVP makale section'larına satır-aralığı bazında haritalandı; 6.000 kelime hedefine göre IMRaD omurgası kuruldu.

İki stratejik blocker çözüldü:
- **WP0b (kritik SCF eşiği biçimi):** Eşik tek-değer bandı (1.51–1.65), tek operasyonel varsayıma koşullu. Kapalı forma genelleştirildi: `SCF_krit = C'/(S_amp·(n·T)^0.2) ≈ 1.57`. Denklem, Tablo 3.11'in dört satırıyla (1.51→1422, 1.65→912, 1.95→396, 2.37→149) birebir doğrulandı.
- **Anchor F8 de-risk:** F8 master curve tamamen mevcut Markl-Miner denklemlerinden + EK-1 Python kodundan üretilebilir. HANDOVER risk tablosundaki "F8 için yazar verisi gerekli → darboğaz" riski iptal edildi.

Yazar checkpoint'i geçildi: section yapısı ve V1 kararı onaylandı; kalan non-blocking maddeler güvenli varsayımlarla kapatıldı.

## Karar / Sonuç

- **Section yapısı: Seçenek A (5-section fold)** onaylandı. Background→Introduction, Theory→Methods katlanır. WP5 dosya numaralandırmasıyla (00,01,04,05,06,07) birebir uyumlu. Gövde ~5.850 kelime < 6.000.
- **Kelime tahsisi:** Intro 950 / Methods 2.050 / Results 1.550 / Discussion 1.050 / Conclusions 250. WP5a (Methods) = 2 oturum.
- **V1 mesh:** Ek FEA koşusu YOK — DOF + aspect ratio + literatür + IPC2002 %0.3 SCF uyumu argümanı yeterli.
- **Von Mises %11.5:** Ek koşu YOK; mevcut 3 gerekçe güçlü prose + WP6 rebuttal taslağı.
- **V3 baseline:** Ek koşu GEREKSİZ (analitik hoop 220.8 MPa eşleşmesi tezde mevcut, satır 743-749).
- **Anchor F8:** Master curve (SCF vs T_est, n=4/8/12/24 ailesi) + closed-form eşik. Çevrim varsayımı varsayılan; SCADA verisi varsa WP3a'da revize.
- **Kapsam dışı:** "Türk boru hattı pratiği" pasajı çıkarılacak; D/t=73.1 kısıtı Discussion'da explicit.
- **Metin temizliği (zorunlu):** Tez satır 685 yazar soru işareti, satır 1075 "Tablo 7.1" numara hatası, çift denklem 3.12 → WP5a/WP6a'da düzeltilir.

## Etki

- **Yeni dosya:** `Docs/plan/WP1_thesis_to_paper_map.md` (v1.1, onaylı)
- **Bu log:** `logs/2026-06-02-06-wp1-thesis-to-paper-map.md`
- **Plan etkisi:** Section yapısı kilitlendiğinden WP5 alt-adımları artık net dosya hedeflerine sahip (01/04/05/06/07). WP5a kelime tahsisi execution-plan'daki "~1.000" yerine ~2.050 olarak okunmalı (WP1 map otoriter).
- **Sonraki adım:** WP2 / WP3a / WP4 başlatılabilir (paralel mümkün). Yazar `WPx başlat` komutu bekleniyor.

## Referanslar

- WP1 çıktısı: `Docs/plan/WP1_thesis_to_paper_map.md`
- Execution plan: `Docs/plan/2026-05-26-execution-plan-IJPVP-v2.md`
- Önceki log: `logs/2026-05-26-05-session-end-handover.md`
- Tez kaynağı: `Docs/KUnal_tez_org_tr.md`

---

### WP completion record (WP_skill_mapping formatı)
```
WP1 | superpowers:writing-plans | 2026-06-02T00:00:00+03:00 | Docs/plan/WP1_thesis_to_paper_map.md | author-approved
```
