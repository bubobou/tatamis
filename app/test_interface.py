import interface
import mock
import builtins

def test_non_entier():
    """test de la fonction vérifiant si une chaîne de caract2ère
     peut être convertie en entier"""
    assert interface.non_entier("abc")==True
    assert interface.non_entier("2.7")==True
    assert interface.non_entier("2")==False

def test_reponse_existe_disposition():
    "test de la fonction affichant la réponse à savoir s'il existe ou non une disposition"
    assert interface.reponse_existe_disposition(0)=="Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo"
    assert interface.reponse_existe_disposition(1)=="Il existe au moins une disposition avec des tatamis 2x1 pour ce dojo"

def test_reponse_nombre_disposition():
    "test de la fonction affichant la réponse à connaître nombre de disposition"
    assert interface.reponse_nombre_disposition(0)=="Il existe 0 disposition possible"
    assert interface.reponse_nombre_disposition(1)=="Il existe 1 disposition possible"
    assert interface.reponse_nombre_disposition(2)=="Il existe 2 dispositions possibles"

def test_reponse_nombre_tatamis():
    "test de la fonction affichant la réponse à connaître le nombre de tatamis"
    assert interface.reponse_nombre_tatamis(5,4)=="Le nombre de tatamis 2x1 necessaires pour ce dojo est : 10"
    assert interface.reponse_nombre_tatamis(20,15)=="Le nombre de tatamis 2x1 necessaires pour ce dojo est : 150"

def test_retour_demande():
    "test du retour de la fonction demandant les dimensions : vérifie qu'une entrée de type chaîne retourne un entier "
    with mock.patch.object(builtins, 'input', lambda _: '19'):
        assert interface.demande("largeur") == 19
    with mock.patch.object(builtins, 'input', lambda _: '18'):
        assert interface.demande("longueur") == 18

def test_retour_choix_fonctionnalite():
    "test du retour du choix de fonctionnalité : vérifie que l'entrée saisie corresponde au retour de la fonction"
    with mock.patch.object(builtins, 'input', lambda _: '1'):
        assert interface.choix_fonctionnalite() == '1'
    with mock.patch.object(builtins, 'input', lambda _: '2'):
        assert interface.choix_fonctionnalite() == '2'
    with mock.patch.object(builtins, 'input', lambda _: '3'):
        assert interface.choix_fonctionnalite() == '3'
    with mock.patch.object(builtins, 'input', lambda _: 'e'):
        assert interface.choix_fonctionnalite() == 'e'

def test_demande(capsys):
    "test de la sortie (out) de la fonction demande en simulant une entrée quelconque"
    
    def mock_input(s):
        print(s, end='')
        return "19"

    interface.input = mock_input
    interface.demande("largeur")
    out, err = capsys.readouterr() 
    assert out == "Entrez la largeur (entière) de votre dojo : "
    assert err == ''

    interface.input = mock_input
    interface.demande("longueur")
    out, err = capsys.readouterr() 
    assert out == "Entrez la longueur (entière) de votre dojo : "
    assert err == ''

def test_choix_fonctionnalite(capsys):
    "test de la sortie (out) de la fonction choix_fonctionnalité en simulant une entrée quelconque"


    def mock_input(s):
        print(s, end='')
        return "1"

    interface.input = mock_input
    interface.choix_fonctionnalite()
    out, err = capsys.readouterr()

    assert out == """Que cherchez vous? Entrez : 
    \n1 pour savoir si il existe une disposition pour le dojo; 
    \n2 pour connaître le nombre de dispositions possibles; 
    \n3 pour connaître le nombre de tatamis 2x1 nécéssaires pour la taille du dojo
    \nune autre touche pour sortir du programme
    \n ? """
    assert err == ''