from git import Repo

projekt_mappa = "projekt_mappa"

repo = Repo.init(projekt_mappa)

fejlesztes_ag = repo.create_head("fejlesztes")
uj_feature_ag = repo.create_head("uj_feature")

repo.git.checkout("uj_feature")

with open("falj1.txt", "a") as f:
    f.write("\nVálasszon pénznemet: ")

with open("fajl2.txt", "a") as f:
    f.write("\nAdja meg az átváltani kívánt összeget: ")

repo.git.add(all=True)

repo.index.commit("Fájlmódosítások az 'új_feature' ágon")

repo.git.checkout("fejlesztes")

repo.create_head("bugfix")

repo.git.checkout("bugfix")

with open("falj3.txt", "a") as f:
    f.write("n\Mődosítás a 'bugfix'ágon")

repo.git.add(all=True)

repo.index.commit("Fájlmódosítások a 'bugfix' ágon")

print("Az összes ág és azok legújabb commitja:")
for branch in repo.branches:
    print(branch, repo,commit)

