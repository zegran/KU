# WP6 Faz 3 — WP6b Citation Kesinleştirme + Bibliography

**Tarih:** 2026-07-05
**Tür:** milestone / wp6-faz3 (WP6b)
**Skill:** `citation-verification` (WP6b sorumlu skill)
**Yazar:** Korcan Ünal

## Çıktı

`Docs/paper/sections/08_references.md` — **30 referans**, Elsevier numbered style, ilk-atıf sıralı. Metin içi tüm `[n]` numaraları finalize edildi; 30/30 referans en az bir kez atıflı, atıf-listesi tam eşleşme doğrulandı (grep denetimi).

## Kaynak tabanı
- Tez v2 listesi [1]–[42] (yazar-küratörlü) — 27 giriş buradan.
- WP2 pool — [28] Kiefner primer (E1), [29] Pinheiro dent-SCF (F4, IJPVP metodolojik ikiz).
- WP6b metin-çapali eklemeler — [16] Ross (Taguchi), [26] Montgomery (OLS), [19] Abaqus kılavuzu, [30] Xie (modern S–N), [6] Omale (X70), [3] Murray (wrinkling), [10] Ma + [11] Holliday (ILI).

## DOI doğrulaması (doi-verifier MCP, CrossRef/OpenAlex)
✅ Doğrulandı: Pinheiro 2019 (10.1016/j.ijpvp.2019.01.015) · Ma 2021 (10.3390/s21113862) · Omale 2017 (10.1016/j.msea.2017.07.086) · Xie 2022 (10.1016/j.ijfatigue.2022.106982) · Murray 1997 (10.1016/S0141-0296(96)00096-X) · Laulusa 2006 (10.1016/j.ijsolstr.2005.08.006) · Liu IPC2008 (10.1115/IPC2008-64030) · Johnson IPC2022 + Holliday IPC2018 (DOI tez v2'de mevcut).
Doğrulanamayan cilt/sayfa bilgileri künyelerden çıkarıldı (anti-fabrikasyon; DOI yeterli erişim anahtarı).

## Otonom kararlar
1. **Zhang ILI review (tez v2 [37]) ÇIKARILDI** — DOI doğrulanamadı (iki farklı sorguda); yerine ILI bağlamına DOI'li [10] Ma (Sensors 2021) + [11] Holliday (IPC2018) atandı.
2. **Methods thin-shell çapası düzeltildi:** eski provisional [1] (=CSA Z662) bağlam hatasıydı → [14] Timoshenko & Woinowsky-Krieger (tez v2'nin yeni eklediği [30]).
3. **Markl [VERIFY] kapandı:** Markl 1952 tez v2'de birincil kaynak olarak mevcut ([34]) → final [22]. C'=1126 kalibrasyon atfı [4,23] (Rosenfeld + Rodabaugh WRC 335 — WP2 pool "C' kaynağı kritik" notu uyarınca).
4. **Intro'ya [6] Omale eklendi** — X70 mekanik özellik iddiasının peer-reviewed desteği (WP2 pool'un "[16] çift kullanım" hatasının çözümü).
5. **Ripple oluşum mekanizması atfı güçlendirildi:** [2] Bilston&Murray + [3] Murray Eng.Struct. (eski tek [2]=B31.8 zayıf çapaydı).
6. **[9] Johnson (repair tech IPC2022) eklendi** — "cut-out or repair with sleeve" cümlesinin doğal çapası (R7 ile uyumlu).

## ⚠ Yazar teyidi bekleyen künye alanları (submission öncesi)
1. **[5] API 5L** — baskı/yıl eksik (tez v2'de de yok). Hangi baskı kullanıldıysa (örn. 46th ed., 2018) eklenmeli.
2. **[28] Kiefner primer** — rapor no/yıl eksik; PHMSA-2011-0023 docket referansı kondu. Yazar tam raporu teyit etmeli.
3. **[4] Rosenfeld IPC2002** — ASME digital collection DOI'si (10.1115/IPC2002-27124) eklenebilir; şu an DOI'siz konferans künyesi.

## İstatistik
- 30 referans: 10 dergi makalesi (2'si IJPVP), 5 konferans (IPC), 7 standart, 6 kitap, 2 rapor/bülten.
- Peer-reviewed dergi oranı WP2 hedefiyle uyumlu yükseltildi (tez: 3 → paper: 10).

## Değişen dosyalar
`08_references.md` (YENİ) · `01_introduction.md` · `04_methods.md` · `05_results.md` · `06_discussion.md`

## Sonraki adım
Faz 4 — WP6c/M1 tam dil pass'i (Q1 register + anti-AI).
