###________________________________ 25/09/2025_______________________________###
#%%
import pandas as pd

###________________Découverte des bases____________###
#%% 
#1.1 Crée une Series avec les notes de 5 étudiants
serie = [12,14,9,19,11]
Notes = pd.Series(serie , index = ["hamza" ,
                                    "houssine" ,
                                    "ayoub",
                                    "adib",
                                    "slama"])
print(Notes)

#%%
#1.2 Crée un DataFrame avec des colonnes : Nom, Âge, Ville
data = pd.DataFrame({"Nom" : ["Hamza", "Houssine", "Youssef", "Mounir"],
                    "Age" : [25,35,31,32],
                    "Ville" : ["tadla","BM","FBS","tadla"]})
data
#%%
#1.3 Lis un fichier CSV. Affiche les 10 premières lignes.
df_csv = pd.read_csv("df.csv", sep = ";")
df_csv.head(10)

#%%
#1.4 Combien de lignes et colonnes contient ton dataset ?
df_csv.shape
nb_lignes = df_csv.shape[0]
nb_colonnes = df_csv.shape[1]

print("data cette data il existe",nb_colonnes,"colonnes et",
       nb_lignes, "lignes")

###________________Sélection et filtrage_____________###
#%%
#2.1 Affiche uniquement la colonne Nom d’un DataFrame
data.loc[:,"Nom"]
#%%
#2.2 Affiche les 2 premières lignes où Âge > 30
Age_30 = data[data["Age"]>30].head(2)
Age_30

#%%
#2.3 Sélectionne les colonnes Nom et Ville pour 2 premiers
Result = data.loc[:,["Nom","Ville"]].head(2)
Result

###________________Nettoyage des données _____________###
#%%
#3.1