# projet_drone33

This is our internship project : drone 33. This shall be edited into further details later on in the project. This file will serv as a documentation for the project.

## xamp version **7.3.20**
## wordpress version **5.6**
## Python version 3.6+

## Bibliothèques à installer si vous n'utilisez pas l'exe:
*il faut bien évidement avoir python 3 et pip d'installé au préalable*

> `pip install Pillow`


## Notice d'utilisation de l'interface de modification de site :

##### Une fois situé sur le menu principale de l'interface, selectionner le bouton migration.

Cela va donc vous ouvir une nouvelle fenêtre et vous offrir un pannel de possibilité de changement.

## Dans un premier temps et avant toutes choses, vous devez faire les changements qui s'appliquent sur les photos que vous verrez sur l'application

### Faire les changements de texte sur votre nouveau site à migrer
La principale chose que vous allez voir son des screens avec des encadrés <b>JAUNE</b>. Ces encradrés représente l'exactitude des changements qui vont être appliqués sur le site. Donc lorsqu'un texte est encadré d'un rectangle jaune, il faut le changer par exactement ce que vous souhaiter mettre à la place. Il est donc important de garder les majuscules, ponctuations, accents, parenthèses qui sont <b>BIEN VISIBLE DANS LE CARRÉ JAUNE</b>.<br><br>

### La première photo que vous allez voir est celle-ci<br>
![changement drone 33](https://cdn.discordapp.com/attachments/510525802371219456/812384998308315176/1.png)
#### Il faut donc entrer ici le nouveau nom de votre site sous le meme format que celui qui apparait.
Ici par exemple il est affiché "drone 33" sur la photo, il faut donc que vous remplaciez par "drone 12" par exemple, et non "drone12", "Drone12", "Drone 12", "DRONE12". Tous ces types de changements seront à faire par la suite sur d'autres photos où vous verrez toutes ces différentes syntaxes à modifier et à <b>conserver</b>.<br><br><br><br>

## Il y a cependant quelques exceptions
les images suivante sont des couleurs à changer :<br>

![hoover de bouton](https://cdn.discordapp.com/attachments/510525802371219456/811700097720385536/15.png)
#### Il faut donc mettre la code hexadécimal d'une couleur
par exemple, la couleur rouge du site drone33 est #C80108. Cependant, il est important de ne pas mettre le '#' avant, et de simplement mettre le code héxadécimal, à savoir : C80108.
Ce changement va donc affecter la couleur du hover du bouton, donc la coleur qui s'affichera lorsqu'on passe la souris dessus. Sur la photo, c'est donc la couleur rosé qui va être affecté.<br><br><br><br>

![couleur des boutons](https://cdn.discordapp.com/attachments/510525802371219456/811700772936351775/7.png)
#### Pour cette photo-ci, il faut egalement mettre le code héxadécimal.
Même paterne que la photo précédente, le code hexadécimal de la couleur que vous souhaitez, sans le '#' avant, par exemple : C80108
Ce changement va donc affecter la couleur des boutons du site. Cela va donc changer la couleur rouge que vous voyez par la couleur hexadécilamal que vous indiquerez.<br><br><br><br>

![couleur du pre-loader](https://cdn.discordapp.com/attachments/510525802371219456/811962000904683550/33.png)
#### Pour cette photo-ci, il faut egalement mettre le code héxadécimal.
Même paterne que la photo précédente, le code hexadécimal de la couleur que vous souhaitez, sans le '#' avant, par exemple : C80108
Ce changement va affecter la couleur du pré-loader du site, actuellement rouge, vous pouvez y mettre le code héxadécimal de la couleur que vous souhaitez.<br><br><br><br>

## Autres changements type affectés aux photos

![changement Charle DEBITUS](https://cdn.discordapp.com/attachments/510525802371219456/811964161306787850/26.png)
#### Changement de texte simple
Ici, c'est un texte simple à changer. Il ne faut cependant pas se tromper et bien changer uniquement ce qu'il y a dans le rectangle jaune. Veillez à bien garder la syntaxe de Charles DEBITUS, par Jean DUPONT, par exemple.<br><br><br><br>

![changement DRONE33](https://cdn.discordapp.com/attachments/510525802371219456/812335670496460801/4.png)
#### Changement de texte simple
Ici encore, il faut bien respecter la syntaxe si vous voulez garder cette derniere. En effet, sur la photo y est encadré DRONE33, il faut donc remplacer DRONE33 par DRONE12 par exemple, et non DRONE 12, ou encore drone 12, drone12. Il est important de garder la même syntaxe qui est indiquer dans l'encadré jaune.<br><br><br><br>

![changement de 'tribunaux de bordeaux'](https://cdn.discordapp.com/attachments/510525802371219456/812337051973451806/23.png)
#### Autre exemple de changement
Ici, il est important de changer toute la phrase qui est encadré, même si le but final est de changer la ville. Nous avons décider de faire cela car cela nous permet de cibler les bonnes phrases à changer. Ici, il faut donc modifier la phrase total et remplacer par, par exemple: "aux tribunaux compétents de Rodez".<br><br><br><br>

# Changement à faire à la main

### Il y a, suite a quelques modifications, des changements à faire à la main afin de s'assurer du bon changement de toute les informations du nouveau site
* <b>Si ce n'est pas déjà fait, se connecter avec les nouveau identifiant d'administration du site</b>
* <b>Rafraichir toute les pages du site avec elementor</b><br>
Pour ce faire, se connecter avec les indentifiants administrateur sur le wordpress, et faire "modifier avec elementor", faire un changement type (effacer une lettre et la remettre) pour avoir le bouton mettre à jour disponible en bas à gauche et cliquer dessus.
* <b>Rafraichir le site une fois avec l'onglet "Personaliser"</b><br>
Faire un changement type (desactiver et ré activer une feature) pour avoir le bouton "publier" ou "mettre à jour" disponible, et appuyer dessus.
### Ces changements permette majoritairement de faire apparaitre toute les couleurs mise à jour.
Cela enlevera possiblement des images sur le site, comme des images dans les services, ou encore dans les réalisations. Il faut donc remettre ces images à la main, que ce soit par elementor pour tout le site, et par l'onglet de personnalisation pour la page réalisation.
### Il faut refaire également la section contact dans le footer.
Les informations vont disparaitre pour cause de modification et elementor qui n'aime pas ca. Pour ce faire, vous devez :
 * Aller sur l'onglet "personnaliser" lorsque vous êtes connecté
 * Dessendre tout en bas pour apercevoir le footer
 * Selectionner un des crayons des sections déjà existante.
 * Sur la gauche s'affiche un menu avec 3 sections, créer-en une avec les informations de contact nécéssaire.
 * Pour choisir sa position, deplacer l'onglet "contact" du menu de gauche plus ou moins en haut ou en bas des autres onglets.

## Tous les autres changements ou personnalisations que vous n'avez pas apperçu dans notre application, ou non décrite ici, sont à faire à la main, à travers Elementor ou l'onglet personnalisation de Wordpress directement

