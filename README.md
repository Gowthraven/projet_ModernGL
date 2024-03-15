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
2. Installez les dépendances nécessaires avec `pip install -r requirements.txt`.
3. Lancez le moteur avec `python main.py`.

## Modification de la Scène

[TODO]

### Limitations et Apprentissages

Face au manque de temps, certaines optimisations et fonctionnalités avancées comme le shadowmap dynamique n'ont pu être intégrées. Toutefois, ce mini projet a été l'occasion d'un riche apprentissage, en particulier sur les shaders, renforçant les connaissances acquises l'année précédente.

## Résultats

Le projet a abouti à la création d'un moteur de rendu fonctionnel capable de gérer une skybox, de l'envmap, et de la shadowmap, avec du softshadow, malgré certains rendus initiaux peu convaincants. Les améliorations successives, après plusieurs tests, ont permis d'obtenir des ombres plus réalistes.

*Exemple de rendu initial des ombres, montrant un aspect brut.*

![Ombre avec shadowmap](https://github.com/Gowthraven/projet_ModernGL/blob/main/images/shadow_1.png)

*Amélioration significative avec l'intégration d'un soft shadow pour un rendu plus diffus des ombres*

![Ombre avec shadowmap](https://github.com/Gowthraven/projet_ModernGL/blob/main/images/shadow_2.1.png)



## Conclusion

Ce projet a été une opportunité d'apprendre et d'expérimenter avec ModernGL et le rendu OpenGL sous Python. Malgré les défis initiaux, les résultats obtenus démontrent la flexibilité et une certaine puissance de Python pour le développement de moteurs de rendu. Les ressources et tutoriels utilisés ont été indispensables pour surmonter les obstacles techniques et parvenir à un résultat satisfaisant.

## Remerciements

Je tiens à exprimer ma gratitude envers les créateurs des ressources éducatives mentionnées, en particulier CoderSpace, pour leurs tutoriels détaillés qui ont grandement facilité mon apprentissage du rendu avec ModernGL, ainsi qu'une meilleure compréhension de certaines notions abordés en cours.
