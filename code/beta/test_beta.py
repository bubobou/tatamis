import calcul_coordonnees_tatamis
import calcul_nombre_dispositions

def test_nombre_disposition():
    '''test du calcul du nombre de dispositions'''
    assert calcul_nombre_dispositions.nombre_de_dispositions(3,12)==calcul_coordonnees_tatamis.Dispositions(3,12).count
    assert calcul_nombre_dispositions.nombre_de_dispositions(14,15)==calcul_coordonnees_tatamis.Dispositions(14,15).count