#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Função que inicia o bot
def iniciar_bot():
    email = email_entry.get()
    senha = senha_entry.get()

    if email and senha and arquivo_bd:
        try:
            # Iniciando o navegador
            nav = webdriver.Chrome()

            # Importa base de dados
            base_dados = pd.read_csv(arquivo_bd)
            # Entrando no site do login
            nav.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

            # Fazendo login com os dados da interface
            login_input = nav.find_element('xpath','/html/body/div[1]/div/div[2]/form/div[1]/div[1]/input').send_keys(email, Keys.TAB)
            login_senha = nav.find_element('xpath','/html/body/div[1]/div/div[2]/form/div[1]/div[2]/input').send_keys(senha, Keys.ENTER)

            # Cadastro dos produtos
            # Cadastro dos produtos
            for linha in base_dados.index:
                # Código do produto
                codigo = str(base_dados.loc[linha, 'codigo'])  # Converta para string
                codigo_produto = nav.find_element('xpath', '/html/body/div[1]/div/div[1]/div[2]/form/div[1]/div[1]/input').send_keys(codigo)
                time.sleep(1)
            
                # Marca
                marca = str(base_dados.loc[linha, 'marca'])  # Converta para string
                marca_produto = nav.find_element('xpath', '/html/body/div[1]/div/div[1]/div[2]/form/div[1]/div[2]/input').send_keys(marca)
                time.sleep(1)
            
                # Tipo
                tipo = str(base_dados.loc[linha, 'tipo'])  # Converta para string
                tipo_produto = nav.find_element('xpath', '/html/body/div[1]/div/div[1]/div[2]/form/div[1]/div[3]/input').send_keys(tipo)
                time.sleep(1)
            
                # Categoria
                categoria = str(base_dados.loc[linha, 'categoria'])  # Converta para string
                categoria_produto = nav.find_element('xpath', '/html/body/div[1]/div/div[1]/div[2]/form/div[1]/div[4]/input').send_keys(categoria)
                time.sleep(1)
            
                # Preço unitário
                preco = str(base_dados.loc[linha, 'preco_unitario'])  # Converta para string
                preco_produto = nav.find_element('xpath', '/html/body/div[1]/div/div[1]/div[2]/form/div[1]/div[5]/input').send_keys(preco)
                time.sleep(1)
            
                # Custo
                custo = str(base_dados.loc[linha, 'custo'])  # Converta para string
                custo_produto = nav.find_element('xpath', '/html/body/div[1]/div/div[1]/div[2]/form/div[1]/div[6]/input').send_keys(custo)
                time.sleep(1)
            
                # Observações
                obs = str(base_dados.loc[linha, 'obs'])  # Converta para string
                obs_produto = nav.find_element('xpath', '/html/body/div[1]/div/div[1]/div[2]/form/div[1]/div[7]/input').send_keys(obs, Keys.ENTER)
                time.sleep(1)

                
              
            messagebox.showinfo("Sucesso", "Bot finalizado com sucesso!")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao executar o bot: {str(e)}")
    else:
        messagebox.showwarning("Erro", "Por favor, insira todos os dados e selecione um banco de dados.")

# Função para selecionar o banco de dados
def selecionar_banco_dados():
    global arquivo_bd
    arquivo_bd = filedialog.askopenfilename(
        title="Selecione o Banco de Dados",
        filetypes=(("Arquivos CSV", "*.csv"), ("Todos os Arquivos", "*.*"))
    )

    if arquivo_bd:
        bd_label.config(text=f"Banco de Dados: {arquivo_bd}")
    else:
        bd_label.config(text="Nenhum banco de dados selecionado.")

# Interface gráfica com tkinter
root = tk.Tk()
root.title("Tela de Login do Bot")
root.geometry("400x300")

# Campo para email (Gmail)
email_label = tk.Label(root, text="Gmail:")
email_label.pack(pady=10)
email_entry = tk.Entry(root, width=40)
email_entry.pack()

# Campo para senha
senha_label = tk.Label(root, text="Senha:")
senha_label.pack(pady=10)
senha_entry = tk.Entry(root, show="*", width=40)
senha_entry.pack()

# Botão "Iniciar Bot"
iniciar_bot_btn = tk.Button(root, text="Iniciar Bot", command=iniciar_bot, width=20, height=2, bg="green", fg="white")
iniciar_bot_btn.pack(pady=20)

# Botão para selecionar banco de dados
selec_bd_btn = tk.Button(root, text="Selecionar Banco de Dados", command=selecionar_banco_dados, width=30)
selec_bd_btn.pack(pady=10)

# Label para exibir o banco de dados selecionado
bd_label = tk.Label(root, text="Nenhum banco de dados selecionado.")
bd_label.pack(pady=10)

# Variável global para armazenar o caminho do banco de dados
arquivo_bd = ""

# Loop da interface gráfica
root.mainloop()


# In[ ]:




