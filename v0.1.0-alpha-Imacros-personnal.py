import pyautogui
import time

#------------------------------------------First PyAutoGui test--------------------------------------------------------#
pyautogui.alert("Merci de ne pas intéragir avec les périphérique durant l'exécution des macros")
time.sleep(1)
liste_test:int=['Test changement bureau', 'test capture décran (non fonctionnelle)', 'ouverture paramètre', 'Test Ouverture Youtube (Non-fonctionnel)', 'Remplissage automatique mail']
x = pyautogui.confirm('Listes des tests :', buttons=liste_test)

#Pour futur panneau de configuration
mail :str=''

if x == 'Changement bureau':
#Changer de bureau du 1 au 2 puis du 2 au 1
        pyautogui.hotkey('ctrl', 'win', 'right')
        time.sleep(1.3)
        pyautogui.hotkey('ctrl', 'win', 'left')

elif x == 'test capture décran (non fonctionnelle)':
#capture d'écran - problème : impossibilité de choisir le nom de la capture d'écran
    test : int = pyautogui.confirm("Appuyer sur Ok quand pret pour la capture", buttons=['Ok', 'Annuler'])
    if test == 'Ok':
        name = pyautogui.prompt("entrer le nom de la capture d'écran")
        pyautogui.screenshot('capture_test_3.png')

elif x == 'Ouverture paramètre':
#Ouverture des paramètres   
    pyautogui.hotkey('win', 'i')

elif x == 'Test Ouverture Youtube (Non-fonctionnel)':

#Ouverture Youtube : Utilisation du clavier - Trop personnel
##problème : nique l'onglet ouvert ou onglet à préparer mais plus d'interet !!!
    test : int = pyautogui.confirm('test la feature Youtube', buttons=['Ok', 'Annuler'])
    if test == 'Ok':
        i : int
        X : list[int] = [214, 791, 400, 601] #avant derniere etape = écriture lien, derniere etape = click lien
        Y : list[int] = [1055, 913, 74, 540]
        time.sleep(0.4)
        for i in range(0, len(X)):
                       pyautogui.click(X[i], Y[i])
                       print("étape", i+1,"effectué") #debug
                       if i == 2:                             
                             pyautogui.typewrite("Youtube", interval=0.3)
                             time.sleep(1) #sinon page pas le temps de charger : temps minimal et le plus rapide sans bug et aléatoire: 0.7
                             pyautogui.press('enter')

#Remplissage automatique adresse mail - valentin.lallemandtignac@gmail.com
elif x == 'Remplissage automatique mail':
      #inclure dans le futur espace configuration:
      mail = pyautogui.prompt('Entrer votre adresse mail')
      #-------------------------------------------
      pyautogui.alert('Positioner la souris')
      pyautogui.click(pyautogui.position())
      pyautogui.write(mail)


      
        