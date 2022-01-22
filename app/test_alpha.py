import alpha

def test_eq():
    """test de la fonction eq"""
    assert alpha.eq(1,1)==1
    assert alpha.eq(1,0)==0

def test_commut_nbre_disp():
    """test de la commutativité de la longueur et de la largeur"""
    assert alpha.nombre_de_dispositions(4,3)==alpha.nombre_de_dispositions(3,4)

def test_nombre_de_disposition():
    """test du nombre de disposition conformément à la table de D.Hickerson"""
    assert alpha.nombre_de_dispositions(5,2)==6
    assert alpha.nombre_de_dispositions(13,10)==0
    assert alpha.nombre_de_dispositions(15,2)==277
    assert alpha.nombre_de_dispositions(16,15)==2

def test_disposition_max():
    """test de la maximisation de la disposition"""
    r,s = alpha.recherche_disposition_max(30,20)
    for i in range(r+1,31):
        for j in range(s,21):
            assert alpha.nombre_de_dispositions(i,j)==0


# execution : python3 -m pytest