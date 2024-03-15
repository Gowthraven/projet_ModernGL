# Rapport de Projet : Moteur de Rendu avec ModernGL

## Introduction

Ce projet a été initié suite à une série de défis techniques, incluant une panne de PC, des erreurs de compilation, et des problèmes de configuration, qui ont considérablement réduit le temps disponible pour travailler sur mon projet initial, et ne pouvant pas reprendre la base de projet que j'avais codé l'an dernier. Nécessitant une adaptation rapide, j'ai décidé de me lancer dans le développement d'un moteur de rendu en utilisant Python et la bibliothèque ModernGL, une alternative à PyOpenGL.

### Contexte

Python, avec sa facilité de débogage et sa syntaxe claire, s'est avéré être un choix judicieux pour ce projet, bien qu'il n'est pas naturel de coder du OpenGL avec ce langage. ModernGL offre une approche moderne et efficace pour le rendu OpenGL, ce qui m'a motivé à explorer cette bibliothèque. De plus, l'utilisation de PyGLM, un wrapper pour GLM (OpenGL Mathematics) écrit en C++, a apporté des avantages en termes de performance et de compatibilité avec OpenGL.

## Objectifs du Projet

- Développer un petit moteur de rendu utilisant ModernGL, en suivant les tutoriels disponibles sur internet.
- Implémenter des fonctionnalités avancées telles qu'une skybox, de l'envmap, et/ou de la shadowmap.
- Se familiariser avec les étapes du pipeline de rendu OpenGL et la structure d'un moteur de rendu, sous Python.

## Développement

### Recherches et Ressources

Des recherches initiales m'ont mené à diverses ressources, incluant des tutoriels, des bases de code, et des vidéos explicatives. Voici quelques références clés qui ont guidé mon travail :

- Tutoriels OpenGL sur [developpez.com](https://opengl.developpez.com/tutoriels/apprendre-opengl/?page=glossaire)
- Ressources et textures fournies par [LearnOpenGL](https://github.com/JoeyDeVries/LearnOpenGL/tree/master/resources/textures)
- Documentation officielle de [ModernGL](https://moderngl.readthedocs.io/en/5.8.2/)
- Série de tutoriels vidéo sur [CoderSpace Channel](https://www.youtube.com/@CoderSpaceChannel)

### Réalisation

En suivant les tutoriels de CoderSpace, j'ai intégré ModernGL avec Pygame pour créer le moteur de rendu. Cette approche m'a permis de comprendre la structure d'un moteur de rendu, la syntaxe de ModernGL, et les étapes critiques du pipeline de rendu OpenGL.

## Résultats

Le projet a abouti à la création d'un moteur de rendu fonctionnel capable de gérer une skybox, de l'envmap, et de la shadowmap. La structure des classes a été améliorée pour une meilleure organisation et maintenabilité du code, en comparaison avec les tutoriels vidéos de CoderSpace.

## Conclusion

Ce projet a été une opportunité d'apprendre et d'expérimenter avec ModernGL et le rendu OpenGL sous Python. Malgré les défis initiaux, les résultats obtenus démontrent la flexibilité et une certaine puissance de Python pour le développement de moteurs de rendu. Les ressources et tutoriels utilisés ont été indispensables pour surmonter les obstacles techniques et parvenir à un résultat satisfaisant.

## Remerciements

Je tiens à exprimer ma gratitude envers les créateurs des ressources éducatives mentionnées, en particulier CoderSpace, pour leurs tutoriels détaillés qui ont grandement facilité mon apprentissage du rendu avec ModernGL, ainsi qu'une meilleure compréhension de certaines notions abordés en cours.
