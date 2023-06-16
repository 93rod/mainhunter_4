import os

def detect_suspicious_file_requests(threshold):
    root_directory = os.getcwd()  # Chemin du répertoire racine

    # Dictionnaire pour stocker le nombre de demandes pour chaque fichier
    file_requests = {}

    # Parcourir le système de fichiers
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            # Chemin absolu du fichier
            file_path = os.path.join(root, file)

            # Vérifier si le fichier a déjà été demandé
            if file_path in file_requests:
                # Incrémenter le nombre de demandes pour ce fichier
                file_requests[file_path] += 1
            else:
                # Ajouter le fichier au dictionnaire avec une demande initiale de 1
                file_requests[file_path] = 1

    # Vérifier les fichiers suspects en fonction du seuil défini
    suspicious_files = []
    for file, count in file_requests.items():
        if count > threshold:
            suspicious_files.append(file)

    return suspicious_files

# un seuil de 5 demandes
suspicious_files = detect_suspicious_file_requests(7)

# Afficher les fichiers suspects
for file in suspicious_files:
    print(f"Le fichier '{file}' est suspect.")
else:
    print("Aucun fichier suspect.")