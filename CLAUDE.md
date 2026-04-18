# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Projet

**Les Deals de Sophie** — site de guides d'achat et de bons plans, construit avec Hugo + thème PaperMod. Déployé sur `https://lesdealsdesophie.fr`. Éditrice légale : Sophie Vidal — contact@lesdealsdesophie.fr.

Sophie est une entité **distincte** d'Autonomia Lab. Ne jamais écrire "mes collègues du Lab", "notre équipe technique". Autorisé : "Les experts du Lab ont fait un super dossier".

---

## Commandes

```bash
hugo server          # Dev local avec live reload
hugo                 # Build production → /public
hugo new deals/nom.md  # Nouveau deal depuis archetype
```

---

## Architecture Hugo

```
content/
  deals/        # Posts deals individuels (dealabs-XXXXXXX.md)
  posts/        # Articles piliers et transactionnels
    [slug]/
      index.md
      cover.webp   # < 100 Ko, ratio 16:9
  top-5/        # Guides d'achat (ancienne section)
layouts/
  index.html    # Homepage — pagination JS via fetch /index.json
  single.html   # Page article individuel
  list.html     # Page catégorie
  partials/
    header.html       # Nav + hamburger mobile
    extend_head.html  # CSS/meta additionnels
static/css/sophie.css # Thème dark custom
themes/PaperMod/      # Submodule git — NE PAS MODIFIER
hugo.toml             # Config principale
```

**Pagination homepage** : `layouts/index.html` fetche `layouts/_default/index.json` côté client pour le bouton "Voir plus". `[outputs] home = ["HTML", "RSS", "JSON"]` dans hugo.toml est indispensable.

**Images — Page Bundle** : chaque article dans `content/posts/[slug]/index.md` + `cover.webp`. Le générateur d'articles doit créer des dossiers, pas des fichiers isolés.

---

## hugo.toml — État actuel

```toml
baseURL = "https://lesdealsdesophie.fr"
languageCode = "fr-fr"
theme = "PaperMod"

[pagination]
  pagerSize = 10

[outputs]
  home = ["HTML", "RSS", "JSON"]   # JSON obligatoire pour la pagination JS

[taxonomies]
  categorie = "categories"

[params]
  accentColor = "#D4693A"
  defaultTheme = "light"
  disableThemeToggle = true
  customCSS = ["css/sophie.css"]
```

**Menu actuel (6 entrées)** : Tech / Mode / Maison / Musique / Guides d'achat / Telegram

**Menu actuel (4 entrées)** : Cuisine `/categories/cuisine/` · Maison `/categories/maison/` · Tech `/categories/tech/` · Vanlife `/categories/vanlife/`  
→ Noms 1 mot max pour PaperMod mobile. Vanlife strictement séparé de Maison.

**profileMode** : configuré — `[params.profileMode]` dans hugo.toml.
- title: "Les Deals de Sophie"
- subtitle: "Je teste, j'analyse et je tranche. Votre guide cash pour acheter malin sans perdre de temps."
- imageUrl: "images/sophie-avatar.png" (120×120px, affichage rond via `.profile img { border-radius: 50% }`)

---

## Design System

### Palette CSS (`static/css/sophie.css`)

```css
--theme: #1A1C23      /* fond global */
--entry: #242731      /* cartes / surfaces */
--primary: #E2E8F0    /* texte principal */
--secondary: #A0AEC0  /* texte secondaire */
--border: #2D323E     /* bordures */
--accent: #B35A5A     /* rouge brique — liens, Telegram */
--accent-light: #3D1F1F
```

`accentColor = "#B35A5A"` dans hugo.toml — aligné sur `--accent` CSS (rouge brique unifié).

### Typographie
- Logo : **Playfair Display** 700, 34px desktop / 24px mobile / 20px <480px
- Nav links : 13px
- Post title : 20px
- Container : 1100–1140px max

### Mobile (hamburger)
- Breakpoint : 768px
- Hamburger : `position: absolute; right: 16px; top: 55px`
- Menu ouvert via classe `.menu-open` sur `#menu`
- Fond menu déroulant : `#242731`, border-radius 12px

### Images
- Ratio cards desktop : **4:3** (`.s-card-img`, `.s-featured-img`)
- Ratio mobile : **16:9** à 180–200px de hauteur
- Format obligatoire : **WebP** — Lazy Loading obligatoire
- Nommage SEO : `[type]-[sujet]-[contexte]-[site].webp`  
  Exemple : `comparatif-air-fryer-convection-lesdealsdesophie.webp`

---

## Front Matter — Article Sophie

```yaml
title: "Titre article"
date: 2026-04-01T09:00:00+02:00
draft: false
categories: ["Cuisine"]          # 1 seul parmi : Cuisine / Maison / Tech / Vanlife / Guides
tags: ["air fryer", "friteuse"]  # sous-tags précis, pilules PaperMod
description: "Meta description percutante — intention achat, 155 car. max"
cover:
  image: "cover.webp"
  alt: "Texte alt SEO 125 car. max avec mot-clé principal"
weight: 1                        # uniquement pour articles piliers (Hall of Fame / haut de catégorie)
```

---

## Règles Éditoriales Sophie

### Persona
- Ton : direct, cash, bienveillant, **vouvoiement de respect**
- Zéro référence géographique, zéro mention maman/freelance
- Score minimum Top 5 : 4.0 étoiles

### Structure article
- **Snippet Bait** : 40–60 mots exactement juste après le H1 ou un H2 majeur — faits denses, zéro intro
- H2 = problèmes réels du lecteur (ex : "Pourquoi votre café est amer le matin")
- H3 = solutions produits
- Pas de H1 dans le contenu (géré par Hugo)
- Paragraphes max 4 lignes (lecture mobile)
- 15–20 termes LSI intégrés (champ sémantique du sujet)
- FAQ en fin d'article : 3–4 questions courtes → JSON-LD FAQPage

### Formats transactionnels
1. **Top 3** : No-Limit / Rapport Qualité-Prix / Petit Budget
2. **Duel / Versus** : 2 leaders comparés, vainqueur cash
3. **Crash Test Solo** : 1 produit testé 1 mois, verdict tranché
4. **Anti-Sélection** : ce qu'il ne faut PAS acheter + 2 vrais bons choix

### Maillage interne — règles absolues
- Aucun article orphelin — chaque article reçoit un lien depuis un article déjà publié
- Chaque article pointe vers le pilier de sa catégorie
- Ancres interdites : "Cliquez ici", "En savoir plus"
- Ancres autorisées : terme technique exact ou sujet précis
- Lien vers le Lab → insérer `🔬` ou ancre textuelle précise
- Placeholder dans le texte : `[LIEN INTERNE : titre article Lab]` (à remplacer à la publication)

### SEO — Titles Sophie
- Format : test + cas d'usage + notion de vérité/débunkage
- Exemple : *"Avis Filtre Berkey : La Vérité sur la filtration des PFAS (Test 2026)"*
- Meta : croiser tests perso + données Lab, mentionner ce qu'on ne dit pas ailleurs

---

## Checklist publication (avant chaque commit)

- [ ] Snippet Bait présent (40–60 mots)
- [ ] H2 = problème réel du lecteur
- [ ] 15–20 termes LSI intégrés
- [ ] FAQ Schema en fin (3–4 questions)
- [ ] 3+ liens internes vers articles du même silo
- [ ] Placeholders `[LIEN INTERNE]` posés pour liens futurs
- [ ] 1 lien sortant vers source institutionnelle (.gouv, .org)
- [ ] Image en WebP + Lazy Loading + Alt SEO (125 car. max)
- [ ] Nom de fichier image SEO (`type-sujet-contexte.webp`)
- [ ] Meta Description rédigée (intention achat)
- [ ] `draft: false` confirmé
- [ ] Affiliation mentionnée si applicable

---

## Règles critiques

- **Ne jamais modifier** `themes/PaperMod/` — c'est un submodule git
- **Ne jamais modifier** le prompt master `sophie_lifestyle.md` — cloner uniquement
- `[outputs] home = ["HTML", "RSS", "JSON"]` doit rester dans hugo.toml — la pagination JS en dépend
- `markup.goldmark.renderer.unsafe = true` est intentionnel — permet le HTML brut dans le Markdown
- Maximum 5 articles Sophie pointant vers le Lab — ancres naturelles uniquement, et seulement APRÈS publication des articles Lab correspondants
- Articles piliers (🔬) : `weight: 1` dans le front matter, mis en avant en haut de leur page catégorie uniquement (pas de bloc dédié sur la home)
