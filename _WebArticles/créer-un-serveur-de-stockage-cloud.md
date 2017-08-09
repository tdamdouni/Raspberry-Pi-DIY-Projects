# Créer un serveur de stockage cloud

_Captured: 2017-05-06 at 15:29 from [the-raspberry.com](http://the-raspberry.com/owncloud)_

![](https://i0.wp.com/the-raspberry.com/wp-content/uploads/2013/12/cloud-SFR.jpg?fit=801%2C601)

Owncloud ([Owncloud.org](http://owncloud.org/)) est une alternative a Dropbox, cela vous permettre de transformer votre Raspberry pi en serveur de stockage cloud (dans le nuage).

**Wikipedia definition :**

> **[OwnCloud** ](http://fr.wikipedia.org/wiki/OwnCloud)est un logiciel libre offrant une plateforme de services de stockage et d'applications diverses en ligne (cloud computing). Owncloud peut etre installe sur n'importe quel serveur supportant une version recente de PHP (au moins 5.3) et supportant SQLite (base de donnees par defaut), MySQL ou PostgreSQL1, a l'exception notable de Mac OSX 2.

Owncloud fournit un acces universel a vos fichiers via le web, vous pourrez egalement y acceder depuis une application Android ou iOS ainsi qu'avec un [client PC, MAC ou Linux](http://owncloud.org/sync-clients/) qui synchronisera tous les fichiers. Le principe c'est que vous puissiez acceder a vos fichiers de n'importe ou.

Il comprend egalement une plate forme pour visualiser et synchroniser vos contacts, calendriers et signets sur tous vos appareils.

Pour commencer, il faut changer quelque parametre dans le menu raspi-config. Faites donc la commande :
    
    
    sudo raspi-config

Une fois dans le menu raspi-config diriger vous vers memory_split qui se trouve dans Advenced Options et changer la valeur a 16, ainsi le GPU obtient 1capture6Mo de memoire, c'est le reglage le plus petit possible.

![cloud raspberry pi](https://i2.wp.com/the-raspberry.com/wp-content/uploads/2013/12/memory-split-GPU-16.jpg?resize=511%2C303)

Ensuite, allez dans le menu Overclock et choisissez Medium a 900MHz

![Créer un serveur de stockage cloud raspberry pi](https://i2.wp.com/the-raspberry.com/wp-content/uploads/2013/12/overclocking-medium.jpg?resize=456%2C306)

Une fois ces deux reglages changes, le Raspberry pi vous proposera de redemarrer, choisissez Oui.

**1.** On met a jour tous les packets
    
    
    sudo apt-get update
    
    
    sudo apt-get upgrade

**1.1.** On fait la commande : (reglage utilisateur)
    
    
    sudo usermod -a -G www-data www-data

**2.** On installe tous les paquets necessaires a Owncloud
    
    
    sudo apt-get install apache2 php5 php5-gd php5-sqlite php5-curl php5-json php5-common php5-intl php-pear php-apc php-xml-parser libapache2-mod-php5 curl libcurl3 libcurl3-dev sqlite

**3.** On ajoute une ligne a la fin du fichier apache2.conf
    
    
    sudo nano /etc/apache2/apache2.conf

Ajouter la ligne « ServerName owncloud » a la fin du fichier
    
    
    ServerName owncloud

**3.1.** On modifie le le nom de l'host dans le fichier /ect/hosts
    
    
    sudo nano /etc/hosts

Remplacer raspberrypi par owncloud. Il faut la derniere ligne ressemble a ça
    
    
    127.0.1.1                         owncloud

**3.2.** On modifie une ligne dans un fichier
    
    
    sudo nano /etc/apache2/sites-enabled/000-default

changer le « AllowOverride None » en « AllowOverride All »

**4.** On modifie le fichier php.ini de façon a ce que la limite d'upload soit a 2Go au lieu de 2Mo.

Changer ces deux lignes comme ceci :
    
    
    upload_max_filesize = 2G
     post_max_size = 2G

Pour trouver facilement ces lignes utiliser la recherche en faisant Ctrl + W.

**5.** On supprime l'ancien index.html
    
    
    sudo rm /var/www/index.html

**6.** On active la reecriture d'Apache
    
    
    sudo a2enmod rewrite
     sudo a2enmod headers

**7.** On redemarre Apache
    
    
    sudo /etc/init.d/apache2 restart

**8.** On telecharge Owncloud
    
    
    cd
    
    
    wget http://download.owncloud.org/community/owncloud-5.0.0.tar.bz2

**9.** On extrait l'archive
    
    
    tar xvf owncloud-5.0.0.tar.bz2

**10.** On deplace le dossier owncloud vers /var/www
    
    
    sudo mv owncloud/* /var/www
     sudo mv owncloud/.htaccess /var/www

**11.** On supprime l'archive et on donne les droits a l'utilisateur (Attention cela va supprimer les fichiers precedemment ajoutes a www-data)
    
    
    rm -rf owncloud owncloud-5.0.0.tar.bz2 sudo chown -R www-data:www-data /var/www

Maintenant vous pouvez vous connecter a Owncloud, pour cela il faut entrer l'ip de votre Raspberry pi dans l'url d'un navigateur.L'ip qui se presente comme cela 192.168.x.xx est la meme que celle que vous utilisez pour vous connecter en SSH. Vous pouvez trouver cet ip a tous moment en faisant la commande
    
    
    ifconfig

Quand vous arrivez sur la page, Owncloud vous demande de creer un compte. Saisissez donc un nom d'utilisateur et un mot de passe puis cliquer sur le bouton finish setup.

![owncloud admin account create](https://i1.wp.com/the-raspberry.com/wp-content/uploads/2013/12/owncloud-admin-account-create.jpg?resize=411%2C583)

![owncloud interface](https://i0.wp.com/the-raspberry.com/wp-content/uploads/2013/12/owncloud-interface.jpg?resize=761%2C372)

Il n'est pas obligatoire de securiser Owncloud avec le protocole SSL, je le conseillerais plutot a des entreprises que a des particuliers.

**1\. **Pour commencer faites les commandes suivantes :
    
    
    sudo mkdir -p /etc/apache2/ssl
    sudo openssl req -new -x509 -days 365 -nodes -out /etc/apache2/ssl/apache.pem -keyout /etc/apache2/ssl/apache.pem
    sudo ln -sf /etc/apache2/ssl/apache.pem /etc/apache2/ssl/`/usr/bin/openssl x509 -noout -hash < /etc/apache2/ssl/apache.pem`
    sudo chmod 600 /etc/apache2/ssl/apache.pem

Des informations sur votre pays, societe, provinces… vous seront demandees. Repondez si vous le souhaitez ou appuyez sur entree pour passer la question

**2.**Ouvrir le port 443
    
    
    sudo nano /etc/apache2/ports.conf

Enlever toutes les lignes qui commencent par # et qui sont a l'interieur de <IfModule mod_ssl.c>

**3.** On redemarre Apache
    
    
    sudo service apache2 reload

**4.** On active le module SSL et on redemarre Apache
    
    
    sudo a2enmod ssl
    sudo service apache2 force-reload

**5.** Configuration de SSL
    
    
    sudo nano /etc/apache2/sites-available/ssl

Coller ceci dans le fichier vide
    
    
           SSLEngine On
           SSLCertificateFile /etc/apache2/ssl/apache.pem
           DocumentRoot /var/www

**6.** On redemarre une derniere fois
    
    
    sudo a2ensite ssl
    sudo service apache2 force-reload

Et voila, vous pouvez maintenant acceder a Owncloud en faisant https://192.168.x.xx

Si vous avez un message comme quoi l'identite de ce site Web n'a pas ete verifiee, c'est normal. Ignorer ce message.

![cadeau147582](https://i0.wp.com/the-raspberry.com/wp-content/uploads/2013/06/cadeau147582.png?resize=896%2C388)
