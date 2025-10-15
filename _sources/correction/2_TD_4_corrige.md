# Correction du TD n°4 : Modes d'interpolation des trajets

On étudie le centre d'usinage 4 axes Realméca de l'atelier de fabrication du DGM. C'est un centre d'usinage à broche horizontale possédant 3 axes de translation de variables $X_m$, $Y_m$, $Z_m$ ainsi qu'un axe de rotation au niveau du plateau de variable $B$. La modélisation cinématique est donnée en {numref}`cin_C300H_c`.

```{figure} img/TD4/schema_cin.png
---
width: 300px
name: cin_C300H_c
--- 
Modélisation cinématique du centre 4 axes C300H
```

Pour la suite, on ne tiendra pas compte de la rotation de l'outil réalisé par la broche (mouvement de coupe pour l'usinage).

- $\mathcal{R}_p=(O_p, \overrightarrow{x_p}, \overrightarrow{y_p}, \overrightarrow{z_p})$ le repère associé à la pièce posée sur le plateau;
- $\mathcal{R}_m=(O_m, \overrightarrow{x_m}, \overrightarrow{y_m}, \overrightarrow{z_m})$ le repère associé au centre d'usinage, orienté par les différents axes;
- l'axe $\overrightarrow{z_m}$ est l'axe de la broche, orienté s'éloignant de la pièce;
- le point $O_o$ est l'intersection entre l'axe de rotation B et la face supérieure du plateau.

Dans la configuration de référence du centre d'usinage (notamment l'axe $B$ à zéro), on positionne la pièce sur le plateau tel que la base du repère pièce $\mathcal{B}_p$ soit identique à la base machine $\mathcal{B}_m$.

Le paramétrage du système ainsi que les matrices homogènes de transformations entre repères sont données en annexe.

Le positionnement de l'outil par rapport à la pièce est spécifié par les composantes de position et les cosinus directeurs ($X_p,Y_p,Z_p,i,k$).

## Modèles Géométriques Direct et Inverse

**Question 1.1 :** Rappeler les variables de l'espace des tâches et celles de l'espace articulaire.

````{admonition} Solution

```{figure} img/TD4/MGD_MGI.png
---
width: 300px
--- 
```
	
Pour ce robot, la position et l'orientation de l'organe terminal sont caractérisées par :

- 3 composantes pour la position : $X_p$, $Y_p$, $Z_p$
- 2 composantes pour l'orientation : $i$, $k$ avec $\sqrt{i^2+k^2} = 1$ :  effectivement l'orientation de l'outil est toujours perpendiculaire à $\overrightarrow{y_p}$ d'ou $j = 0$ et le vecteur est unitaire d'où la relation entre $i$ et $k$.

Soit $\mathbf{X} = (X_p, Y_p, Z_p, i, 0, k)$ le vecteur contenant les paramètres de l'espace des tâches et $\mathbf{q} = (X_m, Y_m, Z_m, B)$ le vecteur contenant les paramètres de l'espace articulaire. Le 0 des paramètres de l'espace des tâches n'est pas obligatoire. Il est ici uniquement pour bien distinguer les 3 paramètres de position et les 3 (2) paramètres d'orientation.

Modèle géométrique directe : 

$$
\begin{equation*}
\mathbf{X} = f_{MGD}(\mathbf{q})
\end{equation*}
$$

Modèle géométrique inverse : 

$$
\begin{equation*}
\mathbf{q} = f_{MGI}(\mathbf{X})
\end{equation*}
$$

```{figure} img/TD4/ch_rep.png
---
width: 200px
--- 
```

````

**Question 1.2 :** À partir de la présentation du sujet et des annexes, déterminer les MGD et MGI du centre d'usinage.

````{admonition} Solution

**1** - Détermination du MGD

$$
\begin{equation*}
~^p\mathbf{P} = \mathbf{T}_{pm} \cdot ~^m\mathbf{P} \qquad \qquad ~^p\mathbf{v} = \mathbf{T}_{pm} \cdot ~^m\mathbf{v}
\end{equation*}
$$

MGD en position :  

On prend un point $P$ défini par une position quelconque dans l' espace articulaire.

$$
\begin{equation*}
\begin{pmatrix} X_p \\ Y_p \\ Z_p \\ 1 \end{pmatrix} =
\begin{pmatrix}
          	\text{C}B & 0 & \text{S}B & - d_x - p_x \ \text{C}B - (p_z+j_z) \ \text{S}B \\
  		0             & 1 & 0             & - d_y - p_y \\
	        -\text{S}B & 0 & \text{C}B & - d_z + p_x \ \text{S}B - (p_z+j_z) \ \text{C}B \\
       		0 & 0 & 0 & 1\\
\end{pmatrix} \cdot \begin{pmatrix} X_m \\ Y_m \\ Z_m \\ 1 \end{pmatrix}
\end{equation*}
$$

MGD en orientation :

On prend un vecteur $v$ représentant l'orientation de l'outil dans le repère machine. En choisissant d'utiliser un vecteur, on utilise seulement la matrice de rotation qui fait intervenir uniquement le paramètre $B$. 

$$
\begin{equation*}
\begin{pmatrix} i \\ 0 \\ k \\ 1 \end{pmatrix} =
\begin{pmatrix}
          	\text{C}B & 0 & \text{S}B & - d_x - p_x \ \text{C}B - (p_z+j_z) \ \text{S}B \\
  		0             & 1 & 0             & - d_y - p_y \\
	        -\text{S}B & 0 & \text{C}B & - d_z + p_x \ \text{S}B - (p_z+j_z) \ \text{C}B \\
       		0 & 0 & 0 & 1\\
\end{pmatrix} \cdot \begin{pmatrix} 0 \\ 0 \\1 \\ 0 \end{pmatrix}
\end{equation*}
$$

On trouve donc le MGD :

$$
\begin{equation*}
\begin{cases}
X_p = X_m \text{C}B + Z_m \text{S}B - d_x - p_x \text{C}B - (p_z+j_z)  \text{S}B\\
Y_p = Y_m - d_y - p_y\\
Z_p = - X_m \text{S}B + Z_m \text{C}B - d_z + p_x \text{S}B - (p_z+j_z) \text{C}B \\
i = \text{S}B \\
k = \text{C}B \\
\end{cases}
\end{equation*}
$$

**2** - Détermination du MGI 

MGI en position : 

$$
\begin{equation*}
\begin{pmatrix} X_m \\ Y_m \\ Z_m \\ 1 \end{pmatrix} =
	\begin{bmatrix}
          	\text{C}B & 0 & -\text{S}B & p_x + d_x \ \text{C}B - d_z \ \text{S}B \\
  		0             & 1 & 0              & p_y + d_y \\
	        \text{S}B  & 0 & \text{C}B & (p_z+j_z) +  d_x \ \text{S}B + d_z \ \text{C}B \\
       		0 & 0 & 0 & 1\\
	\end{bmatrix} \cdot \begin{pmatrix} X_p \\ Y_p \\ Z_p \\ 1 \end{pmatrix}
\end{equation*}
$$

MGI en orientation : 

$$
\begin{equation*}
\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} =
	\begin{bmatrix}
          	\text{C}B & 0 & -\text{S}B & p_x + d_x \ \text{C}B - d_z \ \text{S}B \\
  		0             & 1 & 0              & p_y + d_y \\
	        \text{S}B  & 0 & \text{C}B & (p_z+j_z) +  d_x \ \text{S}B + d_z \ \text{C}B \\
       		0 & 0 & 0 & 1\\
	\end{bmatrix} \cdot \begin{pmatrix} i \\ 0 \\ k \\ 0 \end{pmatrix}
\end{equation*}	
$$

On cherche a déterminer $B$ en fonction de $i$ et $j$ pour obtenir le MGI. Pour cela, il est plus simple de partir des équations équations en orientation obtenir à partir du MGD.

Résolution de B : 	
	
$$
\begin{equation*}
\begin{cases}
i = \text{S}B \\
k = \text{C}B \\
\end{cases}
\end{equation*}
$$

```{figure} img/TD4/calcul_B.png
---
width: 300px
--- 
```


On trouve donc le MGI :

$$
\begin{equation*}
\begin{cases}
X_m = X_p \text{C}B  - Z_p \text{S}B + p_x + d_x \text{C}B - d_z \text{S}B \\
Y_m = Y_p + p_y + d_y\\
Z_m = X_p \text{S}B  + Z_p \text{C}B + (p_z+j_z) +  d_x \text{S}B + d_z \text{C}B\\
B = \text{atan2}(i,k) \Leftrightarrow B = 
\begin{cases}
\arctan(i/k) \textbf{ if } k>0 \\
\arctan(i/k)- \pi \textbf{ if } k<0 \\
B = 90\deg \text{ if } k = 0 \text{ and } i = 1 \\
B = -90\deg \text{ if } k = 0 \text{ and } i = -1
\end{cases}
\end{cases}
\end{equation*}
$$

````

On souhaite usiner un plan de longueur $L$, avec un outil hémisphérique piloté en son centre tout en faisant varier l'orientation de l'axe outil ({numref}`usinage_piece_c`). Pour cela, on construit une trajectoire allant du premier positionnement de l'outil $P_1$ incliné d'un angle $\alpha$ ($\alpha > 0$) par rapport à $\mathbf{z_p}$, au positionnement outil $P_2$ incliné d'un angle $-\alpha$.

```{figure} img/TD4/usinage_piece.png
---
width: 300px
name: usinage_piece_c
--- 
Présentation des différentes configurations de l'outil.
```

**Question 1.3 :** Pour chacun des cas $P_1$ et $P_2$, déterminer les valeurs des variables traduisant le positionnement de l'outil dans l'espace des tâches et dans l'espace articulaire.

````{admonition} Solution

```{figure} img/TD4/configuration.png
---
width: 500px
--- 
```

**1** - Configuration initiale :

Espace des tâches : $\mathbf{X}_1 = \begin{pmatrix} L/2 \\ \text{indéterminé} \\ 0 \\ \sin(\alpha) \\ 0 \\ \cos(\alpha)\end{pmatrix} \qquad \qquad$ espace articulaire : $\mathbf{q}_1 = \begin{pmatrix} X_m^1 \\ Y_m^1 \\ Z_m^1 \\ B^1 \end{pmatrix}$

Pour déterminer $\mathbf{q}_1 $ on utilise le MGI appliqué à $\mathbf{X}_1$. On trouve :

$$
\begin{equation*}
\mathbf{q}_1  = 
\begin{cases}
X_m^1 = \dfrac{L}{2} \text{C}\alpha + p_x + d_x \text{C}\alpha - d_z \text{S}\alpha\\
Y_m^1 = \text{Indéterminé}\\
Z_m^1 = \dfrac{L}{2} \text{S}\alpha + p_z + j_z + d_x \text{S}\alpha + d_z \text{C}\alpha\\
B^1 = \alpha
\end{cases}
\end{equation*}
$$

**2** - Configuration finale :

Espace des tâches : $\mathbf{X}_2 = \begin{pmatrix} -L/2 \\ \text{indéterminé} \\ 0 \\ -\sin(\alpha) \\ 0 \\ \cos(\alpha)\end{pmatrix} \qquad \qquad$ espace articulaire : $\mathbf{q}_2 = \begin{pmatrix} X_m^2 \\ Y_m^2 \\ Z_m^2 \\ B^2 \end{pmatrix}$

Pour déterminer $\mathbf{q}_2 $ on utilise le MGI appliqué à $\mathbf{X}_2$. On trouve :

$$
\begin{equation*}
\mathbf{q}_2  = 
\begin{cases}
X_m^2 = -\dfrac{L}{2} \text{C}\alpha + p_x + d_x \text{C}\alpha + d_z \text{S}\alpha\\
Y_m^2 = \text{Indéterminé}\\
Z_m^2 = \dfrac{L}{2} \text{S}\alpha + p_z + j_z - d_x \text{S}\alpha + d_z \text{C}\alpha\\
B^2 = -\alpha
\end{cases}
\end{equation*}
$$

**3** - Calcul de $B^1$ et $B^2$

$\alpha \in \left[0, \frac{pi}{2} \right[  \qquad \cos(\alpha) > 0 \Leftrightarrow k > 0$ d'ou : $B^1 = \alpha$ et $B^2 = -\alpha$

````

## Modes d'interpolation

**Question 2.1 :** Pour un trajet calculé par mode d'interpolation linéaire dans l'espace des tâches, représenter en fonction de l'abscisse curviligne du trajet, l'évolution des variables des tâches. Comment évoluent qualitativement les variables articulaires ?	

````{admonition} Solution

```{figure} img/TD4/interp_taches.png
---
width: 400px
--- 
```

````

**Question 2.2 :** Faire de même pour un mode d'interpolation linéaire dans l'espace articulaire.

````{admonition} Solution

```{figure} img/TD4/interp_articulaires.png
---
width: 400px
--- 
```

````

Pour faciliter l'écriture, on définit pour la suite le paramètre d'interpolation $u$, variant de 0 à 1.

**Question 2.3 :** Exprimer les deux équations vectorielles fonction de $u$ qui traduisent l'interpolation linéaire dans l'espace des tâches et l'espace articulaire en fonction des valeurs correspondantes associées à $P_1$ et $P_2$

````{admonition} Solution

Interpolation supposée linéaire

Dans l'espace des tâches

On passe de la configuration $\mathbf{X}_1$ à la configuration $\mathbf{X}_2$ ( point $P_1$ au point $P_2$ ) de manière linéaire :

$$
\begin{equation*}
\overrightarrow{O_pP}(u) = \overrightarrow{O_pP_1} + u \cdot \left( \overrightarrow{O_pP_2} - \overrightarrow{O_pP_1}\right)
\end{equation*}
$$

Dans l'espace des tâches

On passe de la configuration $\mathbf{q}_1$ à la configuration $\mathbf{q}_2$ de manière linéaire :

$$
\begin{equation*}
\begin{cases}
X_m(u) &= X_m^1 + u(X_m^2 - X_m^1) \\
Y_m(u) &= Y_m^1 + u(Y_m^2 - Y_m^1) \\
Z_m(u) &= Z_m^1 + u(Z_m^2 - Z_m^1) \\
B(u) &= B^1 + u(B^2 - B^1) \\
\end{cases}
\end{equation*}
$$

````

## Influence du mode d'interpolation

On cherche à déterminer l'effet dans l'espace des tâches du mode d'interpolation dans l'espace articulaire.

**Question 3.1 :** Exprimer l'écart géométrique généré au niveau du point piloté de l'outil pour toute valeur de $u$.

````{admonition} Solution

On s'intéresse uniquement à un écart de position. Par conséquent, dans la suite du TD on ne raisonnera que sur les 3 composantes de position.

Effet de l'interpolation linéaire dans l'espace articulaire, dans l'espace des tâches 

$$
\begin{align*}
\text{Ecart} &= \overrightarrow{P_{theorique}P_{atteint}}\\
&= \overrightarrow{O_p P_{lin-esp-art}} - \overrightarrow{O_p P_{lin-esp-piece}}\\
&= f_{MGD} \begin{pmatrix}
X_m(u)\\
Y_m(u)\\
Z_m(u)\\
B(u)\\
\end{pmatrix} - \left[ \overrightarrow{O_pP_1} + u \cdot \left( \overrightarrow{O_pP_2} - \overrightarrow{O_pP_1}\right) \right] \quad \forall u \in \left[0;1 \right]
\end{align*}
$$

````

**Question 3.2 :** Faire l'application pour $u=0.5$ (milieu de la trajectoire). Analyser les influences des autres paramètres.

````{admonition} Solution

Pour $u = 0,5$ 

$$
\begin{equation*}
\text{Ecart} = f_{MGD} \begin{pmatrix}
X_m(u = 0,5)\\
Y_m(u = 0,5)\\
Z_m(u = 0,5)\\
B(u = 0,5)\\
\end{pmatrix} - \dfrac{1}{2}\left( \overrightarrow{O_pP_1} +  \overrightarrow{O_pP_2}\right)
\end{equation*}
$$

On commence par calculer les valeurs $X_m, Y_m, Z_m, B$ en $u= 0,5$ :

$$
\begin{equation*}
\begin{cases}
X_m(u = 0,5) &= \dfrac{X_m^1 +X_m^2}{2} = p_x + d_x \cos(\alpha)  \\
Y_m(u = 0,5) &= \text{Indéterminé} \\
Z_m(u = 0,5) &= \dfrac{Z_m^1 +Z_m^2}{2} = \dfrac{L}{2}\sin(\alpha) + p_z + j_z + d_z \cos(\alpha)  \\
B(u = 0,5) &= \dfrac{B^1 +B^2}{2} = 0 
\end{cases}
\end{equation*}
$$

En appliquant la fonction MGD établie à la question 1.2 on trouve la position du point $P$ : $X_p^a, Y_p^a, Z_p^a$ en $u = 0,5$ pour une interpolation linéaire dans l'espace articulaire.

$$
\begin{equation*}
f_{MGD} \begin{pmatrix}
X_m(u = 0,5)\\
Y_m(u = 0,5)\\
Z_m(u = 0,5)\\
B(u = 0,5)\\
\end{pmatrix} = 
\begin{cases}
X_p^a(u = 0,5) &= d_x \cos(\alpha)- dx  \\
Y_p^a(u = 0,5) &= \text{Indéterminé} \\
Z_p^a(u = 0,5) &= \dfrac{L}{2}\sin(\alpha) + d_z \cos(\alpha)- d_z   
\end{cases}
\end{equation*}
$$

On trouve facilement la position du point $P$ : $X_p^t, Y_p^t, Z_p^t$ en $u = 0,5$ pour une interpolation linéaire dans l'espace des taches.

$$
\begin{equation*}
\dfrac{1}{2}\left( \overrightarrow{O_pP_1} +  \overrightarrow{O_pP_2}\right) = 
\begin{cases}
X_p^t(u = 0,5) &= 0  \\
Y_p^t(u = 0,5) &= \text{Indéterminé} \\
Z_p^t(u = 0,5) &= 0  
\end{cases}
\end{equation*}
$$

d'où : 

$$
\begin{equation*}
Ecart =   
\begin{cases}
d_x (\cos(\alpha)- 1)  \\
\text{Indéterminé} \\
\dfrac{L}{2}\sin(\alpha) + d_z( \cos(\alpha)- 1)   
\end{cases}
\end{equation*}
$$

````

**Question 3.3 :** Aller au bout de l'application et effectuer une représentation du comportement pour un posage de la pièce tel que $d_x=0$ et $d_z=\dfrac{L}{2}$, et dans le cas où $\alpha = 45^{\circ}$.

````{admonition} Solution

```{figure} img/TD4/ecart.png
---
width: 300px
--- 
```

Après application numérique on trouve : 

$$
\begin{equation*}
Ecart =   
\begin{cases}
d_x (\cos(\alpha)- 1) &= 0 \\
\text{Indéterminé} &= \text{Indéterminé}  \\
\dfrac{L}{2}\sin(\alpha) + d_z( \cos(\alpha)- 1) &= \dfrac{L}{2}(\sqrt{2}-1) 
\end{cases}
\end{equation*}
$$

On observe bien que l'écart est uniquement suivant l'axe $\overrightarrow{z}$.

````

## Annexes

matrices homogènes de transformations entre repères issues du paramétrage

$$
\begin{equation}
	\mathbf{T}_{pm}=
	\begin{bmatrix}
          	\text{C}B & 0 & \text{S}B & - d_x - p_x \ \text{C}B - (p_z+j_z) \ \text{S}B \\
  		0             & 1 & 0             & - d_y - p_y \\
	        -\text{S}B & 0 & \text{C}B & - d_z + p_x \ \text{S}B - (p_z+j_z) \ \text{C}B \\
       		0 & 0 & 0 & 1\\
	\end{bmatrix} \nonumber
\end{equation}
$$

$$
\begin{equation}
	\mathbf{T}_{mp}=
	\begin{bmatrix}
          	\text{C}B & 0 & -\text{S}B & p_x + d_x \ \text{C}B - d_z \ \text{S}B \\
  		0             & 1 & 0              & p_y + d_y \\
	        \text{S}B  & 0 & \text{C}B & (p_z+j_z) +  d_x \ \text{S}B + d_z \ \text{C}B \\
       		0 & 0 & 0 & 1\\
	\end{bmatrix} \nonumber
\end{equation}
$$

avec

- ($p_x,p_y,p_z$) les composantes du vecteur caractéristique machine $\mathbf{O_m O_o}$;
- ($d_x,d_y,d_z$) les composantes du vecteur caractéristique de décalage lié au posage de la pièce sur la table $\mathbf{O_o O_p}$;
- $j_z$ la caractéristique de longueur d'outil.

 