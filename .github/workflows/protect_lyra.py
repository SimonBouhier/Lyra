import os

LICENSE_HEADER = """
''' 
Fichier {filename} - (c) Simon Bouhier 2024  
Sous licence CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/
'''
"""

def protect_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.py', '.lyra', '.md', '.txt')):  # Extensions cibles
                filepath = os.path.join(root, file)
                with open(filepath, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    if "CC BY 4.0" not in content:  # Évite les doublons
                        f.seek(0, 0)
                        f.write(LICENSE_HEADER.format(filename=file) + content)

# À exécuter depuis la racine de votre dépôt :
protect_folder('./')
