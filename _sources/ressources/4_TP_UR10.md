# TP : Étude d'un robot sériel - UR10

Le robot UR10 est un robot collaboratif, pouvant travailler en cohabitation avec l'humain sans protection particulière. Il est dimensionné pour exécuter des tâches de grande dimension (portée allant jusqu'à $1300 mm$), avec des poids allant jusqu'à $10 kg$ en bout de structure. Les applications ciblées sont le conditionnement, la palettisation, l'assemblage et le pick and place. Ses principaux atouts sont la facilité et rapidité de configuration, de programmation et son côté collaboratif, rendant son amortissement rapide.

```{figure} img/TP_UR10/UR10.png
---
width: 400px
name: UR10
--- 
robot UR10
```

## Découverte et prise en main du système

L'objectif de cette partie est de découvrir la structure et le fonctionnement du robot par quelques manipulations.

**Question 1.1 :** Effectuer la procédure de démarrage du robot fournie dans les documents ressource à la fin du sujet.

Réaliser quelques déplacements manuels pour assimiler les différents corps et liaisons du robot :
- dans le mode articulaire ;
- dans le repère de base du robot ;
- dans le repère associé à l'outil (effecteur).

**Question 1.2 :** En déduire comment sont situés le référentiel de base du robot et le référentiel associé à l'outil.

**Question 1.3 :** Réaliser quelques déplacements en mode apprentissage pour découvrir le côté "collaboratif".

**Question 1.4 :** En effectuant des manipulations, découvrir comment sont orientées :
- la base dite « de référence » attaché à la base du robot ;
- la base attachée à l'extrémité ou effecteur du robot. 

Déterminer de façon analogue où sont situées les origines.

**Question 1.5 :** Pour ce robot :
- le paramétrage en position est-il de type cartésien ? polaire ? sphérique ?
- le paramétrage en orientation est-il de type Euler ? Bryan ? quaternions ? extrinsèque ? intrinsèque ?


## Modélisation géométrique

L'objectif de cette partie est de développer un modèle géométrique pour le robot, et confronter ce résultat à deux données :
- la description des paramètres constructeurs;
- la modélisation effectuée pour l'UR10 dans l'application RoboDK.

### Schéma cinématique

**Question 2.1 :** Mettre le robot dans la configuration où toutes les valeurs des axes valent 0°. Réaliser un schéma cinématique, en 3D, dans cette configuration (dessin avec couleurs sur une page A4). Y positionner le référentiel de base du robot ainsi que celui de l’effecteur déterminé précédemment.


### Paramétrage DHm

**Question 2.2 :** En effectuant des manipulations axe par axe, déterminer l'orientation puis le sens de chaque axe
$Z_i$ des liaisons, afin qu'il corresponde au signe positif donné par le pilotage du contrôleur.

**Question 2.3 :** Sur le schéma cinématique précédent, effectuer l'ensemble des tracés et paramétrage selon la convention dite de Denavit et Hartenberg modifiée. Synthétiser les résultats dans le tableau approprié. Mesurer, si besoin au réglet, les constantes géométriques.


### Confrontation à la modélisation dans l'application RoboDK

Le fabricant, fourni dans la documentation technique un tableau de paramètres servant de référence à la calibration du robot ({numref}`UR10para`).

**Question 2.4 :** Analyser les paramètres constructeurs et retrouver les différences et similitudes par rapport au paramétrage construit. Expliquer les différences de paramétrage.


### Confrontation à la modélisation dans l'application RoboDK

Depuis un fichier vierge, puis importer, depuis la librairie en ligne, un robot UR10. Éditer les paramètres du robot en double-cliquant sur le robot.

**Question 2.5 :** En masquant les référentiels inutiles et en agrandissant les flèches (menu « View - Make reference
frames bigger »), déterminer le paramétrage et système d'axes du modèle de l'UR10 dans le logiciel.


## construction du Modèle Géométrique Direct (MGD)

**Question 3.1 :** A partir du paramétrage DHm proposé, expliciter chacune des matrices homogènes de transformation entre les différents corps solides. En déduire, sans le développer l'expression du MGD.

**Question 3.2 :** A l'aide d'une fonction dédiée, implémenter sous Matlab le MGD. Dans un script dédié, comparer les résultats simulés sur quelques configurations :
- aux valeurs affichées sur le panel de contrôle du robot ;
- aux valeurs simulées dans RoboDK.


## construction du Modèle Cinématique Direct (MCD) - (S'il reste du temps ...)

**Question 4.1 :** A partir de la formulation différentielle (variationnelle) du MGD, formuler le MCD.

**Question 4.2 :** Implémenter sousMatlab dans une fonction dédiée à cet effet le MCD, en se basant uniquement sur la fonction MGD précédemment développée.



## Documents ressources

Les pages suivantes regroupent un certain nombre de documents permettant d'appréhender le fonctionnement du système ainsi que ses composants technologiques.

[Notice d'allumage/arrêt du robot UR10](img/TP_UR10/UR10dem.pdf)

```{figure} img/TP_UR10/UR10para.png
---
width: 500px
name: UR10para
--- 
Paramètres donnés par le constructeur
```

```{figure} img/TP_UR10/UR10joint.png
---
width: 300px
name: UR10joint
--- 
Configuration et dénomination des corps et liaisons
```

```{figure} img/TP_UR10/UR10doc.png
---
width: 600px
name: UR10doc
--- 
Extrait de la documentation utilisateur
```
