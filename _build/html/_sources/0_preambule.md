---
title: "Systèmes Poly-Articulés"
author: "Kevin Godineau"
description: "Elements de formation pour l'UE Systèmes Poly-Articulés"
institute: "ENS Paris-Saclay"
date: "20/03/2024"
---

# M1 SPA : Systèmes Poly-Articulés

Ce document sert de support pour l'Unité d'Enseignement intitulé "Systèmes Poly-Articulés" du master Mécanique de l'Université Paris-Saclay parcours MIP (Mécanique et Ingénierie de la Production) et MMS (Mécanique des Matériaux et des Structures)

eCampus : [https://ecampus.paris-saclay.fr/course/view.php?id=40554](https://ecampus.paris-saclay.fr/course/view.php?id=40554)

## Objectifs pédagogiques

Le module Systèmes Poly-Articulés (SPA) traite d'un des deux domaines majeurs de la robotique. Dans ce module on s'intéresse à la modélisation mécanique, cinématique et dynamique des systèmes et structures poly-articulés. Les notions abordées permettent de soutenir un très grand nombre de travaux de recherche en robotique, fabrication additive, fabrication soustractive. De nombreuses passerelles vers le second grand domaine de la robotique (contrôle-commande) sont également soulevées. 

- Acquérir les outils et concepts scientifiques fondamentaux utilisés en modélisation géométrique et cinématique des robots. 
- Manipuler des robots industriels et comprendre les problématiques techniques associées à la réalisation d'une trajectoire par l'effecteur. 

## Modalités pédagogiques

Le volume horaire de l'UE est découpé en $4 \times 2h$ de cours, $4 \times 2h$ de TD et $3 \times 4h$ de TP. À cela, on peut rajouter, une séance de $2h$ facultative qui est consacré à la réalisation de l'examen de l'année passée. 

- Cours n°1 : Éléments mathématiques, paramétrages des positionnements
- Cours n°2 : Modélisation géométrique 
- TD n°1 : Paramétrage - MGI, MGD d'un robot SCARA
- Cours n°3 : Modèle géométrique inverse
- TD n°2 : MGI par la méthode de Paul, singularités
- Cours n°4 : Modèle cinématique
- TD n°3 : Modélisations cinématiques - Singularités
- TD n°4 : Modes d'interpolation des trajets
- Examen de l'année passée (facultative) : TD basée sur l'examen de l'année passée, il s'agit d'une séance de remédiation sur toutes les notions vues dans le cours.
- TP n°1, n°2 et n°3 : Parmis les quatre TP, l'étudiant est amené a faire trois TP et deux comptes rendus de TP noté. Un compte rendu sur un système sériel et un compte rendu sur un système parallèle. 

## Modalités d'évaluation

La note finale du module est composée pour 50 % de la note de l'examen écrit (d'une durée de $2h$) et pour 50 % de la moyenne des notes des deux comptes rendus de TP.

## Liste des Travaux Dirigés

::::{card-carousel} 3

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/2_TD_1
:link-type: doc
**TD n°1**
^^^
```{image} https://www.fanuc.eu/~/media/corporate/products/robots/scara/sr-6ia-c/sr-6ia_c_l.png
:height: 100
```

Paramétrage - MGI, MGD d'un robot SCARA
+++
Faire le TD {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/2_TD_2
:link-type: doc
**TD n°2**
^^^
```{image} https://www.fsi-france.fr/wp-content/uploads/2019/11/csm_tx200-6-axis-robotic-arm-pim-2x-50249-jpg-orig_d32898df3c.jpg
:height: 100
```

Paramétrage - MGI par la méthoe de Paul, singularités
+++
Faire le TD {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/2_TD_3
:link-type: doc
**TD n°3**
^^^
```{image} https://www.evsrobot.com/wp-content/uploads/2024/01/6kg-Payload-600mm-4-Axis-Universal-SCARA-Robot.png
:height: 100
```

Modélisations cinématiques - Singularités
+++
Faire le TD {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/2_TD_4
:link-type: doc
**TD n°4**
^^^
```{image} https://www.usinenouvelle.com/expo/img/fraiseuse-usinage-lourd-whb-1000-012221895-product_zoom.jpg
:height: 100
```

Modes d'interpolation des trajets
+++
Faire le TD {fas}`arrow-right`
:::

::::

## Liste des Travaux Pratiques

::::{card-carousel} 3

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/4_TP_Mitsubishi
:link-type: doc
**TP sériel Mitsubishi**
^^^
```{image} ressources/img/TP_Mitsubishi/RV4FL.jpg
:height: 100
```
Paramétrage, singularités, nombre solution MGI, Flag, types de trajets
+++
Lire le TP {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/4_TP_UR10
:link-type: doc
**TP sériel UR10**
^^^
```{image} ressources/img/TP_UR10/UR10.png
:height: 100
```
Paramétrage, MGD, convention de DH et DHm, MCD
+++
Lire le TP {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/4_TP_Spiderbot
:link-type: doc
**TP parallèle Spiderbot**
^^^
```{image} ressources/img/TP_Spiderbot/PhotoSupport.png
:height: 100
```
MGI d'un architecture parallèle, influence d'un défaut géométrique
+++
Lire le TP {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/4_TP_Falcon
:link-type: doc
**TP parallèle Falcon**
^^^
```{image} ressources/img/TP_Falcon/falcon.png
:height: 100
```
Robot haptique, nombre de solution MGD MGI, recherche de solutions
+++
Lire le TP {fas}`arrow-right`
:::

::::

## Liste des Examens des années passées

::::{card-carousel} 3

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/5_Examen_SPA_2022_2023
:link-type: doc
**Examen 2022/2023**
^^^
```{image} ressources/img/Examen_2022_2023/xArm7.jpg
:height: 100
```
Etude du robot xArm 6
+++
Faire l'examen {fas}`arrow-right`
:::

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/5_Examen_SPA_2023_2024
:link-type: doc
**Examen 2023/2024**
^^^
```{image} ressources/img/Examen_2023_2024/spot-payloads-mobile.png
:height: 100
```
Etude du robot Spot
+++
Faire l'examen {fas}`arrow-right`
:::

::::


## Liste des Projets (pour aller plus loin)

::::{card-carousel} 3

:::{card}
:margin: 3
:class-body: text-center
:class-header: bg-light text-center
:link: ressources/10_Projet_1_Robot_Axis
:link-type: doc
**Projet n°1**
^^^
```{image} ressources/img/Projet1/P1_Axis.jpg
:height: 100
```
Modélisation du robot "Axis", loi de commandes des actionneurs
+++
Lire le Projet {fas}`arrow-right`
:::

::::

## À propos de ce document

L'auteur principal de cette édition du module est Kevin Godineau, mais le contenu du cours et une partie de celui des TD et TP est une réécriture du cours de Sylvain Lavernhe.





