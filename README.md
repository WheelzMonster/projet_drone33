# projet_drone33

This is our internship project : drone 33. This shall be edited into further details later on in the project. This file will serv as a documentation for the project.

## xamp version **7.3.20**
## wordpress version **5.6**
## Python version 3.6+
<br><br>
## Mise en place de l'application

### Bibliothèque à installer :
*il faut bien évidement avoir python 3 et pip d'installé au préalable*
Pour installer pip, tapez donc ceci dans un terminal, peu importe votre emplacement sur le terminal:

> `pip install Pillow`

### Installation de Python

Vous devez donc avoir python 3.6, ou plus, d'installer pour faire fonctionner notre application. Pour ce faire, il faut aller sur ce lien :<br>
python 3.8 : https://www.python.org/downloads/release/python-380/ <br>
et télécharger la version correspondante à votre PC.<br>
Sur Mac, vous avez simplement à suivre le processus d'installation. <br>
Sur Windows, n'oubliez pas de cocher la case : "Add Python 3.8 to PATH" lors de l'installation.<br>
Si vous avez quelque difficulté pour l'installation sur Windows, https://www.youtube.com/watch?v=ZDnwD3Z1tPc <br><br>

Une fois Python d'installé, vous pouvez vous rendre directement dans le dossier sur lequel vous avez installé notre application, faire :<br><br>
sur Windows :<br>
Cliquez sur la barre de chemin du dossier, et ecrivez > `cmd` <br><br>
Sur Mac :<br>
Préférences > Clavier > Raccourcis clavier > Services. Cherchez "Nouveau terminal ici" et "Nouvel onglet de terminal ici". Vous pouvez aussi les assigner à des raccourcis clavier.<br>
Après avoir effectué cela, rendez-vous sur votre dossier d'installation de notre application : Clique droit > ouvrir un terminal ici. <br>



### Emplacement des dossiers/fichiers

* Le dossier img/slider contiendra toutes les images utilisées pour afficher les changements effectuer grâce à l'application.
* README.md est donc le fichier que vous êtes en train de lire.
* main.py est le fichier contenant le code de l'application. <br>

Il faudra également mettre l'archive de votre site (créée par duplicator) à la racine de l'application. À savoir là où se trouve les dossiers et fichiers qui viennent d'être décrit.

## Notice d'utilisation de l'interface de modification de site :

### Une fois situé sur le menu principale de l'interface, selectionner le bouton "migration"

Cela va donc vous ouvrir une nouvelle fenêtre et vous offrir un panel de possibilités de changements.

## Dans un premier temps et avant toutes choses, vous devez faire les changements de textes au niveau du slider d'images que vous verrez sur l'application.
/!\ Il ne faut donc pas commencer par faire le changement des photos grâce aux boutons sur la gauche de la fenêtre. /!\

### Faire les changements de texte sur votre nouveau site à migrer
La principale chose que vous allez voir son des screens avec des encadrés <b>JAUNE</b>. Ces encradrés représentent l'exactitude des changements qui vont être appliqués sur le site. Donc lorsqu'un texte est encadré d'un rectangle jaune, il faut le changer par exactement ce que vous souhaiter mettre à la place. Il est donc important de garder les majuscules, ponctuations, accents, parenthèses qui sont <b>BIEN VISIBLE DANS LE CARRÉ JAUNE</b>. Dans le cas contraire, il manquera surement ces derniers sur le site.
<br>
Pour faire un changement proprement, il faut donc :
* 1- Aller sur l'image correspondante au changement
* 2- Écrire le texte à modifier dans la zone de texte juste en dessous du slider d'image
* 3- Appuyer sur le bouton "valider"
* 4- Passer à l'image suivante
<br>

![menu explication](https://cdn.discordapp.com/attachments/510525802371219456/813426688360579113/menu.png)

<br>
Si vous vous êtes trompé, ou vous voulez tout simplement modifier le changement que vous aviez déjà fait, il vous suffit de revenir sur l'image du slider en question et réécrire le changement à faire dans la zone de texte, et re valider. Le nouveau changement sera pris en compte.<br>
Veillez à bien remplir chaque zone de texte et à bien appuyer sur valider pour chaque image du slider pour éviter toutes erreurs d'indentation.

<br><br>

### La première photo que vous allez voir est celle-ci<br>
![changement drone 33](https://cdn.discordapp.com/attachments/510525802371219456/812384998308315176/1.png)
#### Il faut donc entrer ici le nouveau nom de votre site sous le même format que celui qui apparaît.
Ici par exemple il est affiché "drone 33" sur la photo, il faut donc que vous remplaciez par "drone 12" par exemple, et non "drone12", "Drone12", "Drone 12", "DRONE12". Tous ces types de changements seront à faire par la suite sur d'autres photos où vous verrez toutes ces différentes syntaxes à modifier et à <b>conserver</b>.<br><br><br><br>

## Il y a cependant quelques exceptions
les images suivante sont des couleurs à changer :<br>

![hoover de bouton](https://cdn.discordapp.com/attachments/510525802371219456/811700097720385536/15.png)
#### Il faut donc mettre la code hexadécimal d'une couleur
Par exemple, la couleur rouge du site drone33 est #C80108. Cependant, il est important de ne pas mettre le '#' avant, et de simplement mettre le code héxadécimal, à savoir : C80108.
Ce changement va donc affecter la couleur du hover du bouton, donc la couleur qui s'affichera lorsqu'on passe la souris dessus. Sur la photo, c'est donc la couleur rosée qui va être affectée.<br><br><br><br>

![couleur des boutons](https://cdn.discordapp.com/attachments/510525802371219456/811700772936351775/7.png)
#### Pour cette photo-ci, il faut egalement mettre le code héxadécimal.
Même paterne que la photo précédente, le code hexadécimal de la couleur que vous souhaitez, sans le '#' avant, par exemple : C80108
Ce changement va donc affecter la couleur des boutons du site. Cela va donc changer la couleur rouge que vous voyez par la couleur hexadécilamal que vous indiquerez.<br><br><br><br>

![couleur du pre-loader](https://cdn.discordapp.com/attachments/510525802371219456/811962000904683550/33.png)
#### Pour cette photo-ci, il faut également mettre le code héxadécimal.
Même paterne que la photo précédente, le code hexadécimal de la couleur que vous souhaitez, sans le '#' avant, par exemple : C80108
Ce changement va affecter la couleur du pré-loader du site, actuellement rouge, vous pouvez y mettre le code héxadécimal de la couleur que vous souhaitez.<br><br><br><br>

## Autres changements types affectés aux photos

![changement Charle DEBITUS](https://cdn.discordapp.com/attachments/510525802371219456/811964161306787850/26.png)
#### Changement de texte simple
Ici, c'est un texte simple à changer. Il ne faut cependant pas se tromper et bien changer uniquement ce qu'il y a dans le rectangle jaune. Veillez à bien garder la syntaxe de Charles DEBITUS, par Jean DUPONT, par exemple, donc Prénom NOM.<br><br><br><br>

![changement DRONE33](https://cdn.discordapp.com/attachments/510525802371219456/812335670496460801/4.png)
#### Changement de texte simple
Ici encore, il faut bien respecter la syntaxe si vous voulez garder cette derniere. En effet, sur la photo y est encadré DRONE33, il faut donc remplacer DRONE33 par DRONE12 par exemple, et non DRONE 12, ou encore drone 12, drone12. Il est important de garder la même syntaxe qui est indiquer dans l'encadré jaune.<br><br><br><br>

![changement de 'tribunaux de bordeaux'](https://cdn.discordapp.com/attachments/510525802371219456/812337051973451806/23.png)
#### Autre exemple de changement
Ici, il est important de changer toute la phrase qui est encadré, même si le but final est de changer la ville. Nous avons décider de faire cela car cela nous permet de cibler les bonnes phrases à changer. Ici, il faut donc modifier la phrase totale et remplacer par : "aux tribunaux compétents de Rodez" par exemple.<br><br><br><br>


## Changement du logo, CGV et des télé-pilotes

#### Après avoir changer le texte de chacune des images présentes, passons aux changements des images du site.

Vous trouverez 4 boutons : 
* Importer un logo
* Importer photo pilote 1
* Importer photo pilote 2
* Importer CGV

Ces 4 boutons vont chacun vous ouvrir votre exploratreur de fichier et vous demander d'aller chercher l'image que vous souhaitez choisir pour : le logo, le télé-pilote 1, le télé-pilote 2 et le PDF de la nouvelle CGV.

<b>Je tiens à préciser que cette étape doit se faire APRÈS avoir fait les modifications de texte avec le slider d'image.</b>

## Une fois tous ces changement fait, merci d'appuyer sur le bouton "terminer" afin d'appliquer tous les changements au dossier du site.
Une fois appuyé sur le bouton, vous verrez le bouton devenr blanc et le rester tant que les modifications n'ont pas fini de s'appliquer sur le dossier.

![bouton terminer](https://cdn.discordapp.com/attachments/510525802371219456/813429672087781376/finish_button.png)

<br><br>

# Changement à faire à la main

### Il y a, suite a quelques modifications, des changements à faire à la main afin de s'assurer du bon changement de toutes les informations du nouveau site
* <b>Si ce n'est pas déjà fait, se connecter avec les nouveaux identifiants d'administration du site</b>
* <b>Rafraichir toutes les pages du site avec Elementor</b><br>

Pour ce faire, se connecter avec les indentifiants administrateur sur le Wordpress, et faire "modifier avec Elementor", faire un changement temporaire, qui n'impact rien (effacer une lettre et la remettre par exemple) pour avoir le bouton "mettre à jour" disponible en bas à gauche et cliquer dessus.

* <b>Rafraichir le site une fois avec l'onglet "Personaliser"</b><br>

Faire un changement temporaire, qui n'impact rien (desactiver et ré-activer une fonctionnalité par exemple) pour avoir le bouton "publier" disponible, et appuyer dessus.

### Ces changements permettent majoritairement de faire apparaître toutes les couleurs mise à jour.

Cela enlevera possiblement des images sur le site, comme des images dans les services, ou encore dans les réalisations. Il faut donc remettre ces images à la main, que ce soit par Elementor pour tout le site, et par l'onglet de personnalisation pour la page réalisation.

### Il faut refaire également la section contact dans le footer.

Les informations vont disparaitre pour cause de modifications. Pour ce faire, vous devez :

 * Aller sur l'onglet "Personnaliser" lorsque vous êtes connecté.
 * Descendre tout en bas pour apercevoir le footer.
 * Selectionner un des crayons des sections déjà existante.
 * Sur la gauche s'affiche un menu avec 3 sections, créer-en une avec les informations de contact nécéssaire.
 * Pour choisir sa position, déplacer l'onglet "contact" du menu de gauche plus ou moins en haut ou en bas des autres onglets.

### Pour changer les phrases à modifier sur l'application
Ouvrez un IDE ou un editeur de texte le fichier main.py.
Allez dans la fonction "file operation" dans lequel sont répertoriées toutes les phrases déjà changées, et changez donc une phrase existante par le nouveau texte original.

## Tous les autres changements ou personnalisations que vous n'avez pas apperçu dans notre application, ou non décrite ici, sont à faire à la main, à travers Elementor ou l'onglet personnalisation de Wordpress directement

