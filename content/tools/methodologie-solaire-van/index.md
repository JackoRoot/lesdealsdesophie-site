---
title: "Méthodologie : Calculateur puissance solaire van"
description: "Sources, formules et données du calculateur de dimensionnement solaire van. PVGIS toit plat, rendement MPPT Victron terrain, consommations équipements 12V."
date: 2026-05-03
draft: false
layout: page
hidefromlist: true
---

← [Calculateur solaire van](/tools/calculateur-solaire-van/) · ← [Tous les outils](/tools/)

# Méthodologie du calculateur puissance solaire van

> Cette page détaille l'origine de chaque chiffre utilisé par le calculateur. **Transparence totale** : les données officiellement sourcées sont distinguées des estimations terrain.

## Approche du calculateur

Le calculateur répond à une question simple : **combien de watts de panneaux solaires installer sur le toit de mon van pour couvrir ma consommation ?**

**Mode profils rapides** : choisissez un profil type (minimaliste, standard, confort, télétravail). Idéal pour une première estimation avant l'aménagement.

**Mode "Mes équipements réels"** : renseignez chaque appareil (watts × heures/jour). Le calculateur totalise votre consommation journalière réelle et dimensionne l'installation en conséquence.

**La formule centrale :**

<pre style="font-size:17px !important;line-height:1.7;font-family:'Courier New',Courier,monospace;background:#1c1e26;padding:14px 16px;border-radius:8px;color:#d5d5d6;overflow-x:auto;">Wc nécessaires = Consommation journalière (Wh/j)
                 ÷ Productible toit plat (Wh/kWc/j)
                 × 1 000

Productible toit plat (Wh/kWc/j) = 
  Productible zone (kWh/kWc/j)
  × Coefficient saison
  × Rendement MPPT (0,95)
  × (1 - Pertes système (0,14))
  × 1 000</pre>

---

## Données officiellement sourcées ✅

### Productible solaire — toit plat van (inclinaison 0°)

Un panneau posé à plat sur un toit de van produit **8 à 12% de moins** qu'un panneau incliné à 35° plein Sud (optimum France). Le calculateur applique une correction de **-10%** (valeur médiane).

| Zone | Ville référence | Productible optimum 35° | Productible toit plat 0° | Valeur journalière été |
|------|----------------|------------------------|--------------------------|----------------------|
| H1 — Nord | Paris | 950 kWh/kWc/an | 855 kWh/kWc/an | ~2,3 kWh/kWc/j |
| H2 — Centre | Lyon | 1 200 kWh/kWc/an | 1 080 kWh/kWc/an | ~3,0 kWh/kWc/j |
| H3 — Sud | Marseille | 1 580 kWh/kWc/an | 1 395 kWh/kWc/an | ~3,8 kWh/kWc/j |

**Source** : [PVGIS-SARAH3 JRC — Commission Européenne](https://re.jrc.ec.europa.eu/pvg_tools/fr/) · Simulation 2005-2023, technologie c-Si

#### Coefficients saisonniers (H2 — Lyon, référence)

| Saison | Coefficient | Productible toit plat journalier |
|--------|-------------|----------------------------------|
| Hiver (déc-fév) | ×0,45 | ~1,4 kWh/kWc/j |
| Printemps (mars-mai) | ×0,85 | ~2,6 kWh/kWc/j |
| Été (juin-août) | ×1,00 | ~3,0 kWh/kWc/j (référence) |
| Automne (sept-nov) | ×0,65 | ~2,0 kWh/kWc/j |
| Moyenne annuelle | ×0,75 | ~2,2 kWh/kWc/j |

> **Important** : En hiver au Nord, la production peut tomber à ~1 kWh/kWc/j. Un van full-time hivernant en Bretagne aura besoin d'un appoint (alternateur, prise secteur camping).

**Source** : PVGIS-SARAH3 JRC — données mensuelles 2005-2023

---

### Rendement MPPT Victron SmartSolar

- Peak efficiency constructeur : **98-99%**
- **Rendement réel terrain moyen : 95%** ← valeur utilisée dans le calculateur
- Chute si câbles DC longs (>3m) ou rapport Vpv/Vbatt très élevé

**Modèles van recommandés :**

| Modèle | Puissance PV max (12V) | Prix indicatif mai 2026 |
|--------|----------------------|------------------------|
| SmartSolar 75/15 | 220 Wc | 54-70 € |
| SmartSolar 100/20 | 440 Wc | 69-90 € |
| SmartSolar 100/30 | 440 Wc (30A) | 99-120 € |

**Source** : [Victron Energy — SmartSolar MPPT datasheets 2023](https://www.victronenergy.fr/solar-charge-controllers/smartsolar-mppt-75-10-75-15-100-15-100-20) · Victron Community Forum 2021

---

### Pertes système — 14%

Valeur par défaut PVGIS pour une installation on-grid standard, appliquée telle quelle pour une installation van.

| Poste | Valeur |
|-------|--------|
| Câblage DC | ~2% |
| Encrassement (poussière route) | ~3-5% |
| Mismatch | ~1,5% |
| MPPT + divers | ~5-8% |
| **Total retenu** | **14%** |

**Source** : JRC PVGIS 2022 (valeur par défaut on-grid) · ADEME 2019

---

### Profondeur de décharge batterie LFP — 80%

Les batteries LiFePO4 (LFP) supportent une décharge à 80% de leur capacité nominale en usage régulier, sans dégradation prématurée des cycles.

**Formule capacité batterie :**
<pre style="font-size:17px !important;line-height:1.7;font-family:'Courier New',Courier,monospace;background:#1c1e26;padding:14px 16px;border-radius:8px;color:#d5d5d6;overflow-x:auto;">Capacité (Ah) = Consommation (Wh/j) × Jours autonomie
                ÷ 0,80 (DoD) ÷ 12V</pre>

**Source** : Victron Energy — LiFePO4 Battery datasheet · Pylontech datasheet

---

### Frigo compresseur 12V — données mesurées

| Modèle | Capacité | Conso terrain 25°C | Conso été 35°C+ |
|--------|----------|-------------------|-----------------|
| Dometic CFX-35 | 36L | 28-38 Ah/j (~19 Wh/h) | ×1,7-2,0 |
| Dometic CFX-65 | 62L | 38-48 Ah/j | ×1,7-2,0 |

> La valeur par défaut dans le calculateur (19 W × 24h = 456 Wh/j brut, soit ~380 Wh/j avec les cycles) correspond à un Dometic CFX-35 à 25°C. **En été méditerranéen, multipliez par 1,7 minimum.**

**Source** : [VanPowerCalc — Consommation frigo compresseur](https://vanpowercalc.com/fr/frigo-compresseur-camping-car) · Fiche produit Dometic CFX3-35

---

## Données estimées terrain ⚠️

Ces données proviennent de sites spécialisés vanlife et de retours terrain. Elles sont cohérentes entre elles mais **ne proviennent pas de datasheets officiels** pour chaque modèle.

| Équipement | Valeur par défaut | Source | Fiabilité |
|------------|------------------|--------|-----------|
| LED 12V total van | 15 W | objectif-vie-en-van.com | Terrain |
| Ordi portable | 65 W | camp-us.fr (fourchette 50-90 W) | Terrain |
| Ventilateur toit | 20 W | expressvanning.com | Terrain |
| Pompe eau 12V | 60 W × 0,15h/j | objectif-vie-en-van.com | Terrain |
| Chargeurs USB | 20 W × 1h/j | Terrain agrégé | Terrain |
| Chauffage diesel (élec.) | 20 W × usage | CARAPACE 2026, Webasto spec | Moyen |

> **Recommandation** : utilisez le mode manuel et renseignez les vraies valeurs de vos équipements. La consommation d'un ordinateur portable varie de 30W (Macbook Air) à 130W (PC gaming) — l'écart est énorme.

**Sources** : [objectif-vie-en-van.com](https://objectif-vie-en-van.com/installation-electrique-van/) · [CARAPACE Store — Chauffage stationnaire 2026](https://www.carapacestore.fr/chauffage-stationnaire-van-amenage-guide-complet-2026/) · camp-us.fr

---

## Prix indicatifs matériel mai 2026

**[PRIX APPROXIMATIFS — susceptibles d'évoluer]**

| Produit | Prix indicatif |
|---------|----------------|
| Panneau flexible 100W (Dokio, Eco-Worthy) | 80-120 € |
| Panneau flexible 200W | 150-200 € |
| MPPT Victron SmartSolar 75/15 | 54-70 € |
| MPPT Victron SmartSolar 100/20 | 69-90 € |
| Batterie LFP Victron SuperPack 100Ah | ~450 € |
| Batterie LFP Victron SuperPack 200Ah | ~900 € |

**Sources prix** : H2R Équipements · Solaris Store · Idealo.fr · relevés mai 2026

---

## Profils de consommation journalière

| Profil | Consommation | Équipements typiques |
|--------|-------------|----------------------|
| Minimaliste | ~150 Wh/j | Frigo + LED + téléphone |
| Standard | ~350 Wh/j | Frigo + ordi 2h + LED + pompe |
| Confort | ~600 Wh/j | Frigo + ordi 4h + LED + ventilateur |
| Télétravail | ~1 000 Wh/j | Frigo + 2 ordis + LED + ventilateur + tout |

**Source** : [stationnomade.com](https://stationnomade.com/blog/comment-calculer-ses-besoins-en-energie-quand-on-vit-en-van-guide-ultra-simple-pour-vanlifers/) · [CARAPACE Store 2026](https://www.carapacestore.fr/refrigerateur-van-amenage-compresseur-trimixte-absorption-guide-2026/)

---

## Configurations recommandées (CARAPACE 2026)

| Usage | Panneaux | Batterie LFP | Budget matériel |
|-------|----------|-------------|-----------------|
| Weekend / appoint | 100-200 Wc | 100 Ah | 500-900 € |
| Vanlife équilibré | 200-300 Wc | 200 Ah | 900-1 400 € |
| Full-time / télétravail | 300-400 Wc | 200-300 Ah | 1 200-2 200 € |

**Source** : [CARAPACE Store — Guide réfrigérateur van 2026](https://www.carapacestore.fr/refrigerateur-van-amenage-compresseur-trimixte-absorption-guide-2026/)

---

## Ce que le calculateur ne couvre pas

**Ombrage** — un arbre, un vélo sur le toit, une antenne satellite peuvent réduire la production de 15 à 30%. Non modélisé.

**Recharge alternateur** — en roulant, l'alternateur recharge la batterie auxiliaire (via coupleur séparateur ou DC-DC Victron Orion). Non intégré : le calculateur dimensionne l'autonomie solaire seule.

**Panneau portable** — un panneau orientable (posé au sol, incliné vers le soleil) produit jusqu'à 40% de plus qu'un panneau toit plat. Pour un van en stationnement prolongé, c'est un complément efficace.

**Températures extrêmes** — les batteries LFP ne doivent pas être chargées sous 0°C. En hiver, prévoyez une isolation ou un système de chauffage de batterie.

---

**Dernière mise à jour** : Mai 2026
**Sources principales** : PVGIS-SARAH3 JRC (2005-2023) · Victron Energy datasheets 2023 · VanPowerCalc · CARAPACE Store 2026 · objectif-vie-en-van.com
