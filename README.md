Rootkit Hunter (mainhunter_4) est un outil puissant conçu pour renforcer la sécurité de votre système en détectant et en supprimant les rootkits, ainsi que d'autres menaces de sécurité. Il offre plusieurs fonctionnalités pour analyser les ports, les fichiers importants spécifiés dans le fichier de configuration, et comparer les empreintes de fichiers à la base de données VirusTotal. Ce fichier README donne un aperçu de mainhunter_4 et de ses fonctionnalités.

# Installation
Clonez le dépôt mainhunter_4 depuis GitHub : git clone https://github.com/93rod/mainhunter_4
Accédez au répertoire mainhunter_4 : cd mainhunter_4

# Utilisation
mainhunter_4 propose plusieurs options en ligne de commande pour effectuer différentes vérifications de sécurité :

## Analyse des ports
Pour analyser les ports ouverts sur votre système, utilisez la commande suivante :

> rootkit_hunter.py --analyse-ports

Cela effectuera une analyse de tous les ports ouverts sur votre machine et fournira un rapport sur les services suspects ou non autorisés en cours d'exécution.

## Analyse des fichiers importants
mainhunter_4 vous permet de spécifier une liste de fichiers importants dans le fichier de configuration qui doivent être surveillés pour toute modification non autorisée. Pour lancer une analyse de ces fichiers, utilisez la commande suivante :

> rootkit_hunter.py --analyse-fichiers

mainhunter_4 calculera les empreintes de fichiers des fichiers spécifiés et les comparera aux empreintes de fichiers stockées. Toute divergence sera signalée, indiquant des modifications potentielles des fichiers importants.

## Comparaison des empreintes de fichiers avec VirusTotal
mainhunter_4 intègre le service VirusTotal pour comparer les empreintes de fichiers des fichiers système à la base de données VirusTotal, qui contient des informations sur les logiciels malveillants connus. Pour effectuer cette vérification, utilisez la commande suivante :

> rootkit_hunter.py --verifier-virustotal

mainhunter_4 calculera les empreintes de fichiers des fichiers système et les comparera à la base de données VirusTotal. Si des fichiers sont identifiés comme malveillants, ils seront signalés comme des menaces potentielles pour la sécurité.

# Configuration
mainhunter_4 utilise un fichier de configuration (mainhunter_4.conf) pour spécifier divers paramètres et options. Veuillez vous référer au fichier de configuration pour des explications détaillées de chaque paramètre et personnalisez-les selon vos besoins.

Contributions
Nous encourageons les contributions pour améliorer la fonctionnalité et la sécurité de mainhunter_4. Si vous rencontrez des problèmes ou avez des suggestions d'améliorations, veuillez les soumettre via le dépôt GitHub.

# Licence
mainhunter_4 est publié sous la licence MIT. Veuillez consulter le fichier LICENSE pour plus de détails.

# Avertissement
mainhunter_4 est un outil puissant pour renforcer la sécurité de votre système. Cependant, il doit être utilisé de manière responsable et en conformité avec les lois et réglementations applicables. Les développeurs de mainhunter_4 ne sont pas responsables de toute mauvaise utilisation ou dommage causé par l'outil.

## Remarque : N'oubliez pas de mettre régulièrement à jour mainhunter_4 et de maintenir votre système à jour avec les correctifs de sécurité pour assurer une protection optimale contre les menaces en constante évolution.

Pour plus d'informations, veuillez vous référer à la documentation complète disponible dans le dépôt.

Merci d'utiliser Rootkit Hunter (mainhunter_4) pour renforcer la sécurité de votre système !
