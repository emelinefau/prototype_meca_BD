# M1 SPA : Systèmes Poly-Articulés

Ce dépot contient un livre Jupyter (Jupyter book) dont la version au format .html est disponible à l'adresse suivante : 

**Mettre le lien (uniquement possible après le 1er commit)**

Ce document sert de support pour l'Unité d'Enseignement "Systèmes Poly-Articulés" du master Mécanique de l'Université Paris-Saclay parcours MIP (Mécanique et Ingénierie de la Production) et MMS (Mécanique des Matériaux et des Structures)

## A propos de ce document

L'auteur principal de cette édition du cours est Kevin Godineau mais le contenu du cours et une partie de celui des TD et TP est une réécriture du cours de Sylvain Lavernhe.

## Informations techniques

### Instalation des outils pour créer un jupyterbook

Pour l'instalation il suffit d'exécuter les ligne suivantes : 

    pip install -U jupyter-book
    pip install sphinx-proof

### création du jupyterbook en local 

La construction de la version .html et de la version latex s'effectue en utilisant les commandes suivantes :

Pour nettoyer un jupyterbook :

    jupyter-book clean m1_spa_jbook

Pour "compiler" les fichiers .md en un document .html :

    jupyter-book build m1_spa_jbook --builder html

Pour "compiler" les fichiers .md en un document .pdf via latex :

    jupyter-book build m1_spa_jbook --builder pdflatex

Ces commandes doivent être exécuté depuis le dossier contenant le dossier a compiler (ici, "m1_spa_jbook").

<!-- 
## Commandes markdown spécifiques

### Boites

```{admonition} Définition
:class: tip

ddd
```

    ```{admonition} Définition
    :class: tip

    ddd
    ```

```{admonition} Remarque
:class: Note

ddd
```

    ```{admonition} Remarque
    :class: Note

    ddd
    ```

```{admonition} Attention
:class: attention

ddd
```

    ```{admonition} Attention
    :class: attention

    ddd
    ```

Voici la liste des types possible de boites : {tip}, {note}, {attention}, {caution}, {danger}, {error}, {hint}, {important}, {warning}. Dans ce cas la ligne class n'est pas obligatoire exemple : 

```{error} 

ddd
```
    ```{error} 

    ddd
    ```

### figures

```{figure} img/Cours/1_1.png
---
width: 350px
name: Base_espace_vectoriel1
---
Vecteur et base d'espace vectoriel
```

    ```{figure} img/Cours/1_1.png
    ---
    width: 350px
    name: Base_espace_vectoriel1
    ---
    Vecteur et base d'espace vectoriel
    ```

Pour cité la figure {numref}`Base_espace_vectoriel1` il faut un "name" puis écrire : 

    (figure {numref}`Base_espace_vectoriel1`)


### citation : 

L'article {cite:p}`chomsky_certain_1959` présente 

    {cite:p}`chomsky_certain_1959`

### équation  :

Voici un exemple d'équation 

$$ 
\begin{equation}
\mathcal{B} = (\mathbf{u_1},\mathbf{u_2}, \cdots, \mathbf{u_n})
\end{equation} 
$$ 

    $$ 
    \begin{equation}
    \mathcal{B} = (\mathbf{u_1},\mathbf{u_2}, \cdots, \mathbf{u_n})
    \end{equation} 
    $$ (eq:definition_base) 

Pour citer l'équation {eq}`eq_1_11` on utilise la commande suivante 

    {eq}`eq_1_11` 

### liens hypertextes

adresse mail : contact@ens-paris-saclay.fr 

site web : https://clermont-ferrand.fr/

site web avec chaine de caractère à la place de l'URL [unicode](https://fr.wikipedia.org/wiki/Unicode)



::::

::::{grid} 1 1 2 3
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: 2_TD_1
:link-type: doc
:class-header: bg-light

Text content ✏️
^^^

Structure books with text files and Jupyter Notebooks with minimal configuration.
:::

:::{grid-item-card}
:link: 2_TD_1
:link-type: doc
:class-header: bg-light

MyST Markdown ✨
^^^

Write MyST Markdown to create enriched documents with publication-quality features.

:::

:::{grid-item-card}
:link: 2_TD_1
:link-type: doc
:class-header: bg-light

Executable content 🔁
^^^

Execute notebook cells, store results, and insert outputs across pages.

:::

:::{grid-item-card}
:link: 2_TD_1
:link-type: doc
:class-header: bg-light

Live environments 🚀
^^^

Connect your book with Binder, JupyterHub, and other live environments
:::

:::{grid-item-card}
:link: 2_TD_1
:link-type: doc
:class-header: bg-light

Build and publish 🎁
^^^

Share your built books via web services and hosted websites.
:::

:::{grid-item-card}
:link: 2_TD_1
:link-type: doc
:class-header: bg-light

UI components ⚡
^^^

Create interactive and web-native components and services.
:::

::::
 -->
