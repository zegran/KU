# WP0d — Anti-Plagiarism Rewrite SOP (Operasyonel)

> **Durum:** Aktif (WP5a'dan itibaren uygulanır). **K4 yazar-üstlenimi:** Yazar, YÖK kayıt durumu, iThenticate koşusu ve hukuki/disclosure önlemlerini bizzat üstlendi (2026-06-02). Bu dosya CLI'ın drafting teknik prosedürünü sabitler.
> **Hedef:** Üretilen EN prose, TR tezle <%15 iThenticate örtüşmesi. Çeviri DEĞİL, yeniden yazım.

---

## Per-Section Drafting Prosedürü (her WP5 alt-adımında)

1. İlgili TR tez satır aralığını oku (WP1 haritasından).
2. EN bullet skeleton çıkar (≤10 kelime/bullet, sadece içerik noktaları).
3. **TR kaynağı kapat** — prose yazarken TR metne bakma.
4. Skeleton + mental modelden EN prose yaz (paraphrase, yeniden yapı).
5. Anti-AI öz-kontrol (writing-anti-ai disiplini; formal pass WP6c).
6. TR ↔ EN **içerik** çapraz kontrolü (kapsam, sayı doğruluğu — ifade değil).
7. `Docs/paper/sections/0N_<name>.md`'ye kaydet.

## Anti-Plagiarism İlkeleri

- **Çeviri yasak** (Google Translate / DeepL / kelime-kelime).
- Cümle yapısı, paragraf akışı, başlık düzeni yeniden kurgulanır.
- Sayısal değerler birebir korunur (veri doğruluğu); etrafındaki prose yeniden yazılır.
- Tüm figürler yeniden üretildi (WP3b) → görsel benzerlik 0.
- Tez `references.bib`'e self-citation olarak eklenir (WP6b).
- Cover letter'a K4 şeffaflık paragrafı (WP7a): "based in part on the first author's MSc thesis".

## Yazar Tarafı (üstlenildi)
- YÖK tez kayıt/erteleme durumu
- iThenticate koşusu + raporu (hedef <%15 tezden)
- >%15 çıkarsa → WP6c'ye geri dönüş

## CLI Tarafı (bu SOP)
- Yukarıdaki 7-adım her section'da uygulanır
- Citation numaraları provisional; WP6b'de finalize
- QA bulguları (WP3b/WP4 tutarsızlık bayrakları) drafting'de düzeltilir

---
**Sürüm:** v1 — 2026-06-02 (K4 yazar-üstlenimli; CLI drafting prosedürü sabit)
