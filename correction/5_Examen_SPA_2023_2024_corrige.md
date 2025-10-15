# Correction de l'examen de Système Poly-Articulés - 2023/2024

On s'intéresse au robot spot produit par la société Boston Dynamics. Ce robot est composé de quatre jambes comprenant chacune 3 articulations. Le robot peut également être complété par un bras articulé au bout duquel se trouve une pince. Spot est un robot mobile agile qui navigue sur le terrain avec une mobilité sans précédent. Il permet ainsi d'automatiser des tâches d'inspection de routine et la capture de données de manière sûre, précise et fréquente. 

Une description des composants du robot et de la pince sont donnés en annexe.
 
```{figure} img/Examen_2023_2024/spot-payloads-mobile.png
---
width: 400px
--- 
Robot Spot + bras articulé
```

## Étude d'une jambe : modèle géométrique direct

Le robot est composé de 4 jambes identiques. Ces 4 jambes sont reliées au corps du robot et sont chacune composées d'une hanche (hip), d'une jambe supérieure et d'une jambe inférieure (cf. {numref}`spot1c`). Les jambes ainsi que leurs composants sont désignés par leurs positions sur le robot "$fl$" pour front left "$bl$" pour back left et idem pour "$fr$" et "$br$". Ces dénominations seront utilisées dans le paramétrage du robot. La distance entre les centres des articulations de la hanche (rouge) est nommée $h_1$, la distance entre les articulations de la jambe supérieure (bleu) est notée $h_2$ et la distance entre l'articulation et le pied (vert) est notée $h_3$. La position du point $O_{fl}$ dans le repère ($O_{0}, \overrightarrow{x_0}, \overrightarrow{y_0}, \overrightarrow{z_0}$) est notée ($a_{fl}, b_{fl}, c_{fl}$). Les pieds sont considérés comme des portions de sphère et leurs centres sont désignés par les points $F_{fl}$, $F_{bl}$ ...    


```{figure} img/Examen_2023_2024/spot2.png
---
width: 500px
name: spot2c
--- 
Spot : schéma cinématique partiel 
```

**Question 1.1 :** Construire sur le document réponse le paramétrage au sens de Denavit Hartenberg modifié (DHm) en partant du point $O_{fl}$. On considèrera le repère de base de la jambe comme étant ($O_{fl}, \overrightarrow{x_0}, \overrightarrow{y_0}, \overrightarrow{z_0}$).

```{figure} img/Examen_2023_2024/spot3.png
---
width: 300px
name: spot3c
--- 
Spot : schéma cinématique jambe avant gauche.
```

À titre indicatif : dans la {numref}`spot3c` le trait en pointillé passant par $O_{fl}$ est parallèle au vecteur $\overrightarrow{x_0}$. 

````{admonition} Solution

```{figure} img/Examen_2023_2024/spot3correction.png
---
width: 300px
--- 
```

````


**Question 1.2 :** Synthétiser les résultats dans le tableau DHm associé. Dessiner également les figures de changement de repère en représentant les différents paramètres articulaires comme étant positif.
 

````{admonition} Solution
Tableau de paramètres DHm pour le robot


|      | $d_i$ | $\alpha_i$ | $r_i$ | $\theta_i$ | 
|:----:|:-----:|:----------:|:-----:|:----------:|
| $\mathbf{T}_{01}$ | 0 | $-90^{\circ}$ | 0 | $\theta_1$ |  
| $\mathbf{T}_{12}$ | 0 | $90^{\circ}$  | $h_1$ | $\theta_2$ |
| $\mathbf{T}_{23}$ | $h_2$ | 0 | 0 | $\theta_3$ |

```{figure} img/Examen_2023_2024/Q_2.png
---
width: 300px
--- 
```

````
	
**Question 1.3 :** Déterminer les matrices homogènes de transformation $T_{ij}$ entre les différents corps.
 

````{admonition} Solution
Matrices homogènes élémentaires de transformations entre repères :

$$
\begin{align*}
	\mathbf{T}_{01}&=
    \begin{bmatrix}
    	1 & 0 & 0 & 0 \\
		0 & \text{C}\alpha_1 & -\text{S}\alpha_1 & 0 & 0 \\
		0 &\text{S}\alpha_1 &  \text{C}\alpha_1 & 0 & 0 \\
		0 & 0 & 0 & 1\\
    \end{bmatrix} \times
    \begin{bmatrix}
		\text{C}\theta_1 & -\text{S}\theta_1 & 0 & 0 \\
		\text{S}\theta_1 &  \text{C}\theta_1 & 0 & 0 \\
		0 & 0 & 1 & 0 \\
		0 & 0 & 0 & 1\\
    \end{bmatrix}  
	\\
	\\
	\mathbf{T}_{01}&=
	\begin{bmatrix}
		\text{C}\theta_1 & -\text{S}\theta_1 & 0 & 0 \\
		0 & 0 & 1 & 0 \\
		-\text{S}\theta_1 &  -\text{C}\theta_1 & 0 & 0 \\
		0 & 0 & 0 & 1\\
    \end{bmatrix}
    \\
    \\
	\mathbf{T}_{12}&=
    \begin{bmatrix}
    	1 & 0 & 0 & 0 \\
		0 & \text{C}\alpha_2 & -\text{S}\alpha_2 & 0 & 0 \\
		0 &\text{S}\alpha_2 &  \text{C}\alpha_2 & 0 & 0 \\
		0 & 0 & 0 & 1\\
    \end{bmatrix} \times
    \begin{bmatrix}
		\text{C}\theta_2 & -\text{S}\theta_2 & 0 & 0 \\
		\text{S}\theta_2 &  \text{C}\theta_2 & 0 & 0 \\
		0 & 0 & 1 & h_1 \\
		0 & 0 & 0 & 1\\
    \end{bmatrix}  
	\\
	\\
	\mathbf{T}_{12}&=
	\begin{bmatrix}
		\text{C}\theta_2 & -\text{S}\theta_2 & 0 & 0 \\
		0 & 0 & -1 & -h_1 \\
		\text{S}\theta_2 &  \text{C}\theta_2 & 0 & 0 \\
		0 & 0 & 0 & 1\\
    \end{bmatrix}
    \\
    \\  
	\mathbf{T}_{23}&=
	\begin{bmatrix}
		\text{C}\theta_3 & -\text{S}\theta_3 & 0 & h_2 \\
		\text{S}\theta_3 &  \text{C}\theta_3 & 0 & 0 \\
		0 & 0 & 1 & 0 \\
		0 & 0 & 0 & 1\\
    \end{bmatrix}
\end{align*}
$$

````

**Question 1.4 :** En déduire l'expression du modèle géométrique direct (MGD) permettant d'exprimer la position du pied avant gauche ($x_{fl},y_{fl},z_{fl}$) dans le repère du robot ($O_{fl}, \overrightarrow{x_0}, \overrightarrow{y_0}, \overrightarrow{z_0}$). Rappeler quels sont les paramètres de l'espace des tâches et les paramètres de l'espace articulaire.
 

````{admonition} Solution

$$
\begin{align*}
\begin{pmatrix}
x_{fl} \\ y_{fl} \\ z_{fl} \\ 1
\end{pmatrix}
&= \mathbf{T}_{01} \cdot \mathbf{T}_{12} \cdot  \mathbf{T}_{23} \cdot  
\begin{pmatrix}
h_3 \\ 0 \\ 0 \\ 1
\end{pmatrix} \\
\\
\begin{pmatrix}
x_{fl} \\ y_{fl} \\ z_{fl} \\ 1
\end{pmatrix}
&=  \mathbf{T}_{01} \cdot  \mathbf{T}_{12} \cdot   
\begin{pmatrix}
h_{3}\text{C}\theta_3 + h_2 \\h_{3}\text{S}\theta_3 \\ 0 \\ 1
\end{pmatrix} \\
\\
\begin{pmatrix}
x_{fl} \\ y_{fl} \\ z_{fl} \\ 1
\end{pmatrix} &= \mathbf{T}_{01} \cdot
\begin{pmatrix}
h_{3}\text{C}(\theta_3+\theta_2)+h_2\text{C}\theta_2 \\ -h_1 \\h_{3}\text{S}(\theta_3+\theta_2)+h_2\text{S}\theta_2 \\ 1
\end{pmatrix}\\
\\
\begin{pmatrix}
x_{fl} \\ y_{fl} \\ z_{fl} \\ 1
\end{pmatrix} &= 
\begin{pmatrix}
(h_{3}\text{C}(\theta_3+\theta_2)+h_2\text{C}\theta_2)\text{C}\theta_1+h_1\text{S}\theta_1 \\h_{3}\text{S}(\theta_3+\theta_2)+h_2\text{S}\theta_2 \\ -(h_{3}\text{C}(\theta_3+\theta_2)+h_2\text{C}\theta_2)\text{S}\theta_1+h_1\text{C}\theta_1  \\ 1
\end{pmatrix} 
\end{align*}
$$

````

**Question 1.5 :** Déterminer par le calcul les singularités de cette structure. Expliquer les solutions trouvées par des croquis pour expliquer le sens physique. 


````{admonition} Solution
Pour déterminer les singularités on calcul la jacobienne du MGD :

$$
\begin{align*}
J &=
\begin{bmatrix}
		-(h_{3}\text{C}(\theta_3+\theta_2)+h_2\text{C}\theta_2)\text{S}\theta_1+h_1\text{C}\theta_1 & (-h_{3}\text{S}(\theta_3+\theta_2)-h_2\text{S}\theta_2)\text{C}\theta_1 & -h_{3}\text{S}(\theta_3+\theta_2)\text{C}\theta_1 \\
		0 & h_{3}\text{C}(\theta_3+\theta_2)+h_2\text{C}\theta_2 & h_{3}\text{C}(\theta_3+\theta_2) \\
		-(h_{3}\text{C}(\theta_3+\theta_2)+h_2\text{C}\theta_2)\text{C}\theta_1-h_1\text{S}\theta_1 & (h_{3}\text{S}(\theta_3+\theta_2)+h_2\text{S}\theta_2)\text{S}\theta_1 & h_{3}\text{S}(\theta_3+\theta_2)\text{S}\theta_1 \\
\end{bmatrix}
\end{align*}
$$

On calcul ensuite le déterminant de cette matrice. Après simplification, on trouve :

$$
\begin{equation*}
 det(J) =  -h_2 h_3\text{S}\theta_3(h_2\text{C}\theta_2 + h_3\text{C}(\theta_2 + \theta_3))
\end{equation*}
$$

Les singularité correspondent au solution de l'équation $det(J) = 0$. On trouve ici facilement $\theta_3 = 0\, [\pi]$. 

Cette solution correspond au moment ou la jambe est soit tendu $\theta_3 = 0$ soit la jambe est entièrement replié $\theta_3 = 180 deg$. Les deux solutions ne sont pas atteignable physiquement si l'on regarde les limitations articulaires données dans l'annexe. 

````

## Étude d'une jambe : modèle géométrique inverse 

**Question 2.1 :** En vous aidant de l'annexe 5.2, déterminer le modèle géométrique inverse en position uniquement permettant de relier les valeurs de $\theta_i$ aux valeurs ($x_{fl},y_{fl},z_{fl}$).
 

````{admonition} Solution
On aura besoin des matrices inverses $\mathbf{T}_{10}$ et $\mathbf{T}_{21}$

$$
\begin{align*}
	\mathbf{T}_{10}&=
	\begin{bmatrix}
		\text{C}\theta_1 & 0 & -\text{S}\theta_1 & 0 \\
		-\text{S}\theta_1 & 0 & -\text{C}\theta_1  & 0 \\
		0 & 1 & 0 & 0 \\
		0 & 0 & 0 & 1\\
    	\end{bmatrix}
	\\
	\\
	\mathbf{T}_{12}&=
	\begin{bmatrix}
		\text{C}\theta_2 & 0 &  \text{S}\theta_2 & 0 \\
		-\text{S}\theta_2 & 0 & \text{C}\theta_2 & 0 \\
		0 & -1 & 0 & -h_1 \\
		0 & 0 & 0 & 1\\
    	\end{bmatrix}
\end{align*}  
$$

Résolution en utilisant la méthode de Paul : 

**1 - Première étape :**

$$
\begin{align*}
\begin{pmatrix}
x_{fl} \\ y_{fl} \\ z_{fl} \\ 1
\end{pmatrix}
&= \mathbf{T}_{01} \cdot \mathbf{T}_{12} \cdot  \mathbf{T}_{23}  \cdot 
\begin{pmatrix}
h_3 \\ 0 \\ 0 \\ 1
\end{pmatrix} \\
\\
\mathbf{T}_{10} \cdot
\begin{pmatrix}
x_{fl} \\ y_{fl} \\ z_{fl} \\ 1
\end{pmatrix}
&=  \mathbf{T}_{12} \cdot   
\begin{pmatrix}
h_{3}\text{C}\theta_3 + h_2 \\h_{3}\text{S}\theta_3 \\ 0 \\ 1
\end{pmatrix} \\
\\
\begin{pmatrix}
x_{fl}\text{C}\theta_1 - z_{fl}\text{S}\theta_1 \\ - x_{fl}\text{S}\theta_1  - z_{fl}\text{C}\theta_1 \\ y_{fl} \\ 1
\end{pmatrix} &=   
\begin{pmatrix}
h_{3}\text{C}(\theta_3+\theta_2)+h_2\text{C}\theta_2 \\ -h_1 \\h_{3}\text{S}(\theta_3+\theta_2)+h_2\text{S}\theta_2 \\ 1
\end{pmatrix} \qquad \qquad 
\begin{matrix}
~ \\ (2) \\ ~ \\  ~
\end{matrix}    
\end{align*}
$$

La seconde équation du système dépend uniquement de $\theta_1$. Cette équation correspond à une équation de type 2 (cf. annexe) avec $X = -x_{fl}$, $Y = -z_{fl}y$ et $Z = -h_1$ Cette équation admet deux solutions avec $\varepsilon = \pm 1$ (cf. annexe)

**2 - Deuxième étape :**

La variable articulaire $\theta_1$ est maintenant connue. Pour simplifier les notations on pose donc : $a = x_{fl}\text{C}\theta_1 - z_{fl}\text{S}\theta_1 $ et $b = - x_{fl}\text{S}\theta_1  - z_{fl}\text{C}\theta_1$

$$
\begin{align*}
\mathbf{T}_{21} \cdot    \begin{pmatrix}
a \\ b \\ y_{fl} \\ 1
\end{pmatrix} &=  
\begin{pmatrix}
h_{3}\text{C}\theta_3 + h_2 \\h_{3}\text{S}\theta_3 \\ 0 \\ 1
\end{pmatrix} \\
\\
\begin{pmatrix}
a\text{C}\theta_2 +y_{fl}\text{S}\theta_2 \\ -a\text{S}\theta_2 -y_{fl}\text{C}\theta_2  \\ -b-h_1 \\ 1
\end{pmatrix} &=  
\begin{pmatrix}
h_{3}\text{C}\theta_3 + h_2 \\h_{3}\text{S}\theta_3 \\ 0 \\ 1
\end{pmatrix} \qquad \qquad 
\begin{matrix}
(1) \\ (2) \\ ~ \\  ~
\end{matrix} 
\end{align*}
$$

Les équations (1) et (2) du système correspondent à des équations de type 6 . La méthode de résolution est donnée en annexe et permet dans un premier temps de déterminer $\theta_2$ par un e équation de type 2 qui admet 2 solutions et dans un second temps de déterminer $\theta_3$ par un système d'équation de type 3 (cf. annexe) qui lui admet une unique solution. 
````


**Question 2.2 :** Donner le nombre de configurations articulaires possibles pour une même position de l'effecteur (pied) sans tenir compte des limites articulaires. N'hésitez pas à expliquer votre raisonnement par des figures si nécessaire. 


````{admonition} Solution
La question précédente permet de dire qu'il existe 2 solutions pour $\theta_1$, 2 solutions pour $\theta_2$ et 1 solution pour $\theta_3$. Ainsi il existe 4 configurations articulaires possible pour une même position du pied. Les figures suivantes illustre ces 4 configurations :

```{figure} img/Examen_2023_2024/correction1.png
---
width: 600px
--- 
```
	
````

**Question 2.3 :** Les limites de chaque articulation sont données par le constructeur en annexe 5.1. En vous appuyant sur ces données, déterminez les relations entre les paramètres articulaires constructeurs et vos paramètres articulaires.
 

````{admonition} Solution
Sur le paramétrage actuel on a  : 

$$
\begin{align*}
\theta_1 &= \theta_h - \dfrac{\pi}{2} \\
\theta_2 &= \theta_u - \dfrac{\pi}{2}\\
\theta_3 &= \theta_l
\end{align*}
$$

Le plus simple pour cela est de calculer les limites articulaires au niveau de $\theta_1$, $\theta_2$, $\theta_3$ et de vérifier quel corresponde bien à la description donné dans l'annexe. 
````

**Question 2.4 :** En tenant compte des limites articulaires, donner le nombre de configurations articulaires possibles pour une même position de l'effecteur (pied) ($x_{fl},y_{fl},z_{fl}$) dans le repère du robot ($O_{fl}, \overrightarrow{x_0}, \overrightarrow{y_0}, \overrightarrow{z_0}$).
 

````{admonition} Solution
En tenant compte des limites articulaire il reste une seul solution articulaire possible. Effectivement la limitation sur $\theta_3$ supprime tout de suite les deux solutions ou le genou est devant la droite entre le pied et l'articulation 2. La dernière configuration articulaire est supprimer par la limitation articulaire sur $\theta_1$ qui n'autorise pas le renversement de l'articulation (cf. corrigé question 2.2). 

Le système est donc prévue pour ne pas avoir accès à ces zones de singularités et avoir une seule configuration articulaire possible, cela facilite énormément la commande des pieds. 
````


## Étude préliminaire du système complet

On s'intéresse maintenant au robot en considérant les pieds comme fixes. On souhaite orienter et positionner le corps du robot ($O_{0}, \overrightarrow{x_0}, \overrightarrow{y_0}, \overrightarrow{z_0}$) par rapport a un repère $\mathcal{R}_f$ fixe liée au sol ($O_{f}, \overrightarrow{x_f}, \overrightarrow{y_f}, \overrightarrow{z_f}$). Les positions des 4 points F dans le repère $\mathcal{R}_f$ sont connues. On considère que le MGI et le MGD des jambes sont connus. 

**Question 3.1 :** Donner les paramètres de l'espace des taches et les paramètres de l'espace articulaire puis décrire de manière détaillée sans faire de calcul la méthode permettant d'obtenir le MGI du système entier (sans prendre en compte le bras articulé et la pince).
 

````{admonition} Solution
Les paramètres de l'espace des taches corresponde à la position et l'orientation du repère $\mathcal{R}_0$ par rapport au repère $\mathcal{R}_f$. Il sont donc au nombre de 6 (3 translations et 3 rotations). Les paramètres articulaires sont au nombre de 12. Il s'agit des $4\times 3$ articulations des jambes. 

Pour obtenir le MGI du système il est nécessaire dans un premier temps de calculer dans le repère $\mathcal{R}_f$ les coordonnées des 4 points $O_{fl}$, $O_{fb}$. Cette étape est facile etant donnée que l'on connait la position des différents point dans le repère $\mathcal{R}_0$ ainsi que la position et l'orientation du repère $\mathcal{R}_0$ par rapport à $\mathcal{R}_f$

Dans un second temps, une fois les coordonnées de ces 4 points $O_{fl}$, $O_{fb}$ ... obtenus, il suffit d'appliquer le MGI de chaque pied. Effectivement le problème revient a trouver les valeurs des 3 articulation sur chaque jambe pour que celle-ci donne $x_fl = \overrightarrow{O_{fl}F_{fl}}\cdot \overrightarrow{x_0}$, $y_fl = \overrightarrow{O_{fl}F_{fl}}\cdot \overrightarrow{y_0}$ et $y_fl = \overrightarrow{O_{fl}F_{fl}}\cdot \overrightarrow{z_0}$ idem pour les 3 autres jambes.

````

**Question 3.2 :** Le paramétrage permettant de définir l'orientation du corps du robot dans son environnement correspond à un paramétrage au sens de Tait Bryan (rotations X, Y', Z''). S'agit-il d'un paramétrage extrinsèque ou intrinsèque ? Justifier.
 

````{admonition} Solution
Il s'agit d'un paramétrage avec des rotations intrinsèques étant donné que l'on tourne autour des axes de la nouvelle base à chaque rotation. 
````

**Question 3.3 :** Le fait d'assimiler le pied à un point présente-t-il un problème dans le paramétrage du robot. Justifier votre réponse. 
 

````{admonition} Solution
Les points d'appuis réels des pieds sont toujours la projection orthogonale des points $F$ suivant la normale au sol. Le fait d'assimiler les pieds à un point n'est donc pas gênant si le robot est sur un plan étant donné que les pieds sont des portions de sphères. Effectivement, si le sol est plan les points $F$ constitue juste des translations des points d'appuis réels. Par contre cela pose un soucis si le sol n'est pas plan. 
````


## Étude du bras articulé additionnel sans la pince

Dans cette dernière partie on s'intéresse uniquement au bras articulé représenté dans les {numref}`arm2c` et {numref}`arm1c`.

**Question 4.1 :** Combien de degrés de liberté possède le bras articulé sans tenir compte de la pince. 
 

````{admonition} Solution
Le bras robotique possèdent 6 degrés de liberté du fait de ses 6 liaisons pivots. La septième articulation correspond à l'ouverture ou la fermeture de la pince et n'est donc pas une articulation du bras robotique. 
````

**Question 4.2 :** En supposant connues toutes les matrices de transformation ($T_{ij}$) permettant de décrire le paramétrage géométrique du bras au sens de DHm, décrire précisément la démarche de résolution du MGI sans faire de calcul.   
 

````{admonition} Solution
Ce bras est une structure sériel 6 axes. Les 3 dernier axes constitues un poignet (3 liaisons pivot concourante). Ainsi il est possible de découpler le problème de résolution du MGI en 2 sous problème. Le premier problème consiste a résoudre le problème en position sur le point $0_4 = 0_5 = 0_6$. Ce problème permet de déterminer les 3 premier paramètre articulaire. Ensuite il faut résoudre le problème en orientation afin de déterminer les 3 paramètres articulaire restant. Pour résoude cela on applique la méthode de résolution de Paul. 
````


## Annexes

### Limites articulaires :

Limites articulaires de chaque jambe (les notations utilisées dans ce paragraphe ne sont utiles que pour la question 2.3): 
- articulation 1 entre le corps et la hanche  $\theta_h$ : $\pm$ 45 degrés par rapport au plan $(O_{fl},\overrightarrow{x_0},\overrightarrow{y_0})$
- articulation 2 entre la hanche et la jambe supérieure $\theta_u$ : entre + 41 et - 141 degrés par rapport à l'horizontale lorsque l'articulation 1 est a $\theta_h = 0$.
- articulation 3 au niveau du genou entre la jambe supérieure et la jambe inférieure $\theta_l$: entre -14 et - 160 degrés par rapport à la jambe tendue (flexion/extension de 14 à 160 degrés)

### Équations :

**Inverse d'une matrice homogène :**

$$
\begin{equation*}
\mathbf{T}_{ij} = 
		\begin{bmatrix}
		 & & &  \\
		 &  \mathbf{R}_{ij} &  & \mathbf{t}_{ij} \\
		 & &  &  \\
		0 & 0 & 0 & 1\\
    	\end{bmatrix}
\longrightarrow  
 \mathbf{T}_{ji} =
		\begin{bmatrix}
		 & & &  \\
		 &  \mathbf{R}_{ij} ^t &  & -\mathbf{R}_{ij} ^t \mathbf{t}_{ij} \\
		 & &  &  \\
		0 & 0 & 0 & 1\\
    	\end{bmatrix}	
\end{equation*}
$$

**Solutions de l'équation de type 2 :**

$$
\begin{equation*}
X \text{S}\theta_i + Y \text{C}\theta_i = Z
\end{equation*}
$$

Solution :

$$
\begin{align*}
\theta_i = 
\begin{cases}
\text{atan2}(\pm \sqrt{1 - \text{C}^2\theta_i},\, \text{C}\theta_i) \quad & \text{si} \quad X = 0 \text{ et } Y \ne 0 \\
\text{atan2}(\text{S}\theta_i, \, \pm \sqrt{1 - \text{S}^2\theta_i}) \quad & \text{si} \quad X \ne 0 \text{ et } Y = 0 \\
\begin{cases}
\theta_{i1} = \text{atan2}(-Y,X) \\
\theta_{i2} = \theta_{i1} + 180\deg
\end{cases}  \quad & \text{si} \quad X \ne 0 \text{ et } Y \ne 0 \text{ et } Z = 0 \\
\text{atan2}(\text{S}\theta_i, \, \text{C}\theta_i) \quad & \text{si} \quad X \ne 0 \text{ et } Y \ne 0 \text{ et } Z \ne 0 \text{ et } X^2+Y^2 \geq Z^2 \\
\text{configuration singulière} \quad & \text{si} \quad X \ne 0 \text{ et } Y \ne 0 
\end{cases}
\end{align*}
$$

Dans le cas où $X \ne 0$ et $Y \ne 0$ et $Z \ne 0$, l'équation est résolue en élevant l'expression au carré : en remplaçant les termes en sinus par les fonctions équivalentes en cosinus, on aboutit à une équation du second degré à résoudre donnant la valeur du cosinus. Un raisonnement analogue est mené pour déterminer  le terme en sinus :

$$
\begin{equation*}
\begin{cases}
\text{C}\theta_i = \dfrac{YZ - \varepsilon X \sqrt{X^2+Y^2-Z^2}}{X^2 + Y^2} \\
\text{S}\theta_i = \dfrac{XZ + \varepsilon Y \sqrt{X^2+Y^2-Z^2}}{X^2 + Y^2} \\
\end{cases}
\qquad \text{avec} \qquad \varepsilon = \pm 1
\end{equation*}
$$

Dans ce cas, la résolution de l'équation donne deux solutions, correspondant aux valeurs de $\varepsilon$.

**Solutions de l'équation de type 6 :**

$$
\begin{equation*}
\begin{cases}
W\text{S}\theta_j = X\text{C}\theta_i + Y \text{S}\theta_i + Z_1 \\
W\text{C}\theta_j = X\text{S}\theta_i - Y \text{C}\theta_i + Z_2 \\
\end{cases}
\end{equation*}
$$

Solution :
Elle consiste à élever au carré chaque équation pour faire disparaître $\theta_j$ en les additionnant.$\theta_i$ est alors résolu par une équation de type 2. Ensuite, connaissant $\theta_i$, $\theta_j$ est déterminé par un système d'équations de type 3.

**Solutions de l'équation de type 3 :**

$$
\begin{equation*}
\begin{cases}
X_1\text{s}\theta_i + Y_1 \text{c}\theta_i = Z_1 \\
X_2\text{S}\theta_i + Y_2 \text{C}\theta_i = Z_2 \\
\end{cases}
\end{equation*}
$$

Dans le cas où $X_1 Y_2 - X_2 Y_1 \neq 0$, les termes en cosinus et sinus sont obtenus par
combinaison linaire des deux équations pour éliminer respectivement les termes sinus et
cosinus :

$$
\begin{equation*}
\begin{cases}
\text{C}\theta_i = \dfrac{Z_2 X_1 - Z_1 X_2}{X_1 Y_2 - X_2 Y_1} \\
\text{S}\theta_i = \dfrac{Z_1 Y_2 - Z_2 Y_1}{X_1 Y_2 - X_2 Y_1} \\
\end{cases}
\end{equation*}
$$

Dans le cas où $X_1 Y_2 - X_2 Y_1 = 0$ alors, les équations ne sont plus indépendantes ; on
choisit alors l’une des deux équations que l’on résout en équation de type 2.
Solution :

$$
\begin{align*}
\theta_i = 
\begin{cases}
\text{atan2}(\text{S}\theta_i, \, \text{C}\theta_i) \quad  & \text{si} X_1 Y_2 - X_2 Y_1 \neq 0 \\\text{atan2}(\dfrac{Z_1}{X_1} \, \dfrac{Z_2}{Y_2} ) \quad  & \text{si} Y_1 = 0 \text{ et } X_2 = 0 \\
\end{cases}
\end{align*}
$$

```{figure} img/Examen_2023_2024/arm-diagrams-02.png
---
width: 500px
name: arm2c
--- 
Bras articulé : vue de dessus et vue de face
```

```{figure} img/Examen_2023_2024/arm-diagrams-03.png
---
width: 400px
name: arm1c
--- 
Bras articulé : vue de côté
```

```{figure} img/Examen_2023_2024/spotanatomy.png
---
width: 600px
name: spot1c
--- 
Spot : description des composants
```

```{figure} img/Examen_2023_2024/DHm.png
---
width: 400px
name: EX_2024_DHmc
--- 
Paramétrage de DHm
```

```{figure} img/Examen_2023_2024/spot3.png
---
width: 300px
--- 
```

```{figure} img/Examen_2023_2024/spot3.png
---
width: 300px
--- 
```