# WP3a Tamamlandı — Figure Strategy (Karar Aşaması)

**Tarih:** 2026-06-02
**Tür:** milestone
**WP bağı:** WP3a
**Yazar:** Korcan Ünal
**Skill:** publication-chart-skill (primary) + matplotlib-visualization (support)

## Ne oldu

WP3a başlatıldı. 20 tez figür caption'ı için karar matrisi üretildi (K4 hard rule #5: hiçbir tez şekli olduğu gibi kullanılamaz). Üretim ortamı probe edildi: matplotlib 3.10.8 + numpy 1.26.4 mevcut, pubfig yok → matplotlib birincil rota. 7 main + 3 supplementary figür envanteri tanımlandı; her main figür için amaç/veri kaynağı/eksen/stil/tip belirlendi. Anchor MF7 (F8) closed-form spec'i WP1 §5 ile tam tutarlı; Tablo 3.11 kontrol noktalarıyla doğrulanmış.

WP1→WP2→WP3a boyunca açık kalan tek belirsizlik (yorulma çevrim spektrumu) yazar kararıyla kapandı: varsayılan n=4/8/12/24 kullanılacak (closed-form, ek veri yok).

## Karar / Sonuç

- **Karar matrisi:** Çıkar (3: Şekil 2.2/2.3/2.5 telif/gereksiz) · Yeniden çiz şematik (2) · Merge composite (4→MF1) · Contour yeniden export (4) · Data-plot regenerate (6: 3.10-3.15) · Yeni (2: MF6/MF7).
- **7 main figür:** MF1 model setup, MF2 ripple geometri, MF3 validation vs IPC2002, MF4 parametrik SCF, MF5 LD-SCF regresyon, MF6 karma spektrum hasar, **MF7 anchor kritik SCF master curve**.
- **Mesh-independence figürü iptal** (WP1 §9.3 — V1 ek koşu yok; 8→7 main).
- **F8 (MF7):** n=4/8/12/24 closed-form; `T_est=(1/n)·(C'/(SCF·S_amp))^5`; T=100 yıl çizgisi; 9 FEA overlay; SCF_krit≈1.57.
- **MF1/MF3:** mevcut tez PNG'lerinden + vektörel annotasyon overlay (çözünürlük mitigation'lı).
- **Üretim rotası:** matplotlib (pubfig kurulmayacak).
- **Artwork standardı:** PDF vektör + PNG yedek, ≥500 dpi, grayscale-safe, `Docs/paper/figures/figN_*.pdf`.

## Etki

- **Yeni dosya:** `Docs/plan/WP3a_figure_strategy.md` (v1.1, onaylı)
- **Bu log:** `logs/2026-06-02-08-wp3a-figure-strategy.md`
- **Plan etkisi:** WP3b için figür-bazlı üretim sırası hazır (anchor-öncelikli). Tüm figür-data bağları net. Son açık-uçlu nokta kapandığından WP3b'de belirsizlik yok.
- **Sonraki adım:** WP3b (figür üretimi, matplotlib) veya WP4 (tablo+denklem). Yazar `WPx başlat` bekleniyor.

## Referanslar

- WP3a çıktısı: `Docs/plan/WP3a_figure_strategy.md`
- F8 closed-form: `Docs/plan/WP1_thesis_to_paper_map.md` §5
- Artwork normu: `Docs/refs/IJPVP_official_sources.md` §6
- Önceki log: `logs/2026-06-02-07-wp2-citation-pool.md`

---

### WP completion record (WP_skill_mapping formatı)
```
WP3a | publication-chart-skill | 2026-06-02T00:00:00+03:00 | Docs/plan/WP3a_figure_strategy.md | author-approved
```
