from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
import webbrowser
import os

class AppColetaDados(MDApp):
    num_envios = 0  # Variável de classe para rastrear o número de envios

    def build(self):
        self.tela_cadastro = Screen()
        self.tela_entrada = Screen()

        # Layout principal para a tela de cadastro
        self.layout_cadastro = FloatLayout()
        self.botao_tela_entrada = MDFloatingActionButton(
            icon="account-plus",
            size_hint=(None, None),
            size=("100dp", "100dp"),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=self.ir_para_tela_entrada
        )
        self.layout_cadastro.add_widget(self.botao_tela_entrada)

        self.tela_cadastro.add_widget(self.layout_cadastro)

        # Layout principal para a tela de entrada
        self.layout_entrada = GridLayout(cols=2, padding=10, spacing=10)

        # Campos de texto para coletar dados
        self.Cliente = MDTextField(hint_text="Cliente")
        self.marca = MDTextField(hint_text="Marca")
        self.modelo = MDTextField(hint_text="Modelo")
        self.numero_serie = MDTextField(hint_text="N. Série")
        self.tag = MDTextField(hint_text="Tag")
        self.lacre_antigo = MDTextField(hint_text="Lacre Antigo")
        self.lacre_novo = MDTextField(hint_text="Lacre Novo")
        self.reparado = MDTextField(hint_text="Reparado")
        self.prob_informado = MDTextField(hint_text="Problema Informado")
        self.prob_constatado = MDTextField(hint_text="Problema Constatado")
        self.servico_executado = MDTextField(hint_text="Serviço Executado")
        self.codigo_peca = MDTextField(hint_text="Código da Peça")
        self.obs = MDTextField(hint_text="Observações")
        self.tempo_gasto = MDTextField(hint_text="Tempo Gasto")

        # Adicionando os campos de texto ao layout principal da tela de entrada
        self.layout_entrada.add_widget(self.Cliente)
        self.layout_entrada.add_widget(self.marca)
        self.layout_entrada.add_widget(self.modelo)
        self.layout_entrada.add_widget(self.numero_serie)
        self.layout_entrada.add_widget(self.tag)
        self.layout_entrada.add_widget(self.lacre_antigo)
        self.layout_entrada.add_widget(self.lacre_novo)
        self.layout_entrada.add_widget(self.reparado)
        self.layout_entrada.add_widget(self.prob_informado)
        self.layout_entrada.add_widget(self.prob_constatado)
        self.layout_entrada.add_widget(self.servico_executado)
        self.layout_entrada.add_widget(self.codigo_peca)
        self.layout_entrada.add_widget(self.obs)
        self.layout_entrada.add_widget(self.tempo_gasto)

        # Adicionando o botão flutuante para enviar os dados
        self.botao_enviar = MDFloatingActionButton(
            icon="whatsapp",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            on_release=self.enviar_dados
        )

        # Adicionando o botão de voltar para a tela de cadastro
        self.botao_voltar = MDFloatingActionButton(
            icon="arrow-left",
            size_hint=(None, None),
            size=("56dp", "56dp"),
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_release=self.voltar_para_tela_cadastro
        )

        # Adicionando o layout à tela de entrada
        self.tela_entrada.add_widget(self.layout_entrada)
        self.tela_entrada.add_widget(self.botao_enviar)
        self.tela_entrada.add_widget(self.botao_voltar)

        return self.tela_cadastro

    def ir_para_tela_entrada(self, *args):
        self.tela_cadastro.clear_widgets()
        self.tela_cadastro.add_widget(self.tela_entrada)

    def voltar_para_tela_cadastro(self, *args):
        self.tela_cadastro.clear_widgets()
        self.tela_cadastro.add_widget(self.layout_cadastro)

    def enviar_dados(self, *args):
        # Coletar dados dos campos de texto
        Cliente = self.Cliente.text
        marca = self.marca.text
        modelo = self.modelo.text
        numero_serie = self.numero_serie.text
        tag = self.tag.text
        lacre_antigo = self.lacre_antigo.text
        lacre_novo = self.lacre_novo.text
        reparado = self.reparado.text
        prob_informado = self.prob_informado.text
        prob_constatado = self.prob_constatado.text
        servico_executado = self.servico_executado.text
        codigo_peca = self.codigo_peca.text
        obs = self.obs.text
        tempo_gasto = self.tempo_gasto.text

        # Incrementar o contador de envios
        AppColetaDados.num_envios += 1

        # Formatar os dados coletados
        dados = f"Os {AppColetaDados.num_envios}\n"
        dados += f"Cliente: {Cliente}\nMarca: {marca}\nModelo: {modelo}\nN. Série: {numero_serie}\nTag: {tag}\nLacre Antigo: {lacre_antigo}\nLacre Novo: {lacre_novo}\nReparado: {reparado}\nProblema Informado: {prob_informado}\nProblema Constatado: {prob_constatado}\nServiço Executado: {servico_executado}\nCódigo da Peça: {codigo_peca}\nObservações: {obs}\nTempo Gasto: {tempo_gasto}"

        # Salvar os dados em um arquivo TXT
        self.salvar_em_arquivo(dados)

        # Abrir o link do WhatsApp em um navegador
        link_whatsapp = f"https://wa.me/37984123858?text={dados}"
        self.abrir_link(link_whatsapp)
        
        # Mostrar a mensagem de confirmação
        self.mostrar_dialogo_confirmacao()

    def abrir_link(self, link):
        webbrowser.open(link)

    def mostrar_dialogo_confirmacao(self):
        self.dialogo = MDDialog(
            title="Dados Enviados!",
            text="Os dados foram enviados com sucesso. E arquivo txt gerado com sucesso ",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=self.limpar_campos
                )
            ]
        )
        self.dialogo.open()

    def limpar_campos(self, *args):
        # Limpar os campos de texto
        self.Cliente.text = ""
        self.marca.text = ""
        self.modelo.text = ""
        self.numero_serie.text = ""
        self.tag.text = ""
        self.lacre_antigo.text = ""
        self.lacre_novo.text = ""
        self.reparado.text = ""
        self.prob_informado.text = ""
        self.prob_constatado.text = ""
        self.servico_executado.text = ""
        self.codigo_peca.text = ""
        self.obs.text = ""
        self.tempo_gasto.text = ""
        
        # Fechar o diálogo de confirmação
        self.dialogo.dismiss()

    def salvar_em_arquivo(self, dados):
        # Verificar se o arquivo já existe
        if not os.path.exists("relatorio.txt"):
            # Se não existir, criar o arquivo e escrever os dados
            with open("relatorio.txt", "w") as file:
                file.write("Relatório de Envios:\n")
                file.write(dados)
        else:
            # Se existir, adicionar os dados ao final do arquivo
            with open("relatorio.txt", "a") as file:
                file.write("\n\n")
                file.write(dados)

AppColetaDados().run()