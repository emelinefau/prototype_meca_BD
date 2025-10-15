# Équations typiques et solutions associées pour la résolution des MGI

La liste ci-dessous présente les différents types d'équations qui sont rencontrées lors de la résolution des Modèles Géométriques Inverses (MGI) des structures ouvertes (méthode de Paul et méthode de Pieper). 

La variable $r_i$ correspond à la variable articulaire $q_i$ pour une liaison glissière (prismatique) ; la variable $\theta_i$ correspond à la variable articulaire $q_i$ pour une liaison pivot (rotoïde). Pour le détail des calculs, se référer à \cite{2}.

## Type 1
$$
\begin{equation}
X \, r_i = Y
\end{equation}
$$

Solutions : 

$$
\begin{equation}
r_i = \begin{cases}
Y/X \quad & \text{si} \quad X \neq 0 \\
\text{non défini} \quad & \text{si} \quad X =0 \\
\end{cases}
\end{equation}
$$

## Type 2

$$
\begin{equation}
X \, \text{S}\theta_i + Y\, \text{C}\theta_i = Z
\end{equation}
$$

Solutions : 

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

dans le cas où $ X \neq 0$, $Y \neq 0$ et $Z \neq 0$, l'équation est résolue en élevant l'expression au carré : en remplaçant les termes en sinus par les fonctions équivalentes en cosinus, on aboutit à une équation du second degré à résoudre donnant la valeur du cosinus. Un raisonnement analogue est mené pour déterminer le terme en sinus :

$$
\begin{equation}
\begin{cases}
\text{C}\theta_2 = \dfrac{YZ - \epsilon X \sqrt{X^2+Y^2-Z^2}}{X^2 + Y^2} \\
\text{S}\theta_2 = \dfrac{XZ + \epsilon Y \sqrt{X^2+Y^2-Z^2}}{X^2 + Y^2} \\
\end{cases}
\qquad \text{avec} \qquad \epsilon = \pm 1
\end{equation}
$$

Dans ce cas, la résolution de l'équation donne deux solutions, correspondant aux valeurs de $\epsilon$.

## Type 3

Il s'agit d'un système d'équations à résoudre :

$$
\begin{equation}
\begin{cases}
X_1 \, \text{S}\theta_i + Y_1\, \text{C}\theta_i = Z_1 \\
X_2 \, \text{S}\theta_i + Y_2\, \text{C}\theta_i = Z_2 \\
\end{cases}
\end{equation}
$$

Dans le cas où $X_1 Y_2 - X_2 Y_1 \neq 0$, les termes en cosinus et sinus sont obtenus par combinaison linaire des deux équations pour éliminer respectivement les termes sinus et cosinus :

$$
\begin{equation}
\begin{cases}
\displaystyle{\text{C}\theta_i = \frac{Z_2 X_1 - Z_1 X_2}{X_1 Y_2 - X_2 Y_1}} \\
\displaystyle{\text{S}\theta_i = \frac{Z_1 Y_2 - Z_2 Y_1}{X_1 Y_2 - X_2 Y_1}} \\
\end{cases}
\end{equation}
$$

Dans le cas où $X_1 Y_2 - X_2 Y_1 = 0$ alors, les équations ne sont plus indépendantes ; on choisit alors l'une des deux équations que l'on résout en équation de type 2.

Solution :

$$
\begin{equation}
\theta_i = \begin{cases}
\text{atan2}(\text{S}\theta_i, \text{C}\theta_i) \quad & \text{si} \quad X_1 Y_2 - X_2 Y_1 \neq 0  \\
\text{atan2}(\frac{Z_1}{X_1}, \frac{Z_2}{Y_2}) \quad & \text{si} \quad Y_1 = 0 \text{ et } X_2 = 0 \\
\end{cases}
\end{equation}
$$

## Type 4

$$
\begin{equation}
\begin{cases}
X_1 \, r_j \, \text{S}\theta_i  = Y_1 \\
X_2 \, r_j \, \text{C}\theta_i  = Y_2 \\
\end{cases}
\end{equation}
$$

Solution :

$$
\begin{align*}
\begin{cases}
\begin{cases}
r_i = \pm \sqrt{(Y_1/X_1)^2+(Y_2/X_2)^2} \\
\displaystyle{\theta_{i} = \text{atan2}(\frac{Y_1}{X_1\, r_j}, \frac{Y_2}{X_2\, r_j})}
\end{cases}  \quad & \text{si} \quad X_1 \ne 0 \text{ et } X_2 \ne 0  \\
\text{non défini} \quad & \text{si} \quad X_1 = 0 \text{ ou } X_2 = 0 
\end{cases}
\end{align*}
$$

## Type 5

$$
\begin{equation}
\begin{cases}
X_1  \, \text{S}\theta_i  = Y_1 + Z_1\, r_j\\
X_2 \,  \text{C}\theta_i  = Y_2 + Z_2\, r_j\\
\end{cases}
\end{equation}
$$

Solution :

Elle consiste à isoler les termes en sinus et cosinus dans chaque équation, les élever au carré, puis en les additionnant, on arrive à une équation du second degré en $r_j$ qui ne peut se résoudre que si le discriminant est positif. Une fois $r_j$ déterminé, le calcul de $\theta_i$ se fait en résolvant un système d'équation de type 3.

## Type 6

$$
\begin{equation}
\begin{cases}
W\, \text{S}\theta_j = X \, \text{C}\theta_i + Y\, \text{S}\theta_i + Z_1 \\
W\, \text{C}\theta_j = X \, \text{S}\theta_i - Y\, \text{C}\theta_i + Z_2 \\
\end{cases}
\end{equation}
$$

Solution :

Elle consiste à élever au carré chaque équation pour faire disparaître $\theta_j$ en les additionnant. $\theta_i$ est alors résolu par une équation de type 2. Ensuite, connaissant $\theta_i$, $\theta_j$ est déterminé par un système d'équations de type 3.

## Type 7

$$
\begin{equation}
\begin{cases}
W_1\, \text{C}\theta_j + W_2\, \text{S}\theta_j = X \, \text{C}\theta_i + Y\, \text{S}\theta_i + Z_1 \\
W_1\, \text{S}\theta_j - W_2\, \text{C}\theta_j= X \, \text{S}\theta_i - Y\, \text{C}\theta_i + Z_2 \\
\end{cases}
\end{equation}
$$

Solution :

C'est une généralisation du système d'équations de type 6. Il est résolu en élevant au carré les deux équations puis en les additionnant membre à membre. On abouti à une équation de type 2 en $\theta_i$, puis $\theta_j$ par une équation de type 3.

## Type 8

$$
\begin{equation}
\begin{cases}
X\, \text{C}\theta_i + Y\, \text{C}(\theta_i + \theta_j) = Z_1 \\
X\, \text{S}\theta_i + Y\, \text{S}(\theta_i + \theta_j) = Z_2 \\
\end{cases}
\end{equation}
$$

Solution :

En élevant au carré chaque équation puis en les additionnant, il vient :

$$
\begin{equation}
\begin{cases}
\displaystyle{\text{C}\theta_j = \frac{Z_1^2+ Z_2^2 - X^2 - Y^2}{2 X Y}} \\
\text{S}\theta_j = \sqrt{1 - \text{C}\theta_j^2} \\
\end{cases}
\end{equation}
$$

d'où les deux solutions possible pour $\theta_j$ :

$$
\begin{equation}
\theta_j = \text{atan2}(\pm \sqrt{1 - \text{C}\theta_j^2} , \text{C}\theta_j )
\end{equation}
$$

En développant le premier système d'équations et en factorisant par $\text{C} \theta_i$ et $\text{S} \theta_i$, on abouti à un système de deux équations à deux inconnues, dont les solutions sont :

$$
\begin{equation}
\begin{cases}
\displaystyle{\text{C}\theta_i = \frac{Z_1 B_1 + Z_2 B_2}{B_1^2 + B_2^2}} \\
\displaystyle{\text{S}\theta_i = \frac{Z_2 B_1 - Z_1 B_2}{B_1^2 + B_2^2}} \\
\end{cases}
\end{equation}
$$

où :

$$
\begin{equation}
\begin{cases}
B_1 = X + Y\, \text{C}\theta_j  \\
B_2 =  Y\, \text{S}\theta_j  \\
\end{cases}
\end{equation}
$$

La solution pour l'angle $\theta_i$ (associée à chaque solution $\theta_j$) est alors :

$$
\begin{equation}
\theta_i = \text{atan2}(\text{S}\theta_i , \text{C}\theta_i )
\end{equation}
$$

## Type 9
	
$$
\begin{equation}
a_2 r_i^2 + a_1 r_i + a_0 = 0
\end{equation}
$$

Solution :

Résolution d'une équation de second degré classique.

## Type 10

$$
\begin{equation}
a_4 r_i^4 + a_3 r_i^3 + a_2 r_i^2 + a_1 r_i + a_0 = 0
\end{equation}
$$

Solution :

La solution peut être obtenue à l'aide d'outils de calcul formel ; une solution numérique peut être facilement trouvée avec tout logiciel de calcul scientifique.

## Type 11

$$
\begin{equation}
a_4 \text{S}\theta_i^2 + a_3 \text{C}\theta_i \text{S}\theta_i + a_2 \text{C}\theta_i + a_1 \text{S}\theta_i + a_0 = 0
\end{equation}
$$

Solution :

Il faut se ramener à une équation de type 10. Pour cela, il faut appliquer le changement de variable $t = \text{tan} \left( \frac{\theta_i}{2}\right)$ et donc remplacer les cosinus et sinus par :

$$
\begin{equation}
\begin{cases}
\displaystyle{\text{C}\theta_i = \frac{1-t^2}{1+t^2}} \\
\displaystyle{\text{S}\theta_i = \frac{2t}{1+t^2}} \\
\end{cases}
\end{equation}
$$