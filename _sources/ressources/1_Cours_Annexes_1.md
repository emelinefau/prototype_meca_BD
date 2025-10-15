# Compléments mathématiques

## Fonction atan2

La fonction $\text{atan2}(y, x)$ permet, par l'analyse du signe de ses deux arguments $x$ et $y$ de déterminer le quadrant solution à $2 \pi$ près pour l'inversion de la fonction tangente :

$$
\begin{align}
\text{atan2}(y, x) = 
\begin{cases}
\text{atan}(y/x) \quad & \text{si} \quad  x > 0 \\
\text{atan}(y/x)+\pi \quad & \text{si} \quad  y \geq 0, x < 0 \\
\text{atan}(y/x)-\pi \quad & \text{si} \quad  y < 0, x < 0 \\
\pi/2 \quad & \text{si} \quad  y > 0, x = 0 \\
-\pi/2 \quad & \text{si} \quad  y < 0, x = 0 \\
0 & \text{si} \quad  y = 0, x = 0 \\
\end{cases}
\end{align}
$$

## Matrice orthogonale

Une matrice $\mathbf{A}$ $n\times n$ est dite orthogonale si :

$$
\begin{equation}
\mathbf{A} \mathbf{A}^t = \mathbf{A}^t \mathbf{A} = \mathbf{I}_d
\end{equation}
$$

alors

$$
\begin{equation}
\mathbf{A}^t = \mathbf{A}^t \mathbf{A} \mathbf{A}^{-1} = \mathbf{I}_d \mathbf{A}^{-1} = \mathbf{A}^{-1}
\end{equation}
$$

Pour les matrices de changement de base, les vecteurs colonnes de $\mathbf{A}$ sont orthogonaux et unitaires.

## Pseudo inverse

Cette matrice fut définie simultanément par Moore en 1920 et Penrose en 1955. Elle est connue sous le nom de matrice inverse généralisée ou matrice pseudo-inverse ou encore matrice inverse de Moore-Penrose.
Pour une matrice $\mathbf{A}$ de taille $m \times n$, la matrice inverse généralisée de Moore-Penrose est une matrice « pseudo-inverse » unique de taille $n \times m$ notée $\mathbf{A}^{\dagger}$.
Cette matrice est définie pour les matrices complexes, mais nous ne donnons ici que les relations dans le cas de matrices réelles.

La matrice pseudo-inverse satisfait les équations suivantes :

$$
\begin{align}
\mathbf{A} \mathbf{A}^{\dagger} \mathbf{A} &= \mathbf{A} \\
\Leftrightarrow  \mathbf{A}^{\dagger} \mathbf{A} \mathbf{A}^{\dagger} &= \mathbf{A}^{\dagger} \\
\Leftrightarrow  (\mathbf{A} \mathbf{A}^{\dagger})^t &= \mathbf{A} \mathbf{A}^{\dagger}\\
\Leftrightarrow  (\mathbf{A}^{\dagger} \mathbf{A})^t &= \mathbf{A}^{\dagger} \mathbf{A} 
\end{align}
$$

Elle est notamment utilisée dans les problèmes de minimisation lorsque l'on a plus de données que d'inconnues. Par exemple, soit le système linéaire suivant, d'inconnue $\mathbf{B}$ :

$$
\begin{equation}
\mathbf{A} \mathbf{X} = \mathbf{B}
\end{equation}
$$

en multipliant à gauche par la transposée de $\mathbf{B}$  :

$$
\begin{equation}
\mathbf{A}^t \mathbf{A} \mathbf{X} = \mathbf{A}^t \mathbf{B}
\end{equation}
$$

si l'inverse de $\mathbf{B}^t \mathbf{B})$  (matrice carrée) existe alors :

$$
\begin{equation}
\mathbf{X} = (\mathbf{A}^t \mathbf{A} )^t \mathbf{A}^t \mathbf{B}
\end{equation}
$$

avec la définition de la pseudo inverse :

$$
\begin{equation}
\mathbf{A}^{\dagger} = (\mathbf{A}^t \mathbf{A} )^t \mathbf{A}^t
\end{equation}
$$

la solution de l'équation initiale se réécrit :

$$
\begin{equation}
\mathbf{X} = \mathbf{A}^{\dagger} \mathbf{B}
\end{equation}
$$

Cette solution particulière correspond au vecteur de norme minimale dans la formulation au sens des moindres carrés.

## Matrice de pré-produit vectoriel

Soit le produit vectoriel de $\mathbf{u}$ par $\mathbf{v}$ tel que :

$$
\begin{equation}
\mathbf{u} \wedge \mathbf{v} = \begin{bmatrix} u_x \\ u_y \\ u_z \end{bmatrix} - \begin{bmatrix} v_x \\ v_y \\ v_z \end{bmatrix} = \begin{bmatrix} u_y v_z - u_z v_y \\ u_z v_x - u_x v_z \\ u_x y_v - u_y v_x \end{bmatrix}
\end{equation}
$$

Cette opération peut se mettre sous la forme linéaire suivante :

$$
\begin{equation}
\begin{bmatrix} 0 & -u_z & u_y \\ u_z & 0 & -u_x \\ -u_y & u_x & 0 \end{bmatrix}  \begin{bmatrix} v_x \\ v_y \\ v_z \end{bmatrix}
\end{equation}
$$

On définit ainsi l'opérateur de pré-produit vectoriel appliqué à $\mathbf{u}$, la matrice anti-symétrique notée $\mathbf{\hat{u}}$ :

$$
\begin{equation}
\mathbf{u} \wedge \mathbf{v}  = \mathbf{\hat{u}} \mathbf{v}  \quad \text{avec} \quad 
\mathbf{\hat{u}} = \begin{bmatrix} 0 & -u_z & u_y \\ u_z & 0 & -u_x \\ -u_y & u_x & 0 \end{bmatrix} 
\end{equation}
$$

