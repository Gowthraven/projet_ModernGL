# Rapport de Projet : Rendu avec ModernGL

## Introduction

Ce projet a commencé avec divers défis, incluant des problèmes matériels et logiciels, qui ont réduit le temps de développement disponible, qui était déjà limité. En cherchant une solution, j'ai opté pour Python et ModernGL, pour leur simplicité et efficacité, malgré l'apparente incongruité de Python pour du développement OpenGL. Ayant une certaine facilité à coder avec Python, cela fut enrichissant de développer un mini moteur de rendu avec ce langage. 

### Contexte

L'adoption de Python, connu pour sa facilité de débogage et sa synthaxe intuitive, s'est avéré être un choix correct pour les attentes demandées. Bien qu'il n'est pas naturel de coder du OpenGL avec ce langage, la librairie ModernGL offre une approche moderne et efficace pour le rendu OpenGL (moderne), ce qui m'a motivé à explorer cette bibliothèque. De plus, l'utilisation de PyGLM, un wrapper pour GLM (OpenGL Mathematics) écrit en C++, a apporté des avantages en termes de performance et de compatibilité avec OpenGL.

## Objectifs du Projet

- Concevoir un moteur de rendu léger avec ModernGL, en capitalisant sur les ressources éducatives disponibles en ligne.
- Intégrer des fonctionnalités telles que skybox (cubemap), envmap, et shadowmap.
- Approfondir la compréhension du pipeline de rendu OpenGL et des principes sous-jacents d'un moteur de rendu, dans le contexte de Python.

## Développement

### Recherches et Ressources

Une exploration préliminaire a mené à la découverte de ressources variées, dont des tutoriels, des références de code, et des contenus vidéo, qui ont guidé les étapes du développement.

- Tutoriels OpenGL sur [developpez.com](https://opengl.developpez.com/tutoriels/apprendre-opengl/?page=glossaire)
- Ressources et textures fournies par [LearnOpenGL](https://github.com/JoeyDeVries/LearnOpenGL/tree/master/resources/textures)
- Documentation officielle de [ModernGL](https://moderngl.readthedocs.io/en/5.8.2/)
- Série de tutoriels vidéo avec du code sur [CoderSpace Channel](https://www.youtube.com/@CoderSpaceChannel)
- Documentation NVidia sur les [Shadow Map Antialiasing ](https://developer.nvidia.com/gpugems/gpugems/part-ii-lighting-and-shadows/chapter-11-shadow-map-antialiasing)
- Tutoriel sur le [Pourcentage Closer Filtering](https://ogldev.org/www/tutorial42/tutorial42.html)

### Réalisation

Le suivi des tutoriels de CoderSpace, en intégrant ModernGL à Pygame, a été une étape cruciale pour saisir la logique de l'implémentation d'OpenGL avec ModernGL, avec sa synthaxe spécifique, et les étapes essentielles du pipeline de rendu OpenGL. J'ai suivi de manière assez guidé sa façon de coder pas à pas le moteur de rendu, en modifiant néanmoins la structure du code pour qu'elle soit plus compréhensible et modifiable pour des utilisations futures. 

## Compilation et Exécution 

Pour compiler et exécuter le code :

1. Assurez-vous que Python est installé sur votre machine, idéalement une version récente.
2. Installez les dépendances nécessaires avec `pip install -r requirement.txt`.
3. Lancez le moteur avec `python main.py`.

### Contrôles de la Caméra : 

Les contrôles de la caméra sont modifiables dans le fichier `scene/camera.py`, au besoin.

- **Avancer** : Z ou Flèche du haut
- **Reculer** : S ou Flèche du bas
- **Déplacer à gauche** : Q ou Flèche de gauche
- **Déplacer à droite** : D ou Flèche de droite
- **Monter** : Barre d'espace (Space)
- **Descendre** : Alt gauche (LAlt)


## Structure du code 

Le projet est structuré autour d'un fichier principal (`main.py`), qui orchestre l'ensemble du processus de rendu en initialisant les éléments clés de la scène tels que la lumière, la caméra, les maillages (mesh), et le moteur de rendu (renderer). Le projet se divise en deux sous-dossiers principaux : render et scene, contenant respectivement les composants liés au rendu et à la mise en scène.

### Dossier `render`

Ce dossier contient les éléments essentiels au rendu, tels que les maillages, les shaders, les textures, les Vertex Array Objects (VAOs) et les Vertex Buffer Objects (VBOs).

Fichiers Clés :
- `shaders.py` (Classe Shader) : Charge et gère les shaders (vertex et fragment), essentiels pour définir comment les pixels et les vertices sont traités pendant le rendu.

- `texture.py` (Classe Texture) : Gère les textures avec un système de dictionnaire, optimisant les performances et la qualité à travers l'utilisation de mipmaps et de filtrage anisotrope. Une fonction spécifique assemble les textures de la skybox en une texture cubique, en inversant certaines textures selon leur orientation pour un rendu correct.

- `vao.py` (Classe VAO) : Déclare les VAOs pour les éléments de la scène et leurs ombres. Important pour l'ajout d'éléments à la scène, chaque ajout doit être accompagné d'une déclaration VAO appropriée.

- `vbo_utils.py` et `vbo_elements.py` (Classes VBO) : Fournissent la base pour la déclaration des VBOs spécifiques à chaque objet, en lien avec les attributs définis dans les shaders. `vbo_skybox.py` traite spécifiquement de la skybox. Ces VBO sont ensuite gérés dans un dictionnaire dans `vbo.py`. 

### Dossier `scene`
Contient les composants relatifs à la mise en scène, tels que la caméra, la lumière, les modèles et le système de rendu.

Fichiers Clés :
- `camera.py` (Classe Camera) : Gère la caméra, incluant les mouvements et rotations, offrant une vue dynamique de la scène.

- `light.py` (Classe Light) : Gère l'éclairage de la scène en utilisant des intensités ambiantes, diffuses et spéculaires pour créer des effets d'éclairage réalistes.

- `model_utils.py` (Classes Model/ExtendedBaseModel) : Permet d'initialiser et de rendre des modèles 3D, gérant les paramètres tels que la position, la rotation, l'échelle, et les textures. La version avancée ajoute des fonctionnalités telles que la gestion des ombres.

- `render.py` (Classe Render) : Coordonne le rendu global, incluant le rendu des ombres et le rendu principal. Utilise un tampon de profondeur et un framebuffer pour gérer les informations de profondeur nécessaires au calcul des ombres.

- `scene.py` (Classe Scene) : Organise et configure tous les objets de la scène, leur positionnement, leur échelle, etc.

### Détails des Shaders
- `base.frag` : Gère l'éclairage, les textures, les ombres et la correction gamma. Inclut des fonctions avancées pour le calcul des ombres douces (soft shadows) et utilise un système de coordonnées pour déterminer l'influence des ombres sur les fragments.

- `base.vert` : Prépare les données nécessaires pour chaque vertex, incluant les transformations, l'éclairage et les ombres, en vue du rendu final.

- `shadow_map.vert` : Spécialisé dans la génération de cartes d'ombres, calculant les informations de profondeur du point de vue de la source lumineuse.

- `Shaders de la Skybox` (`skybox.vert` et `skybox.frag`) : Utilisés conjointement pour créer un effet de skybox immersive, simulant un environnement lointain enveloppant la scène.

### Implémentations Notables
- **Biais Anti-Acné** : Afin d'éviter les artefacts d'ombres communs tels que le "shadow acne", un biais est appliqué lors du calcul des ombres, affinant le rendu et améliorant la qualité visuelle.

- **Ombres Douces (Soft Shadows)** : Grâce à un échantillonnage multi-point et un calcul moyenné, les ombres dans la scène bénéficient d'un adoucissement des bords, offrant un rendu plus naturel et réaliste.

- **Correction Gamma** : L'application d'une correction gamma avant et après le traitement des couleurs assure une représentation fidèle et dynamique des couleurs à l'écran, améliorant ainsi l'expérience visuelle globale.

### Limitations

Face au manque de temps, certaines optimisations et fonctionnalités avancées comme le shadowmap dynamique n'ont pu être intégrées. Toutefois, ce mini projet a été l'occasion d'un riche apprentissage, en particulier sur les shaders, renforçant les connaissances acquises l'année précédente. Une piste d'implémentation aurait été de mettre à jour "en temps réel" des cartes d'ombres basées sur la position et l'orientation de la source lumineuse, permettant alors d'avoir des ombres qui s'adaptent aux mouvement dans la scène. 


## Résultats

Le projet a abouti à la création d'un moteur de rendu fonctionnel capable de gérer une skybox, de l'envmap, et de la shadowmap, avec du softshadow, malgré certains rendus initiaux peu convaincants. Les améliorations successives, après plusieurs tests, ont permis d'obtenir des ombres plus réalistes.

### Ombres 

*Exemple de rendu initial des ombres, montrant un aspect brut.*

![Ombre avec shadowmap](https://github.com/Gowthraven/projet_ModernGL/blob/main/images/shadow_1.png)

*Amélioration significative avec l'intégration d'un soft shadow pour un rendu plus diffus des ombres*

![Ombre avec shadowmap](https://github.com/Gowthraven/projet_ModernGL/blob/main/images/shadow_2.1.png)

### Skybox / Cubemap 

*Exemple de rendu avec la skybox*

![Rendu de la skybox](https://github.com/Gowthraven/projet_ModernGL/blob/main/images/skybox_render.gif)

### Modèles à microfacette (Projet M1)

Voir la [vidéo de démonstration](https://www.youtube.com/watch?v=lCydYZzcLg0) du Projet de M1, onglet surface. 



## Conclusion

Ce projet a été une opportunité d'apprendre et d'expérimenter avec ModernGL et le rendu OpenGL sous Python. Malgré les défis initiaux, les résultats obtenus démontrent la flexibilité et une certaine puissance de Python pour le développement de moteurs de rendu. Les ressources et tutoriels utilisés ont été indispensables pour surmonter les obstacles techniques et parvenir à un résultat satisfaisant.

Je tiens à exprimer ma gratitude envers les créateurs des ressources mentionnées, en particulier CoderSpace, pour leurs tutoriels détaillés qui ont grandement facilité mon apprentissage du rendu avec ModernGL, ainsi qu'une meilleure compréhension de certaines notions abordés en cours.


# Rapport de Projet : Animation Skinning 

![Rendu de la skybox](https://github.com/Gowthraven/projet_ModernGL/blob/main/animation/animation_skinning.gif)

L'implémentation du Linear Blend Skinning (LBS) dans le [code fourni](https://github.com/dlyr/m2igai-anim) est une technique de déformation de maillage 3D couramment utilisée dans l'animation de personnages. Elle permet à un modèle 3D d'articuler de manière réaliste en associant les sommets du maillage à un ou plusieurs os d'un squelette, puis en ajustant leur position en fonction des transformations de ces os.

## Fonctionnement de Base

Dans le contexte du projet, chaque sommet du maillage est influencé par deux os principaux, ce qui est souvent le cas pour des modèles simples comme des cylindres ou des bras articulés. Les poids d'influence de ces os sur un sommet donné déterminent à quel point les transformations (rotations, translations) de chaque os affectent la position finale de ce sommet. Dans notre implémentation, ces poids et les informations de liaison aux os sont stockés directement dans les attributs de chaque sommet du maillage.

## Structure de Données

Le maillage est représenté par une classe MiniMesh, qui encapsule les sommets (Vertex), les faces du maillage et les informations nécessaires pour le rendu OpenGL comme les VAO (Vertex Array Objects) et les VBO (Vertex Buffer Objects). Chaque sommet contient sa position, sa normale, un vecteur de couleurs, et cruciallement, un vecteur de poids définissant la contribution relative de chaque os à la position finale du sommet.

## Transformation des Sommets
Lors de l'animation, les transformations appliquées aux os sont calculées en fonction des entrées de l'utilisateur ou d'une séquence d'animation prédéfinie. Ces transformations sont ensuite appliquées aux sommets du maillage en fonction de leurs poids d'influence. Le processus de déformation du maillage implique le calcul d'une nouvelle position pour chaque sommet en combinant les transformations des os influents, pondérées par leurs poids respectifs.

## Calcul du rendu
Dans la boucle de rendu, chaque sommet du maillage est transformé par les matrices de transformation des os auxquels il est lié, avant d'être envoyé au GPU pour le rendu. Cette étape est souvent gérée par des shaders, qui calculent la position finale des sommets en temps réel, permettant ainsi des animations fluides et réactives.

## Conclusion
Cette implémentation du Linear Blend Skinning permet donc une animation assez réaliste de modèles simples comme le cylindre avec un contrôle sur le mouvement des différentes parties du modèle. Bien que je ne peux fournir mes modifications de code en raison de la défaillance de mon PC portable le contenant, une capture vidéo du rendu a heureusement été réalisée en avance, permettant de documenter le résultat visuel de l'implémentation pour le rapport. Dans la vidéo, lorsqu'une flexion ou une déformation est appliquée au cylindre, l'effet de skinning se manifeste clairement, illustrant la déformation du maillage en fonction des poids attribués.






