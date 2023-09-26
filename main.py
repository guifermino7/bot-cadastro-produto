# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
#       https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui # para instalar: pip install pyautogui
import time

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> aperta 1 tecla somente
# pyautogui.hothey -> atalho (combinação de teclas)
# pyautogui.PAUSE -> pausa x segundos até executar o outro comando

pyautogui.PAUSE = 0.5

# Abrir o Chrome
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

# Entrar no link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# Esperar o site carregar
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=1112, y=399) # local de onde está o mouse
pyautogui.write('guilherme.fermino7@hotmail.com') # inserir email
pyautogui.press('tab') # passar para o próximo campo (senha)
pyautogui.write('123') # inserir senha
pyautogui.press('tab') # passar para o próximo campo (logar)
pyautogui.press('enter') # apertar Logar

# Esperar o login ser realizado
time.sleep(3)

# Passo 3: Importar a base de dados de produtos
import pandas # para instalar: pip install pandas numpy openpyxl

tabela = pandas.read_csv('produtos.csv')
print(tabela)

# Passo 5: Repetir o cadastro para todos os produtos
for linha in tabela.index:

    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=1084, y=273)

    codigo = tabela.loc[linha, 'codigo'] # a coluna precisa ser o mesmo nome que está no arquivo
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']
    obs = tabela.loc[linha, 'obs']

    # Preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(preco))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # Apertar para enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    # Subir a página
    pyautogui.scroll(50000)
