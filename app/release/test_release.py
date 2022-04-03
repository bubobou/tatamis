import release
import calcul_nombre_dispositions

def test_disposition_max():
    """test de la maximisation de la disposition"""
    r,s = release.recherche_disposition_max(30,20)
    for i in range(r+1,31):
        for j in range(s,21):
            assert calcul_nombre_dispositions.nombre_de_dispositions(i,j)==0

