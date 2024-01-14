import pyautogui
import time
import pandas
# Passo 1 - Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.write("chrome")  

pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

pyautogui.click(x=689, y=503)

pyautogui.write("email@gmail.com")

pyautogui.press("tab")

pyautogui.write("minhasenha")

pyautogui.click(x=937, y=736)

time.sleep(3)



    # usar biblioteca pandas para ler arquivos
tabela = pandas.read_csv("produtos.csv")
# print(tabela)

for linha in tabela.index:
    pyautogui.click(x=1181, y=353)

    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
        
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)








