# <ins>Documentation projet Drone 33




## wordpress archive version **5.6**
## Python version 3.6+
<br><br>

## Mise en place de l'application

### Installation de Python

Vous devez donc avoir python 3.6, ou plus, d'installer pour faire fonctionner notre application. Pour ce faire : <br>

Sur Mac, vous devez aller sur ce site : https://www.python.org/downloads/release/python-380/ et suivre simplement le processus d'installation. <br>
Sur Windows, allez sur un terminal et entrez : > `python3` <br>
Cela va lancer votre Microsoft store sur la page de Python à télécharger. Vous pouvez donc à partir de ce moment-là suivre le processus d'installation.<br><br>
Si rien ne s’affiche, rendez-vous directement sur le Microsoft Store et recherchez Python 3. (version la plus récente existante)


Une fois Python d'installé, vous pouvez vous rendre directement dans le dossier sur lequel vous avez installé notre application, faire :<br><br>
sur Windows :<br>
Cliquez sur la barre de chemin du dossier, et écrivez  > `cmd` <br><br>
Sur Mac :<br>
Préférences > Clavier > Raccourcis clavier > Services. Cherchez "Nouveau terminal ici" et "Nouvel onglet de terminal ici". Vous pouvez aussi les assigner à des raccourcis clavier.<br>
Après avoir effectué cela, rendez-vous sur votre dossier d'installation de notre application : <br>
Clique droit > ouvrir un terminal ici.
<br>

### Bibliothèque à installer :
*il faut bien évidement avoir python 3 et pip d'installé au préalable.* <br>
Pour installer pip, tapez donc ceci dans un terminal, peu importe votre emplacement sur le terminal:

> `pip install Pillow`

### Emplacement des dossiers/fichiers

*	Le dossier img/slider contiendra toutes les images utilisées pour afficher les changements effectuer grâce à l'application.
*	README.md est donc le fichier que vous êtes en train de lire.
*	main.py est le fichier contenant le code de l'application.

 <br>

Il faudra également mettre l'archive de votre site ainsi que le fichier « installer.php » (créée par Duplicator) à la racine de l'application. À savoir là où se trouve les dossiers et fichiers qui viennent d'être décrit.

## Notice d'utilisation de l'interface de modification de site :

### Pour vous rendre sur notre application, vous devez donc avoir un terminal ouvert à l'emplacement de notre application. Une fois cela fait, vous devez écrire dans le terminal  : 

> `python3 main.py`

Cela va donc lancer notre application pour vous retrouver sur le menu principal. Vous aurez donc accès à 2 utilisations différentes, l’option « sauvegarde » et l’option « migration ».

## La fenêtre "MIGRATION" :

### Une fois situé sur le menu principal de l'interface, sélectionner le bouton "migration"

Une fois le bouton cliqué, le bouton va se mettre en blanc et l'application va charger un peu, c'est le temps qu'il faut pour dézipper l'archive mit à la racine de l'application.
Cela va donc vous ouvrir une nouvelle fenêtre et vous offrir un panel de possibilités de changements.

## Dans un premier temps et avant toutes choses, vous devez faire les changements de textes au niveau du slider d'images que vous verrez sur l'application.
/!\ Il ne faut donc pas commencer par importer les  photos grâce aux boutons sur la gauche de la fenêtre.  /!\

### Faire les changements de texte sur votre nouveau site à migrer

La principale chose que vous allez voir son des screens avec des encadrés <b>JAUNE</b>. Ces encadrés représentent l'exactitude des changements qui vont être appliqués sur le site. Donc lorsqu'un texte est encadré d'un rectangle jaune, il faut le changer par exactement ce que vous souhaitez mettre à la place. Il est donc important de garder les majuscules, ponctuations, accents, parenthèses qui sont <b>BIEN VISIBLE DANS LE CARRÉ JAUNE</b>. Dans le cas contraire, il manquera surement ces derniers sur le site.
<br>
Pour faire un changement proprement, il faut donc :
* 1- Se trouver sur l'image correspondante au changement
* 2- Écrire le texte à modifier dans la zone de texte juste en dessous du slider d'image
* 3- Appuyer sur le bouton "valider"
* 4- Passer à l'image suivante
<br>

![menu explication](https://cdn.discordapp.com/attachments/510525802371219456/813426688360579113/menu.png)

<br>
Si vous vous êtes trompé, ou vous voulez tout simplement modifier le changement que vous aviez déjà fait, il vous suffit de revenir sur l'image du slider en question et réécrire le changement à faire dans la zone de texte, et re valider. Le nouveau changement sera pris en compte.<br>
Veillez à bien remplir chaque zone de texte et à bien appuyer sur valider pour chaque image du slider pour éviter toutes erreurs.

<br><br>

### La première photo que vous allez voir est celle-ci<br>
![changement drone 33](https://cdn.discordapp.com/attachments/510525802371219456/812384998308315176/1.png)
#### Il faut donc entrer ici le nouveau nom de votre site sous le même format que celui qui apparaît.
Ici par exemple il est affiché "drone 33" sur la photo, il faut donc que vous remplaciez par "drone 12" par exemple, et non "drone12", "Drone12", "Drone 12", "DRONE12". Tous ces types de changements seront à faire par la suite sur d'autres photos où vous verrez toutes ces différentes syntaxes à modifier et à <b>conserver</b>.<br><br><br><br>

## Il y a cependant quelques exceptions
les images suivante sont des couleurs à changer :<br>

![hoover de bouton](https://cdn.discordapp.com/attachments/510525802371219456/811700097720385536/15.png)
#### Il faut donc mettre la code hexadécimal d'une couleur
Par exemple, la couleur rouge du site drone33 est #C80108. Il faut donc bien écrire la totalité du code hexadécimal à savoir : #FFFFFF 
Ce changement va donc affecter la couleur du hover du bouton, donc la couleur qui s'affichera lorsqu'on passe la souris dessus. Sur la photo, c'est donc la couleur rosée qui va être affectée.
<br><br><br><br>

![couleur des boutons](https://cdn.discordapp.com/attachments/510525802371219456/811700772936351775/7.png)
#### Pour cette photo-ci, il faut également mettre le code hexadécimal.
Même paterne que la photo précédente, le code hexadécimal de la couleur que vous souhaitez, par exemple : #C80108 Ce changement va donc affecter la couleur des boutons du site. Cela va donc changer la couleur rouge que vous voyez par la couleur hexadécimale que vous indiquerez.<br><br><br><br>

![couleur du pre-loader](https://cdn.discordapp.com/attachments/510525802371219456/811962000904683550/33.png)
#### Pour cette photo-ci, il faut également mettre le code hexadécimal.
Même paterne que la photo précédente, le code hexadécimal de la couleur que vous souhaitez : #C80108 Ce changement va affecter la couleur du pré-loader du site, actuellement rouge, vous pouvez y mettre le code hexadécimal de la couleur que vous souhaitez.
<br><br><br><br>

## Autres changements types affectés aux photos

![changement Charle DEBITUS](https://cdn.discordapp.com/attachments/510525802371219456/811964161306787850/26.png)
#### Changement de texte simple
Ici, c'est un texte simple à changer. Il ne faut cependant pas se tromper et bien changer uniquement ce qu'il y a dans le rectangle jaune. Veillez à bien garder la syntaxe de Charles DEBITUS, par Jean DUPONT, par exemple, donc Prénom NOM.
<br><br><br><br>

![changement DRONE33](https://cdn.discordapp.com/attachments/510525802371219456/812335670496460801/4.png)
#### Changement de texte simple
Ici encore, il faut bien respecter la syntaxe si vous voulez garder cette dernière. En effet, sur la photo y est encadré DRONE33, il faut donc remplacer DRONE33 par DRONE12 par exemple, et non DRONE 12, ou encore drone 12, drone12. Il est important de garder la même syntaxe qui est indiquer dans l'encadré jaune.<br><br><br><br>

![changement de 'tribunaux de bordeaux'](https://cdn.discordapp.com/attachments/510525802371219456/812337051973451806/23.png)
#### Autre exemple de changement
Ici, il est important de changer toute la phrase qui est encadré, même si le but est de changer la ville. Nous avons décidé de faire cela car cela nous permet de cibler les bonnes phrases à changer. Ici, il faut donc modifier la phrase totale et remplacer par : "aux tribunaux compétents de Rodez" par exemple.<br><br><br><br>


## Changement du logo, CGV et des télé-pilotes

#### Après avoir changé le texte de chacune des images présentes, passons aux changements des images du site.

Vous trouverez 4 boutons : 
* Importer un logo
* Importer photo pilote 1
* Importer photo pilote 2
* Importer CGV

Ces 4 boutons vont chacun vous ouvrir votre explorateur de fichier et vous demander d'aller chercher l'image que vous souhaitez choisir pour : le logo, le télé-pilote 1, le télé-pilote 2 et le PDF de la nouvelle CGV.

## Changement du compte de l'administration

Après avoir fait les changements précédents, vous pouvez entrer dans les zones de texte en haut de l'application les renseignements demandés, à savoir votre mail, votre nom de compte et votre mot de passe pour votre compte administrateur de WordPress.

<b>Je tiens à préciser que cette étape doit se faire APRÈS avoir fait les modifications de texte avec le slider d'image.</b>

## Une fois tous ces changements fait, merci d'appuyer sur le bouton "terminer" afin d'appliquer tous les changements au dossier du site.
Une fois appuyé sur le bouton, vous verrez le bouton devenir blanc et le rester tant que les modifications n'ont pas fini de s'appliquer sur le dossier. Il va falloir donc patienter environ 3 minutes. Il se peut même que votre application ne réponde pas, c’est simplement qu’elle est en train de travailler.<br>
Une fois les changements appliqués, un message s’affichera sur l’application vous disant que vous pouvez fermer l’application sans soucis.


![bouton terminer](https://cdn.discordapp.com/attachments/510525802371219456/813429672087781376/finish_button.png)

<br><br>

# Changement à faire à la main

### Il y a, suite à quelques modifications, des changements à faire à la main afin de s'assurer du bon changement de toutes les informations du nouveau site
* <b>Si ce n'est pas déjà fait, se connecter avec les nouveaux identifiants d'administration du site</b>
* <b>Rafraichir toutes les pages du site avec Elementor</b><br>

Pour ce faire, se connecter avec les identifiants administrateur sur le Wordpress, et faire "modifier avec Elementor", faire un changement temporaire, qui n'impact rien (effacer une lettre et la remettre par exemple) pour avoir le bouton "mettre à jour" disponible en bas à gauche et cliquer dessus.

* <b>Rafraichir le site une fois avec l'onglet "Personaliser"</b><br>

Faire un changement temporaire, qui n'impact rien (désactiver et réactiver une fonctionnalité par exemple) pour avoir le bouton "publier" disponible, et appuyer dessus.

### Ces changements permettent majoritairement de faire apparaître toutes les couleurs mise à jour.

Cela enlèvera possiblement des images sur le site, comme des images dans les services, ou encore dans les réalisations. Il faut donc remettre ces images à la main, que ce soit par Elementor pour tout le site, et par l'onglet de personnalisation pour la page réalisation.

### Il faut refaire également la section contact dans le footer.

Les informations vont disparaitre pour cause de modifications. Pour ce faire, vous devez :

 * Aller sur l'onglet "Personnaliser" lorsque vous êtes connecté.
 *	Descendre tout en bas pour apercevoir le footer.
 *	Sélectionner un des crayons des sections déjà existante.
 *	Sur la gauche s'affiche un menu avec 3 sections, créer-en une avec les informations de contact nécessaire.
 *	Pour choisir sa position, déplacer l'onglet "contact" du menu de gauche plus ou moins en haut ou en bas des autres onglets.


### Changer le formulaire de contact

La zone de formulaire de contact est également à changer à la main. Pour ce faire il faut :

*	Désinstaller le plugin Contact Form 7 du nouveau site, une fois exporté.
*	Télécharger l'extension directement sur le site du créateur : https://fr.wordpress.org/plugins/contact-form-7/
*	Vérifier que le dossier du plugin a bien disparu grâce au FTP du nouveau site.
*	Prendre le dossier du plugin fraichement téléchargé et le placer grâce au FTP dans : wp-content/plugins/
*	Retourner sur la page des extensions sur WordPress (rafraichir la page si nécessaire)
*	Aller activer l'extension dans le back office du Wordpress de votre site (dans la partie administration avec les extensions)
*	Aller sur l'onglet "Contact" nouvellement apparu grâce à l'extension et remplir de nouveau les informations demandées par Contact Form 7.
*	Une fois toute les bonnes informations remplis, enregistrer le tout, copier le short-code (code court). (les informations se trouvent dans le fichier Word formulaire de contact si nécessaire)
*	Aller sur le site et modifier avec Elementor, aller sur la partie formulaire de contact et insérer le nouveau code court à la place de l'ancien (l'id et le nom devrait être différent si vous ne l'avait pas changé)


Vous pouvez enregistrer comme modèle le nouveau formulaire sur l'ancien modèle de formulaire. Grâce à cela vous pourrez copier le modèle à tous les endroits nécessaires.

### Pour changer les phrases à modifier sur l'application

Ouvrez dans un IDE ou un éditeur de code le fichier main.py. Allez dans la fonction "file operations" dans lequel sont répertoriées toutes les phrases déjà changées, et changez donc une phrase existante par le nouveau texte original.
Ces phrases se trouvent à partir de la ligne 383. **FAITES ATTENTION lorsque vous faites des changements sur le texte, les changements doivent être strictement égaux à ceux fait sur votre site, veillez à ne pas effacer les {0}, {1} etc**


## Tous les autres changements ou personnalisations que vous n'avez pas aperçu dans notre application, ou non décrite ici, sont à faire à la main, à travers Elementor ou l'onglet personnalisation de Wordpress directement
<br>
Vous pouvez notamment faire : 

* changer les photos sur site
* changer la vidéo de fond dans la page d'accueil
* changer sur rank math les informations
* Ajouter ou enlever des pages si nécéssaire
* Changer les documents officiels des télé-pilotes
* Changer le scénario de vol
* tous autres changements d'identités, d'esthétique, de personnalisation du site que vous souhaitez...


## La fenêtre "SAUVEGARDE" :

vous avez 3 possibilités : <br>

<b>Vous souhaitez mettre une archive sur un serveur FTP afin de la sauvegarder, pour ce faire :</b>

*	Rentrez vos identifiants de serveur FTP dans les champs correspondant
*	Vérifiez que votre archive ainsi que l’installeur se situe bien à la racine de l’application
*	Ecrire le nom que vous souhaitez pour votre dossier contenant l’archive ainsi que l’installeur
*	Rentrez le chemin du dossier dans lequel vous souhaitez rentrer votre archive, si vous souhaitez le mettre à la racine, écrivez « / », si vous souhaitez le mettre dans un dossier appelé « toto » qui se trouve à la racine, écrivez /toto.
*	Pour finir, appuyez sur le bouton « exporter sauv. » et patienter jusqu’à la fin du téléversement de l’archive. Le bouton va se mettre en blanc et l’application va charger votre archive sur le serveur, l’opération sera plus ou moins longue selon votre connexion internet (environ 1 minute pour un débit ascendant à 50 Mbps).

NB : l’application peut possiblement se mettre dans un état « ne répond pas » le temps de ce chargement, il est simplement nécessaire d’attendre la fin du chargement.

<br><br>

<b>Vous souhaitez importer une archive sauvegardée d’un serveur FTP :</b>

*	Rentrez vos identifiants de serveur FTP dans les champs correspondant
*	Dans le champ du nom de l’archive, veillez à bien entrer le nom que vous avez choisis lors de l’exportation
*	Appuyez sur le bouton « importer sauv. » et patienter jusqu’à la fin du téléchargement de l’archive. Le bouton va se mettre en blanc et l’application va charger votre archive sur le serveur, l’opération sera plus ou moins longue selon votre connexion internet (environ 1 minute pour un débit descendant à 50 Mbps)

NB : l’application peut possiblement se mettre dans un état « ne répond pas » le temps de ce chargement, il est simplement nécessaire d’attendre la fin du chargement.

<br><br>

**Vous souhaitez exporter votre archive nouvellement créée sur le serveur FTP correspondant à votre nom de domaine WordPress pour déployer votre site :**

*   Rentrez vos identifiants de serveur FTP dans les champs correspondant
*   Laissez vide le champ « nom de l’archive »
*   Appuyez sur le bouton « importer sauv. » et patienter jusqu’à la fin du téléchargement de l’archive. Le bouton va se mettre en blanc et l’application va charger    votre archive sur le serveur, l’opération sera plus ou moins longue selon votre connexion internet (environ 1 minute pour un débit ascendant à 50 Mbps) Il vous suffira ensuite de vous rendre sur **www.nomdevotresite.fr/installer.php**

<br><br>

**Veuillez également noter qu’il est possible de redéployer sur votre site, une archive sauvegardée (en supposant qu’elle ait été stockée au préalable)**
<br>

**Pour cela il vous suffit de récupérer votre sauvegarde comme expliqué à la 2ème possibilité, de vous rendre dans l’explorateur de fichier à l’endroit ou vous gardez le programme de notre appli, de dézipper votre archive sauvegardée qui contiendra elle-même une archive et un fichier installer.php. Une fois cela fait, veillez à bien supprimer l’archive zippée de sauvegarde. Il est TRES important qu’il ne reste que l’archive se nommant « 20201122_drone33_bc68291ed983ab026628_20210108154840_archive.zip » (ou quelque chose de similaire) et l’installer.php, vous pourrez ensuite relancer notre appli et suivre la 3ème possibilité listée ci-dessus**



