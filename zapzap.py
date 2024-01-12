# frontend - usuaria ve e interage
# backend - logica por tras do site
# instalar biblioteca flet


#               CASE DA PROPOSTA
#  titulo do mensager
# botao de iniciar ->
#     popup 
#         bem vindo ao zapzap
#         escreva seu nome 
#         entrar no chat
# chat ->
#     escrever quem entrou no chat
#     mensagem do usuario
# campo para enviar mensagem
# botao de enviar

#importando a biblioteca
import flet as ft


def main(pagina):
    
    texto = ft.Text("Wesley ZapZap")
    nome_usuario = ft.TextField(label="Escreva seu nome")
    chat = ft.Column()                                                                   # chat em estilo coluna, mas pode ser outro tipo
 
    
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)                                       # criar tunel de conversas entre pessoas 
    
    
    def enviar_mensagem(evento):
        # colocar o nome de usuario na mensagem
        texto_campo_mensagem = f"{nome_usuario.value}:  {campo_mensagem.value}"        
        pagina.pubsub.send_all(texto_campo_mensagem)                                     # todas as mensagens vao ser salvas no tunel
        # limpar o campo_mensagem
        campo_mensagem.value = ""
        pagina.update() 
    
    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    
    botao_enviar = ft.ElevatedButton("enviar", on_click=enviar_mensagem)
    
    def entrar_chat(evento):
        #feche o popup
        popup.open = False                                                               #fechar o popup =false
        #tire o botao de "iniciar chat" da tela
        pagina.remove(botao_iniciar)                                                     # remover o popup
        # adicionar o chat
        pagina.add(chat)
        #criar o campo de enviar mensagem
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar])
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} Entrou no chat"
        pagina.pubsub.send_all(texto)    
        # botao de enviar mensagem
        pagina.update()

    popup = ft.AlertDialog(
        open=False,                                                                      # para o popup nao abrir
        modal=True,                                                                      # tipo do popup
        title=ft.Text("Bem vindo ao Wesley ZapZap"),                                             # titulo da caixa
        content=nome_usuario,                                                            # conteudo da da caixa
        actions=[ft.ElevatedButton("Entrar",on_click=entrar_chat)]                       # acao para o popup
        )
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)

    
    
    pagina.add(texto)
    pagina.add(botao_iniciar)
    
#ft.app(main)                                                                             # versao app
ft.app(main, view=ft.WEB_BROWSER)                                                       # versao site
