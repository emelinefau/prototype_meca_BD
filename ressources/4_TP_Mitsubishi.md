# TP : Étude d'un robot sériel - Misubishi RV-4FL

Le robot Mitsubishi RV-4FL est un robot sériel anthropomorphe 6 axes industriel particulièrement adapté aux opérations de « pick and place » présentant une dynamique élevée et une reproductibilité de $\pm 0.02 mm$ ({numref}`RV4FL`).

```{figure} img/TP_Mitsubishi/RV4FL.jpg
---
width: 400px
name: RV4FL
--- 
robot Mitsubishi RV-4FL
```

## Découverte et prise en main du système

L'objectif de cette partie est de découvrir la structure et le fonctionnement du robot par quelques manipulations.

**Question 1.1 :**  Effectuer la procédure de démarrage du robot fournie dans les documents ressource à la fin du sujet.

Réaliser quelques déplacements manuels pour assimiler les différents corps et liaisons du robot :
- dans le mode articulaire ;
- dans le repère de base du robot ;
- dans le repère associé à l'outil (effecteur).
  
**Question 1.2 :** En déduire comment sont situés le référentiel de base du robot et le référentiel associé à l'outil.

**Question 1.3 :** A partir de l'analyse de la documentation, expliquer quels sont les différents systèmes d'axes (repères) sur le robot ?

**Question 1.4 :** Par une analyse de la documentation fournie et par expérimentations :
- préciser quels sont les paramétrages des positions fournies par l'interface de pilotage (cartésien ? polaire ? sphérique ?) ;
- expliquer comment sont paramétrées les rotations (Euler ? Bryan ? quaternions ? extrinsèque ? intrinsèque ?).


## Modélisation géométrique

L'objectif de cette partie est d'analyser la géométrie du robot puis d'en proposer un modèle géométrique.

### Schéma cinématique

**Question 2.1 :** Réaliser un schéma cinématique, en 3D, dans la configuration « home » (dessin avec couleurs sur une page A4). Y positionner le référentiel de base du robot ainsi que celui de l'effecteur déterminé précédemment.

**Question 2.2 :** Quelle est la particularité de la structure de ce robot 6 axes ?


### Paramétrage DHm

**Question 2.3 :** Sur le modèle précédent, effectuer le paramétrage selon la convention dite de Denavit et Hartenberg modifiée. Synthétiser les résultats dans le tableau approprié.


### Confrontation à la modélisation dans l'application RoboDK

Depuis un fichier vierge, puis importer, depuis la librairie en ligne, le robot Mitsubishi RV-4FL. Éditer les paramètres du robot en double-cliquant sur le robot.

**Question 2.4 :** En masquant les référentiels inutiles et en agrandissant les flèches (menu « View - Make reference frames bigger »), déterminer le paramétrage et système d'axes du modèle du Mitsubishi RV4FL dans le logiciel.


## Problématiques de la génération et exécution de trajets

L'objectif de cette partie est d'aborder de manière concrète différentes difficultés liées au MGI des robots 6 axes pour l'exécution de programmes.


### Nombre de solutions du MGI

**Question 3.1 :** Choisir une configuration quelconque pour le robot, puis simuler la résolution du MGI correspondant à cette configuration de l'effecteur avec l'application RoboDK.

**Question 3.2 :** Réitérer la démarche pour différentes configurations. Quel est le nombre maximal de solution au MGI?

**Question 3.3 :** Analyser la documentation fournie sur les « configuration flag », puis expliquer leur fonctionnement et rôle.

**Question 3.4 :** Comment sont codées les « configuration flag », pour le robot?


### Singularités

**Question 3.5 :** A partir des exemples donnés dans la documentation, analyser la problématique liée au passage au voisinage ou au travers des points singuliers.

**Question 3.6 :** Mettre en oeuvre un essai par déplacement manuel pour illustrer le cas de l'exemple « G-H-I ».

**Question 3.7 :** Comparer d'un point de vue géométrique et cinématique s'il vaut mieux passer près ou au travers des singularités.


### Interpolation des positionnements

Le language de programmation du robot permet d'exprimer un déplacement entre deux configurations du robot (équivalentes à deux positionnements de l'effecteur dans le repère global).

**Question 3.8 :** Mettre en oeuvre le programme préparer à cet effet en présence de l'enseignant.

**Question 3.9 :** Analyser la structure du programme.

**Question 3.10 :** Par analyse Expliquer le principe de fonctionnement des instructions « Mvs » et « Mov » ainsi que leurs différences.

**Question 3.11 :** Quelles sont les conséquences sur la trajectoire effective de l'effecteur ? Expliquer par un raisonnement géométrique simple le résultat observé.


## Documents ressources

Les pages suivantes regroupent un certain nombre de documents permettant d'appréhender le fonctionnement du système ainsi que ses composants technologiques.

[Notice d'allumage/arrêt du robot Mitsubishi RV4-­FL + Notice de pilotage manuel](img/TP_Mitsubishi/RV4FL0.pdf)

[Documentation constructeur partiel (repère, singularité, flag ...)](img/TP_Mitsubishi/RV4FL1.pdf)