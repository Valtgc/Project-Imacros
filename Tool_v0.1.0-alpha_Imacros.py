import pyautogui

x = pyautogui.confirm('Listes des outils utilisable :', buttons=['Key_Names', 'Coordonées souris'])

if x == 'Key_Names':
    pyautogui.alert(pyautogui.KEY_NAMES)

elif x == 'Coordonées souris':
    y :str = pyautogui.confirm('Souris en position ?', buttons=['Oui', 'Annuler'])   
    if y == 'Oui':
        u : str = 'Oui'
        k : int = 0
        while u == 'Oui':
            position = pyautogui.position() # current mouse x and y
            pyautogui.alert(position)
            k += 1
            print("Position", k,":", position)
            u = pyautogui.confirm('Nouvelle position à afficher ?', buttons=['Oui', 'Non'])
        