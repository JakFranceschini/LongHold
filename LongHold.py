import os
import sys
import pandas as pd
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSettings, Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QGridLayout, QHBoxLayout, QFrame, QPushButton, QScrollArea, QLabel, QSpacerItem, QSizePolicy

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1050, 550)
        self.setWindowIcon(QIcon('./assets/icon.ico'))
        self.setWindowTitle('LongHold')

        self.posicao_tamanho_janela = QSettings('LongHold', 'MeuApp')
        self.gerenciar_posicao_tamanho_janela()

        self.aplicar_estilo('./style/style.css')

        self.ativos = pd.read_csv("https://docs.google.com/spreadsheets/d/1sSujoT_tUBA0bHWRpn0aDf59cGpU0tTg3AVzBnFgbUo/export?format=csv&gid=0")
        self.totais = pd.read_csv("https://docs.google.com/spreadsheets/d/1sSujoT_tUBA0bHWRpn0aDf59cGpU0tTg3AVzBnFgbUo/export?format=csv&gid=1590878666")
        self.reservas = pd.read_csv("https://docs.google.com/spreadsheets/d/1sSujoT_tUBA0bHWRpn0aDf59cGpU0tTg3AVzBnFgbUo/export?format=csv&gid=1376608033")
        self.alocacao = pd.read_csv("https://docs.google.com/spreadsheets/d/1sSujoT_tUBA0bHWRpn0aDf59cGpU0tTg3AVzBnFgbUo/export?format=csv&gid=947935505")
        self.proventos = pd.read_csv("https://docs.google.com/spreadsheets/d/1sSujoT_tUBA0bHWRpn0aDf59cGpU0tTg3AVzBnFgbUo/export?format=csv&gid=1266693739")
        self.rentabilidades = pd.read_csv("https://docs.google.com/spreadsheets/d/1sSujoT_tUBA0bHWRpn0aDf59cGpU0tTg3AVzBnFgbUo/export?format=csv&gid=1835204809")

        widget_principal = QWidget()
        widget_principal.setObjectName('widget_principal')
        layout_widget_principal = QVBoxLayout(widget_principal)
        layout_widget_principal.setContentsMargins(0, 0, 0, 0)
        layout_widget_principal.setSpacing(0)
        self.setCentralWidget(widget_principal)

        scroll_area = QScrollArea()
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        layout_widget_principal.addWidget(scroll_area)

        conteudo_scroll = QWidget()
        conteudo_scroll.setObjectName('conteudo_scroll')
        layout_conteudo_scroll = QHBoxLayout(conteudo_scroll)
        layout_conteudo_scroll.setContentsMargins(0, 20, 0, 20)
        layout_conteudo_scroll.setSpacing(15)
        layout_conteudo_scroll.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_area.setWidget(conteudo_scroll)

        layout_conteudo_scroll.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

        layout_central = QVBoxLayout()
        layout_central.setContentsMargins(0, 0, 0, 0)
        layout_central.setSpacing(25)
        layout_conteudo_scroll.addLayout(layout_central)

        layout_conteudo_scroll.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

        barra_superior = QFrame()
        layout_barra_superior = QVBoxLayout(barra_superior)
        layout_barra_superior.setContentsMargins(0, 40, 0, 40)
        layout_barra_superior.setSpacing(5)
        layout_central.addWidget(barra_superior)

        titulo_barra_superior = QLabel('LongHold')
        titulo_barra_superior.setObjectName('titulo_barra_superior')
        layout_barra_superior.addWidget(titulo_barra_superior)

        subtitulo_barra_superior = QLabel('Meu app de acompanhamento de patrimônio.')
        subtitulo_barra_superior.setObjectName('subtitulo_barra_superior')
        layout_barra_superior.addWidget(subtitulo_barra_superior)

        card_patrimonio = QFrame()
        card_patrimonio.setObjectName('cards')
        layout_card_patrimonio = QVBoxLayout(card_patrimonio)
        layout_card_patrimonio.setContentsMargins(20, 20, 20, 20)
        layout_card_patrimonio.setSpacing(60)
        layout_central.addWidget(card_patrimonio)

        area_titulos_card_patrimonio = QFrame()
        layout_area_titulos_card_patrimonio = QVBoxLayout(area_titulos_card_patrimonio)
        layout_area_titulos_card_patrimonio.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_patrimonio.setSpacing(5)
        layout_card_patrimonio.addWidget(area_titulos_card_patrimonio)

        titulo_card_patrimonio = QLabel('Patrimônio')
        titulo_card_patrimonio.setObjectName('titulos_cards')
        layout_area_titulos_card_patrimonio.addWidget(titulo_card_patrimonio)

        subtitulo_card_patrimonio = QLabel('Visão geral do patrimônio atual, total aportado e variação.')
        subtitulo_card_patrimonio.setObjectName('subtitulos_cards')
        layout_area_titulos_card_patrimonio.addWidget(subtitulo_card_patrimonio)

        area_valores_card_patrimonio = QFrame()
        layout_area_valores_card_patrimonio = QGridLayout(area_valores_card_patrimonio)
        layout_area_valores_card_patrimonio.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_patrimonio.setSpacing(20)
        layout_card_patrimonio.addWidget(area_valores_card_patrimonio)

        card_patrimonio_atual = QFrame()
        card_patrimonio_atual.setObjectName("cards_secundarios")
        layout_card_patrimonio_atual = QVBoxLayout(card_patrimonio_atual)
        layout_card_patrimonio_atual.setContentsMargins(0, 0, 0, 0)
        layout_card_patrimonio_atual.setSpacing(10)
        layout_area_valores_card_patrimonio.addWidget(card_patrimonio_atual, 0, 0)

        titulo_card_patrimonio_atual = QLabel("Patrimônio atual")
        titulo_card_patrimonio_atual.setObjectName("titulos_cards_secundarios")
        layout_card_patrimonio_atual.addWidget(titulo_card_patrimonio_atual)

        self.valor_card_patrimonio_atual = QLabel("R$ 0,00")
        self.valor_card_patrimonio_atual.setObjectName("valores_cards_secundarios")
        layout_card_patrimonio_atual.addWidget(self.valor_card_patrimonio_atual)

        card_aporte_total_patrimonio = QFrame()
        card_aporte_total_patrimonio.setObjectName("cards_secundarios")
        layout_card_aporte_total_patrimonio = QVBoxLayout(card_aporte_total_patrimonio)
        layout_card_aporte_total_patrimonio.setContentsMargins(0, 0, 0, 0)
        layout_card_aporte_total_patrimonio.setSpacing(10)
        layout_area_valores_card_patrimonio.addWidget(card_aporte_total_patrimonio, 0, 1)

        titulo_card_aporte_total_patrimonio = QLabel("Total aportado")
        titulo_card_aporte_total_patrimonio.setObjectName("titulos_cards_secundarios")
        layout_card_aporte_total_patrimonio.addWidget(titulo_card_aporte_total_patrimonio)

        self.valor_card_aporte_total_patrimonio = QLabel("R$ 0,00")
        self.valor_card_aporte_total_patrimonio.setObjectName("valores_cards_secundarios")
        layout_card_aporte_total_patrimonio.addWidget(self.valor_card_aporte_total_patrimonio)

        card_variacao_patrimonio = QFrame()
        card_variacao_patrimonio.setObjectName("cards_secundarios")
        layout_card_variacao_patrimonio = QVBoxLayout(card_variacao_patrimonio)
        layout_card_variacao_patrimonio.setContentsMargins(0, 0, 0, 0)
        layout_card_variacao_patrimonio.setSpacing(10)
        layout_area_valores_card_patrimonio.addWidget(card_variacao_patrimonio, 0, 2)

        titulo_card_variacao_patrimonio = QLabel("Variação")
        titulo_card_variacao_patrimonio.setObjectName("titulos_cards_secundarios")
        layout_card_variacao_patrimonio.addWidget(titulo_card_variacao_patrimonio)

        self.valor_card_variacao_patrimonio = QLabel("R$ 0,00")
        self.valor_card_variacao_patrimonio.setObjectName("valores_cards_secundarios")
        layout_card_variacao_patrimonio.addWidget(self.valor_card_variacao_patrimonio)

        self.carregar_dados_card_patrimonio()

        card_reservas = QFrame()
        card_reservas.setObjectName('cards')
        layout_card_reservas = QVBoxLayout(card_reservas)
        layout_card_reservas.setContentsMargins(20, 20, 20, 20)
        layout_card_reservas.setSpacing(60)
        layout_central.addWidget(card_reservas)

        area_titulos_card_reservas = QFrame()
        layout_area_titulos_card_reservas = QVBoxLayout(area_titulos_card_reservas)
        layout_area_titulos_card_reservas.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_reservas.setSpacing(5)
        layout_card_reservas.addWidget(area_titulos_card_reservas)

        titulo_card_reservas = QLabel('Reservas')
        titulo_card_reservas.setObjectName('titulos_cards')
        layout_area_titulos_card_reservas.addWidget(titulo_card_reservas)

        subtitulo_card_reservas = QLabel('Visão geral das minhas reservas totais, conta corrente e reserva de emergência.')
        subtitulo_card_reservas.setObjectName('subtitulos_cards')
        layout_area_titulos_card_reservas.addWidget(subtitulo_card_reservas)

        area_valores_card_reservas = QFrame()
        layout_area_valores_card_reservas = QGridLayout(area_valores_card_reservas)
        layout_area_valores_card_reservas.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_reservas.setSpacing(20)
        layout_card_reservas.addWidget(area_valores_card_reservas)

        card_reservas_totais = QFrame()
        card_reservas_totais.setObjectName("cards_secundarios")
        layout_card_reservas_totais = QVBoxLayout(card_reservas_totais)
        layout_card_reservas_totais.setContentsMargins(0, 0, 0, 0)
        layout_card_reservas_totais.setSpacing(10)
        layout_area_valores_card_reservas.addWidget(card_reservas_totais, 0, 0)

        titulo_card_reservas_totais = QLabel("Reservas totais")
        titulo_card_reservas_totais.setObjectName("titulos_cards_secundarios")
        layout_card_reservas_totais.addWidget(titulo_card_reservas_totais)

        self.valor_card_reservas_totais = QLabel("R$ 0,00")
        self.valor_card_reservas_totais.setObjectName("valores_cards_secundarios")
        layout_card_reservas_totais.addWidget(self.valor_card_reservas_totais)

        card_conta_corrente = QFrame()
        card_conta_corrente.setObjectName("cards_secundarios")
        layout_card_conta_corrente = QVBoxLayout(card_conta_corrente)
        layout_card_conta_corrente.setContentsMargins(0, 0, 0, 0)
        layout_card_conta_corrente.setSpacing(10)
        layout_area_valores_card_reservas.addWidget(card_conta_corrente, 0, 1)

        titulo_card_conta_corrente = QLabel("Conta corrente")
        titulo_card_conta_corrente.setObjectName("titulos_cards_secundarios")
        layout_card_conta_corrente.addWidget(titulo_card_conta_corrente)

        self.valor_card_conta_corrente = QLabel("R$ 0,00")
        self.valor_card_conta_corrente.setObjectName("valores_cards_secundarios")
        layout_card_conta_corrente.addWidget(self.valor_card_conta_corrente)

        card_reserva_emergencia = QFrame()
        card_reserva_emergencia.setObjectName("cards_secundarios")
        layout_card_reserva_emergencia = QVBoxLayout(card_reserva_emergencia)
        layout_card_reserva_emergencia.setContentsMargins(0, 0, 0, 0)
        layout_card_reserva_emergencia.setSpacing(10)
        layout_area_valores_card_reservas.addWidget(card_reserva_emergencia, 0, 2)

        titulo_card_reserva_emergencia = QLabel("Reserva de emergência")
        titulo_card_reserva_emergencia.setObjectName("titulos_cards_secundarios")
        layout_card_reserva_emergencia.addWidget(titulo_card_reserva_emergencia)

        self.valor_card_reserva_emergencia = QLabel("R$ 0,00")
        self.valor_card_reserva_emergencia.setObjectName("valores_cards_secundarios")
        layout_card_reserva_emergencia.addWidget(self.valor_card_reserva_emergencia)

        self.carregar_dados_card_reservas()

        card_investimentos = QFrame()
        card_investimentos.setObjectName('cards')
        layout_card_investimentos = QVBoxLayout(card_investimentos)
        layout_card_investimentos.setContentsMargins(20, 20, 20, 20)
        layout_card_investimentos.setSpacing(60)
        layout_central.addWidget(card_investimentos)

        area_titulos_card_investimentos = QFrame()
        layout_area_titulos_card_investimentos = QVBoxLayout(area_titulos_card_investimentos)
        layout_area_titulos_card_investimentos.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_investimentos.setSpacing(5)
        layout_card_investimentos.addWidget(area_titulos_card_investimentos)

        titulo_card_investimentos = QLabel('Investimentos')
        titulo_card_investimentos.setObjectName('titulos_cards')
        layout_area_titulos_card_investimentos.addWidget(titulo_card_investimentos)

        subtitulo_card_investimentos = QLabel('Visão geral do total investido, total aportado e variação.')
        subtitulo_card_investimentos.setObjectName('subtitulos_cards')
        layout_area_titulos_card_investimentos.addWidget(subtitulo_card_investimentos)

        area_valores_card_investimentos = QFrame()
        layout_area_valores_card_investimentos = QGridLayout(area_valores_card_investimentos)
        layout_area_valores_card_investimentos.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_investimentos.setSpacing(20)
        layout_card_investimentos.addWidget(area_valores_card_investimentos)

        card_total_investimentos = QFrame()
        card_total_investimentos.setObjectName("cards_secundarios")
        layout_card_total_investimentos = QVBoxLayout(card_total_investimentos)
        layout_card_total_investimentos.setContentsMargins(0, 0, 0, 0)
        layout_card_total_investimentos.setSpacing(10)
        layout_area_valores_card_investimentos.addWidget(card_total_investimentos, 0, 0)

        titulo_card_total_investimentos = QLabel("Total em investimentos")
        titulo_card_total_investimentos.setObjectName("titulos_cards_secundarios")
        layout_card_total_investimentos.addWidget(titulo_card_total_investimentos)

        self.valor_card_total_investimentos = QLabel("R$ 0,00")
        self.valor_card_total_investimentos.setObjectName("valores_cards_secundarios")
        layout_card_total_investimentos.addWidget(self.valor_card_total_investimentos)

        card_total_aportado_investimentos = QFrame()
        card_total_aportado_investimentos.setObjectName("cards_secundarios")
        layout_card_total_aportado_investimentos = QVBoxLayout(card_total_aportado_investimentos)
        layout_card_total_aportado_investimentos.setContentsMargins(0, 0, 0, 0)
        layout_card_total_aportado_investimentos.setSpacing(10)
        layout_area_valores_card_investimentos.addWidget(card_total_aportado_investimentos, 0, 1)

        titulo_card_total_aportado_investimentos = QLabel("Total aportado")
        titulo_card_total_aportado_investimentos.setObjectName("titulos_cards_secundarios")
        layout_card_total_aportado_investimentos.addWidget(titulo_card_total_aportado_investimentos)

        self.valor_card_total_aportado_investimentos = QLabel("R$ 0,00")
        self.valor_card_total_aportado_investimentos.setObjectName("valores_cards_secundarios")
        layout_card_total_aportado_investimentos.addWidget(self.valor_card_total_aportado_investimentos)

        card_variacao_investimentos = QFrame()
        card_variacao_investimentos.setObjectName("cards_secundarios")
        layout_card_variacao_investimentos = QVBoxLayout(card_variacao_investimentos)
        layout_card_variacao_investimentos.setContentsMargins(0, 0, 0, 0)
        layout_card_variacao_investimentos.setSpacing(10)
        layout_area_valores_card_investimentos.addWidget(card_variacao_investimentos, 0, 2)

        titulo_card_variacao_investimentos = QLabel("Variação")
        titulo_card_variacao_investimentos.setObjectName("titulos_cards_secundarios")
        layout_card_variacao_investimentos.addWidget(titulo_card_variacao_investimentos)

        self.valor_card_variacao_investimentos = QLabel("R$ 0,00")
        self.valor_card_variacao_investimentos.setObjectName("valores_cards_secundarios")
        layout_card_variacao_investimentos.addWidget(self.valor_card_variacao_investimentos)

        self.carregar_dados_card_investimentos()

        card_alocacao = QFrame()
        card_alocacao.setObjectName('cards')
        layout_card_alocacao = QVBoxLayout(card_alocacao)
        layout_card_alocacao.setContentsMargins(20, 20, 20, 20)
        layout_card_alocacao.setSpacing(60)
        layout_central.addWidget(card_alocacao)

        area_titulos_card_alocacao = QFrame()
        layout_area_titulos_card_alocacao = QVBoxLayout(area_titulos_card_alocacao)
        layout_area_titulos_card_alocacao.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_alocacao.setSpacing(5)
        layout_card_alocacao.addWidget(area_titulos_card_alocacao)

        titulo_card_alocacao = QLabel('Alocação')
        titulo_card_alocacao.setObjectName('titulos_cards')
        layout_area_titulos_card_alocacao.addWidget(titulo_card_alocacao)

        subtitulo_card_alocacao = QLabel('Visão geral da alocação atual dos investimentos, alocação ideal e da diferença.')
        subtitulo_card_alocacao.setObjectName('subtitulos_cards')
        layout_area_titulos_card_alocacao.addWidget(subtitulo_card_alocacao)

        area_valores_card_alocacao = QFrame()
        layout_area_valores_card_alocacao = QGridLayout(area_valores_card_alocacao)
        layout_area_valores_card_alocacao.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_alocacao.setSpacing(20)
        layout_card_alocacao.addWidget(area_valores_card_alocacao)

        card_stocks_alocacao = QFrame()
        card_stocks_alocacao.setObjectName("cards_secundarios")
        layout_card_stocks_alocacao = QVBoxLayout(card_stocks_alocacao)
        layout_card_stocks_alocacao.setContentsMargins(0, 0, 0, 0)
        layout_card_stocks_alocacao.setSpacing(10)
        layout_area_valores_card_alocacao.addWidget(card_stocks_alocacao, 0, 0)

        titulo_card_stocks_alocacao = QLabel("Stocks")
        titulo_card_stocks_alocacao.setObjectName("titulos_cards_secundarios")
        layout_card_stocks_alocacao.addWidget(titulo_card_stocks_alocacao)

        self.valor_card_stocks_alocacao = QLabel("0.00%")
        self.valor_card_stocks_alocacao.setObjectName("valores_cards_secundarios")
        layout_card_stocks_alocacao.addWidget(self.valor_card_stocks_alocacao)

        self.valor_alocacao_ideal_stocks = QLabel("0.00%")
        self.valor_alocacao_ideal_stocks.setObjectName("subvalores_cards_secundarios")
        layout_card_stocks_alocacao.addWidget(self.valor_alocacao_ideal_stocks)

        self.valor_alocacao_diferenca_stocks = QLabel("0.00%")
        self.valor_alocacao_diferenca_stocks.setObjectName("subvalores_cards_secundarios")
        layout_card_stocks_alocacao.addWidget(self.valor_alocacao_diferenca_stocks)

        card_reits_alocacao = QFrame()
        card_reits_alocacao.setObjectName("cards_secundarios")
        layout_card_reits_alocacao = QVBoxLayout(card_reits_alocacao)
        layout_card_reits_alocacao.setContentsMargins(0, 0, 0, 0)
        layout_card_reits_alocacao.setSpacing(10)
        layout_area_valores_card_alocacao.addWidget(card_reits_alocacao, 0, 1)

        titulo_card_reits_alocacao = QLabel("Reits")
        titulo_card_reits_alocacao.setObjectName("titulos_cards_secundarios")
        layout_card_reits_alocacao.addWidget(titulo_card_reits_alocacao)

        self.valor_card_reits_alocacao = QLabel("0.00%")
        self.valor_card_reits_alocacao.setObjectName("valores_cards_secundarios")
        layout_card_reits_alocacao.addWidget(self.valor_card_reits_alocacao)

        self.valor_alocacao_ideal_reits = QLabel("0.00%")
        self.valor_alocacao_ideal_reits.setObjectName("subvalores_cards_secundarios")
        layout_card_reits_alocacao.addWidget(self.valor_alocacao_ideal_reits)

        self.valor_alocacao_diferenca_reits = QLabel("0.00%")
        self.valor_alocacao_diferenca_reits.setObjectName("subvalores_cards_secundarios")
        layout_card_reits_alocacao.addWidget(self.valor_alocacao_diferenca_reits)

        card_acoes_alocacao = QFrame()
        card_acoes_alocacao.setObjectName("cards_secundarios")
        layout_card_acoes_alocacao = QVBoxLayout(card_acoes_alocacao)
        layout_card_acoes_alocacao.setContentsMargins(0, 0, 0, 0)
        layout_card_acoes_alocacao.setSpacing(10)
        layout_area_valores_card_alocacao.addWidget(card_acoes_alocacao, 0, 2)

        titulo_card_acoes_alocacao = QLabel("Ações")
        titulo_card_acoes_alocacao.setObjectName("titulos_cards_secundarios")
        layout_card_acoes_alocacao.addWidget(titulo_card_acoes_alocacao)

        self.valor_card_acoes_alocacao = QLabel("0.00%")
        self.valor_card_acoes_alocacao.setObjectName("valores_cards_secundarios")
        layout_card_acoes_alocacao.addWidget(self.valor_card_acoes_alocacao)

        self.valor_alocacao_ideal_acoes = QLabel("0.00%")
        self.valor_alocacao_ideal_acoes.setObjectName("subvalores_cards_secundarios")
        layout_card_acoes_alocacao.addWidget(self.valor_alocacao_ideal_acoes)

        self.valor_alocacao_diferenca_acoes = QLabel("0.00%")
        self.valor_alocacao_diferenca_acoes.setObjectName("subvalores_cards_secundarios")
        layout_card_acoes_alocacao.addWidget(self.valor_alocacao_diferenca_acoes)

        card_fiis_alocacao = QFrame()
        card_fiis_alocacao.setObjectName("cards_secundarios")
        layout_card_fiis_alocacao = QVBoxLayout(card_fiis_alocacao)
        layout_card_fiis_alocacao.setContentsMargins(0, 0, 0, 0)
        layout_card_fiis_alocacao.setSpacing(10)
        layout_area_valores_card_alocacao.addWidget(card_fiis_alocacao, 1, 0)

        titulo_card_fiis_alocacao = QLabel("Fiis")
        titulo_card_fiis_alocacao.setObjectName("titulos_cards_secundarios")
        layout_card_fiis_alocacao.addWidget(titulo_card_fiis_alocacao)

        self.valor_card_fiis_alocacao = QLabel("0.00%")
        self.valor_card_fiis_alocacao.setObjectName("valores_cards_secundarios")
        layout_card_fiis_alocacao.addWidget(self.valor_card_fiis_alocacao)

        self.valor_alocacao_ideal_fiis = QLabel("0.00%")
        self.valor_alocacao_ideal_fiis.setObjectName("subvalores_cards_secundarios")
        layout_card_fiis_alocacao.addWidget(self.valor_alocacao_ideal_fiis)

        self.valor_alocacao_diferenca_fiis = QLabel("0.00%")
        self.valor_alocacao_diferenca_fiis.setObjectName("subvalores_cards_secundarios")
        layout_card_fiis_alocacao.addWidget(self.valor_alocacao_diferenca_fiis)

        card_criptos_alocacao = QFrame()
        card_criptos_alocacao.setObjectName("cards_secundarios")
        layout_card_criptos_alocacao = QVBoxLayout(card_criptos_alocacao)
        layout_card_criptos_alocacao.setContentsMargins(0, 0, 0, 0)
        layout_card_criptos_alocacao.setSpacing(10)
        layout_area_valores_card_alocacao.addWidget(card_criptos_alocacao, 1, 1)

        titulo_card_criptos_alocacao = QLabel("Criptos")
        titulo_card_criptos_alocacao.setObjectName("titulos_cards_secundarios")
        layout_card_criptos_alocacao.addWidget(titulo_card_criptos_alocacao)

        self.valor_card_criptos_alocacao = QLabel("0.00%")
        self.valor_card_criptos_alocacao.setObjectName("valores_cards_secundarios")
        layout_card_criptos_alocacao.addWidget(self.valor_card_criptos_alocacao)

        self.valor_alocacao_ideal_criptos = QLabel("0.00%")
        self.valor_alocacao_ideal_criptos.setObjectName("subvalores_cards_secundarios")
        layout_card_criptos_alocacao.addWidget(self.valor_alocacao_ideal_criptos)

        self.valor_alocacao_diferenca_criptos = QLabel("0.00%")
        self.valor_alocacao_diferenca_criptos.setObjectName("subvalores_cards_secundarios")
        layout_card_criptos_alocacao.addWidget(self.valor_alocacao_diferenca_criptos)

        self.carregar_dados_card_alocacao()

        card_aporte = QFrame()
        card_aporte.setObjectName('cards')
        layout_card_aporte = QVBoxLayout(card_aporte)
        layout_card_aporte.setContentsMargins(20, 20, 20, 20)
        layout_card_aporte.setSpacing(60)
        layout_central.addWidget(card_aporte)

        area_titulos_card_aporte = QFrame()
        layout_area_titulos_card_aporte = QVBoxLayout(area_titulos_card_aporte)
        layout_area_titulos_card_aporte.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_aporte.setSpacing(5)
        layout_card_aporte.addWidget(area_titulos_card_aporte)

        titulo_card_aporte = QLabel('Aporte')
        titulo_card_aporte.setObjectName('titulos_cards')
        layout_area_titulos_card_aporte.addWidget(titulo_card_aporte)

        subtitulo_card_aporte = QLabel('Visão geral da classe e do ativo do próximo aporte.')
        subtitulo_card_aporte.setObjectName('subtitulos_cards')
        layout_area_titulos_card_aporte.addWidget(subtitulo_card_aporte)

        area_valores_card_aporte = QFrame()
        layout_area_valores_card_aporte = QGridLayout(area_valores_card_aporte)
        layout_area_valores_card_aporte.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_aporte.setSpacing(20)
        layout_card_aporte.addWidget(area_valores_card_aporte)

        card_classe_aporte = QFrame()
        card_classe_aporte.setObjectName("cards_secundarios")
        layout_card_classe_aporte = QVBoxLayout(card_classe_aporte)
        layout_card_classe_aporte.setContentsMargins(0, 0, 0, 0)
        layout_card_classe_aporte.setSpacing(10)
        layout_area_valores_card_aporte.addWidget(card_classe_aporte, 0, 0)

        titulo_card_classe_aporte = QLabel("Classe")
        titulo_card_classe_aporte.setObjectName("titulos_cards_secundarios")
        layout_card_classe_aporte.addWidget(titulo_card_classe_aporte)

        self.valor_card_classe_aporte = QLabel()
        self.valor_card_classe_aporte.setObjectName("valores_cards_secundarios")
        layout_card_classe_aporte.addWidget(self.valor_card_classe_aporte)

        card_ticker_aporte = QFrame()
        card_ticker_aporte.setObjectName("cards_secundarios")
        layout_card_ticker_aporte = QVBoxLayout(card_ticker_aporte)
        layout_card_ticker_aporte.setContentsMargins(0, 0, 0, 0)
        layout_card_ticker_aporte.setSpacing(10)
        layout_area_valores_card_aporte.addWidget(card_ticker_aporte, 0, 1)

        titulo_card_ticker_aporte = QLabel("Ticker")
        titulo_card_ticker_aporte.setObjectName("titulos_cards_secundarios")
        layout_card_ticker_aporte.addWidget(titulo_card_ticker_aporte)

        self.valor_card_ticker_aporte = QLabel()
        self.valor_card_ticker_aporte.setObjectName("valores_cards_secundarios")
        layout_card_ticker_aporte.addWidget(self.valor_card_ticker_aporte)

        card_vazio = QFrame()
        layout_area_valores_card_aporte.addWidget(card_vazio, 0, 2)

        self.carregar_dados_card_aporte()

        card_proventos = QFrame()
        card_proventos.setObjectName('cards')
        layout_card_proventos = QVBoxLayout(card_proventos)
        layout_card_proventos.setContentsMargins(20, 20, 20, 20)
        layout_card_proventos.setSpacing(60)
        layout_central.addWidget(card_proventos)

        area_titulos_card_proventos = QFrame()
        layout_area_titulos_card_proventos = QVBoxLayout(area_titulos_card_proventos)
        layout_area_titulos_card_proventos.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_proventos.setSpacing(5)
        layout_card_proventos.addWidget(area_titulos_card_proventos)

        titulo_card_proventos = QLabel('Proventos')
        titulo_card_proventos.setObjectName('titulos_cards')
        layout_area_titulos_card_proventos.addWidget(titulo_card_proventos)

        subtitulo_card_proventos = QLabel('Visão geral do total ja recebido em proventos e os proventos recebidos ao longo dos anos.')
        subtitulo_card_proventos.setObjectName('subtitulos_cards')
        layout_area_titulos_card_proventos.addWidget(subtitulo_card_proventos)

        area_valores_card_proventos = QFrame()
        layout_area_valores_card_proventos = QGridLayout(area_valores_card_proventos)
        layout_area_valores_card_proventos.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_proventos.setSpacing(20)
        layout_card_proventos.addWidget(area_valores_card_proventos)

        card_total_recebido_proventos = QFrame()
        card_total_recebido_proventos.setObjectName("cards_secundarios")
        layout_card_total_recebido_proventos = QVBoxLayout(card_total_recebido_proventos)
        layout_card_total_recebido_proventos.setContentsMargins(0, 0, 0, 0)
        layout_card_total_recebido_proventos.setSpacing(10)
        layout_area_valores_card_proventos.addWidget(card_total_recebido_proventos, 0, 0)

        titulo_card_total_recebido_proventos = QLabel("Total recebido")
        titulo_card_total_recebido_proventos.setObjectName("titulos_cards_secundarios")
        layout_card_total_recebido_proventos.addWidget(titulo_card_total_recebido_proventos)

        self.valor_card_total_recebido_proventos = QLabel()
        self.valor_card_total_recebido_proventos.setObjectName("valores_cards_secundarios")
        layout_card_total_recebido_proventos.addWidget(self.valor_card_total_recebido_proventos)

        card_2019_proventos = QFrame()
        card_2019_proventos.setObjectName("cards_secundarios")
        layout_card_2019_proventos = QVBoxLayout(card_2019_proventos)
        layout_card_2019_proventos.setContentsMargins(0, 0, 0, 0)
        layout_card_2019_proventos.setSpacing(10)
        layout_area_valores_card_proventos.addWidget(card_2019_proventos, 0, 1)

        titulo_card_2019_proventos = QLabel("2019")
        titulo_card_2019_proventos.setObjectName("titulos_cards_secundarios")
        layout_card_2019_proventos.addWidget(titulo_card_2019_proventos)

        self.valor_card_2019_proventos = QLabel()
        self.valor_card_2019_proventos.setObjectName("valores_cards_secundarios")
        layout_card_2019_proventos.addWidget(self.valor_card_2019_proventos)

        card_2020_proventos = QFrame()
        card_2020_proventos.setObjectName("cards_secundarios")
        layout_card_2020_proventos = QVBoxLayout(card_2020_proventos)
        layout_card_2020_proventos.setContentsMargins(0, 0, 0, 0)
        layout_card_2020_proventos.setSpacing(10)
        layout_area_valores_card_proventos.addWidget(card_2020_proventos, 0, 2)

        titulo_card_2020_proventos = QLabel("2020")
        titulo_card_2020_proventos.setObjectName("titulos_cards_secundarios")
        layout_card_2020_proventos.addWidget(titulo_card_2020_proventos)

        self.valor_card_2020_proventos = QLabel()
        self.valor_card_2020_proventos.setObjectName("valores_cards_secundarios")
        layout_card_2020_proventos.addWidget(self.valor_card_2020_proventos)

        card_2021_proventos = QFrame()
        card_2021_proventos.setObjectName("cards_secundarios")
        layout_card_2021_proventos = QVBoxLayout(card_2021_proventos)
        layout_card_2021_proventos.setContentsMargins(0, 0, 0, 0)
        layout_card_2021_proventos.setSpacing(10)
        layout_area_valores_card_proventos.addWidget(card_2021_proventos, 1, 0)

        titulo_card_2021_proventos = QLabel("2021")
        titulo_card_2021_proventos.setObjectName("titulos_cards_secundarios")
        layout_card_2021_proventos.addWidget(titulo_card_2021_proventos)

        self.valor_card_2021_proventos = QLabel()
        self.valor_card_2021_proventos.setObjectName("valores_cards_secundarios")
        layout_card_2021_proventos.addWidget(self.valor_card_2021_proventos)

        card_2022_proventos = QFrame()
        card_2022_proventos.setObjectName("cards_secundarios")
        layout_card_2022_proventos = QVBoxLayout(card_2022_proventos)
        layout_card_2022_proventos.setContentsMargins(0, 0, 0, 0)
        layout_card_2022_proventos.setSpacing(10)
        layout_area_valores_card_proventos.addWidget(card_2022_proventos, 1, 1)

        titulo_card_2022_proventos = QLabel("2022")
        titulo_card_2022_proventos.setObjectName("titulos_cards_secundarios")
        layout_card_2022_proventos.addWidget(titulo_card_2022_proventos)

        self.valor_card_2022_proventos = QLabel()
        self.valor_card_2022_proventos.setObjectName("valores_cards_secundarios")
        layout_card_2022_proventos.addWidget(self.valor_card_2022_proventos)

        card_2023_proventos = QFrame()
        card_2023_proventos.setObjectName("cards_secundarios")
        layout_card_2023_proventos = QVBoxLayout(card_2023_proventos)
        layout_card_2023_proventos.setContentsMargins(0, 0, 0, 0)
        layout_card_2023_proventos.setSpacing(10)
        layout_area_valores_card_proventos.addWidget(card_2023_proventos, 1, 2)

        titulo_card_2023_proventos = QLabel("2023")
        titulo_card_2023_proventos.setObjectName("titulos_cards_secundarios")
        layout_card_2023_proventos.addWidget(titulo_card_2023_proventos)

        self.valor_card_2023_proventos = QLabel()
        self.valor_card_2023_proventos.setObjectName("valores_cards_secundarios")
        layout_card_2023_proventos.addWidget(self.valor_card_2023_proventos)

        card_2024_proventos = QFrame()
        card_2024_proventos.setObjectName("cards_secundarios")
        layout_card_2024_proventos = QVBoxLayout(card_2024_proventos)
        layout_card_2024_proventos.setContentsMargins(0, 0, 0, 0)
        layout_card_2024_proventos.setSpacing(10)
        layout_area_valores_card_proventos.addWidget(card_2024_proventos, 2, 0)

        titulo_card_2024_proventos = QLabel("2024")
        titulo_card_2024_proventos.setObjectName("titulos_cards_secundarios")
        layout_card_2024_proventos.addWidget(titulo_card_2024_proventos)

        self.valor_card_2024_proventos = QLabel()
        self.valor_card_2024_proventos.setObjectName("valores_cards_secundarios")
        layout_card_2024_proventos.addWidget(self.valor_card_2024_proventos)

        card_2025_proventos = QFrame()
        card_2025_proventos.setObjectName("cards_secundarios")
        layout_card_2025_proventos = QVBoxLayout(card_2025_proventos)
        layout_card_2025_proventos.setContentsMargins(0, 0, 0, 0)
        layout_card_2025_proventos.setSpacing(10)
        layout_area_valores_card_proventos.addWidget(card_2025_proventos, 2, 1)

        titulo_card_2025_proventos = QLabel("2025")
        titulo_card_2025_proventos.setObjectName("titulos_cards_secundarios")
        layout_card_2025_proventos.addWidget(titulo_card_2025_proventos)

        self.valor_card_2025_proventos = QLabel()
        self.valor_card_2025_proventos.setObjectName("valores_cards_secundarios")
        layout_card_2025_proventos.addWidget(self.valor_card_2025_proventos)

        card_2026_proventos = QFrame()
        card_2026_proventos.setObjectName("cards_secundarios")
        layout_card_2026_proventos = QVBoxLayout(card_2026_proventos)
        layout_card_2026_proventos.setContentsMargins(0, 0, 0, 0)
        layout_card_2026_proventos.setSpacing(10)
        layout_area_valores_card_proventos.addWidget(card_2026_proventos, 2, 2)

        titulo_card_2026_proventos = QLabel("2026")
        titulo_card_2026_proventos.setObjectName("titulos_cards_secundarios")
        layout_card_2026_proventos.addWidget(titulo_card_2026_proventos)

        self.valor_card_2026_proventos = QLabel()
        self.valor_card_2026_proventos.setObjectName("valores_cards_secundarios")
        layout_card_2026_proventos.addWidget(self.valor_card_2026_proventos)

        self.carregar_dados_card_proventos()

        card_rentabilidades = QFrame()
        card_rentabilidades.setObjectName('cards')
        layout_card_rentabilidades = QVBoxLayout(card_rentabilidades)
        layout_card_rentabilidades.setContentsMargins(20, 20, 20, 20)
        layout_card_rentabilidades.setSpacing(60)
        layout_central.addWidget(card_rentabilidades)

        area_titulos_card_rentabilidades = QFrame()
        layout_area_titulos_card_rentabilidades = QVBoxLayout(area_titulos_card_rentabilidades)
        layout_area_titulos_card_rentabilidades.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_rentabilidades.setSpacing(5)
        layout_card_rentabilidades.addWidget(area_titulos_card_rentabilidades)

        titulo_card_rentabilidades = QLabel('Rentabilidades')
        titulo_card_rentabilidades.setObjectName('titulos_cards')
        layout_area_titulos_card_rentabilidades.addWidget(titulo_card_rentabilidades)

        subtitulo_card_rentabilidades = QLabel('Visão geral da rentabilidade acumulada e das rentabilidades ao longo dos anos.')
        subtitulo_card_rentabilidades.setObjectName('subtitulos_cards')
        layout_area_titulos_card_rentabilidades.addWidget(subtitulo_card_rentabilidades)

        area_valores_card_rentabilidades = QFrame()
        layout_area_valores_card_rentabilidades = QGridLayout(area_valores_card_rentabilidades)
        layout_area_valores_card_rentabilidades.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_rentabilidades.setSpacing(20)
        layout_card_rentabilidades.addWidget(area_valores_card_rentabilidades)

        card_rentabilidade_total = QFrame()
        card_rentabilidade_total.setObjectName("cards_secundarios")
        layout_card_rentabilidade_total = QVBoxLayout(card_rentabilidade_total)
        layout_card_rentabilidade_total.setContentsMargins(0, 0, 0, 0)
        layout_card_rentabilidade_total.setSpacing(10)
        layout_area_valores_card_rentabilidades.addWidget(card_rentabilidade_total, 0, 0)

        titulo_card_rentabilidade_total = QLabel("Rentabilidade total")
        titulo_card_rentabilidade_total.setObjectName("titulos_cards_secundarios")
        layout_card_rentabilidade_total.addWidget(titulo_card_rentabilidade_total)

        self.valor_card_rentabilidade_total = QLabel()
        self.valor_card_rentabilidade_total.setObjectName("valores_cards_secundarios")
        layout_card_rentabilidade_total.addWidget(self.valor_card_rentabilidade_total)

        card_2019_rentabilidades = QFrame()
        card_2019_rentabilidades.setObjectName("cards_secundarios")
        layout_card_2019_rentabilidades = QVBoxLayout(card_2019_rentabilidades)
        layout_card_2019_rentabilidades.setContentsMargins(0, 0, 0, 0)
        layout_card_2019_rentabilidades.setSpacing(10)
        layout_area_valores_card_rentabilidades.addWidget(card_2019_rentabilidades, 0, 1)

        titulo_card_2019_rentabilidades = QLabel("2019")
        titulo_card_2019_rentabilidades.setObjectName("titulos_cards_secundarios")
        layout_card_2019_rentabilidades.addWidget(titulo_card_2019_rentabilidades)

        self.valor_card_2019_rentabilidades = QLabel()
        self.valor_card_2019_rentabilidades.setObjectName("valores_cards_secundarios")
        layout_card_2019_rentabilidades.addWidget(self.valor_card_2019_rentabilidades)

        card_2020_rentabilidades = QFrame()
        card_2020_rentabilidades.setObjectName("cards_secundarios")
        layout_card_2020_rentabilidades = QVBoxLayout(card_2020_rentabilidades)
        layout_card_2020_rentabilidades.setContentsMargins(0, 0, 0, 0)
        layout_card_2020_rentabilidades.setSpacing(10)
        layout_area_valores_card_rentabilidades.addWidget(card_2020_rentabilidades, 0, 2)

        titulo_card_2020_rentabilidades = QLabel("2020")
        titulo_card_2020_rentabilidades.setObjectName("titulos_cards_secundarios")
        layout_card_2020_rentabilidades.addWidget(titulo_card_2020_rentabilidades)

        self.valor_card_2020_rentabilidades = QLabel()
        self.valor_card_2020_rentabilidades.setObjectName("valores_cards_secundarios")
        layout_card_2020_rentabilidades.addWidget(self.valor_card_2020_rentabilidades)

        card_2021_rentabilidades = QFrame()
        card_2021_rentabilidades.setObjectName("cards_secundarios")
        layout_card_2021_rentabilidades = QVBoxLayout(card_2021_rentabilidades)
        layout_card_2021_rentabilidades.setContentsMargins(0, 0, 0, 0)
        layout_card_2021_rentabilidades.setSpacing(10)
        layout_area_valores_card_rentabilidades.addWidget(card_2021_rentabilidades, 1, 0)

        titulo_card_2021_rentabilidades = QLabel("2021")
        titulo_card_2021_rentabilidades.setObjectName("titulos_cards_secundarios")
        layout_card_2021_rentabilidades.addWidget(titulo_card_2021_rentabilidades)

        self.valor_card_2021_rentabilidades = QLabel()
        self.valor_card_2021_rentabilidades.setObjectName("valores_cards_secundarios")
        layout_card_2021_rentabilidades.addWidget(self.valor_card_2021_rentabilidades)

        card_2022_rentabilidades = QFrame()
        card_2022_rentabilidades.setObjectName("cards_secundarios")
        layout_card_2022_rentabilidades = QVBoxLayout(card_2022_rentabilidades)
        layout_card_2022_rentabilidades.setContentsMargins(0, 0, 0, 0)
        layout_card_2022_rentabilidades.setSpacing(10)
        layout_area_valores_card_rentabilidades.addWidget(card_2022_rentabilidades, 1, 1)

        titulo_card_2022_rentabilidades = QLabel("2022")
        titulo_card_2022_rentabilidades.setObjectName("titulos_cards_secundarios")
        layout_card_2022_rentabilidades.addWidget(titulo_card_2022_rentabilidades)

        self.valor_card_2022_rentabilidades = QLabel()
        self.valor_card_2022_rentabilidades.setObjectName("valores_cards_secundarios")
        layout_card_2022_rentabilidades.addWidget(self.valor_card_2022_rentabilidades)

        card_2023_rentabilidades = QFrame()
        card_2023_rentabilidades.setObjectName("cards_secundarios")
        layout_card_2023_rentabilidades = QVBoxLayout(card_2023_rentabilidades)
        layout_card_2023_rentabilidades.setContentsMargins(0, 0, 0, 0)
        layout_card_2023_rentabilidades.setSpacing(10)
        layout_area_valores_card_rentabilidades.addWidget(card_2023_rentabilidades, 1, 2)

        titulo_card_2023_rentabilidades = QLabel("2023")
        titulo_card_2023_rentabilidades.setObjectName("titulos_cards_secundarios")
        layout_card_2023_rentabilidades.addWidget(titulo_card_2023_rentabilidades)

        self.valor_card_2023_rentabilidades = QLabel()
        self.valor_card_2023_rentabilidades.setObjectName("valores_cards_secundarios")
        layout_card_2023_rentabilidades.addWidget(self.valor_card_2023_rentabilidades)

        card_2024_rentabilidades = QFrame()
        card_2024_rentabilidades.setObjectName("cards_secundarios")
        layout_card_2024_rentabilidades = QVBoxLayout(card_2024_rentabilidades)
        layout_card_2024_rentabilidades.setContentsMargins(0, 0, 0, 0)
        layout_card_2024_rentabilidades.setSpacing(10)
        layout_area_valores_card_rentabilidades.addWidget(card_2024_rentabilidades, 2, 0)

        titulo_card_2024_rentabilidades = QLabel("2024")
        titulo_card_2024_rentabilidades.setObjectName("titulos_cards_secundarios")
        layout_card_2024_rentabilidades.addWidget(titulo_card_2024_rentabilidades)

        self.valor_card_2024_rentabilidades = QLabel()
        self.valor_card_2024_rentabilidades.setObjectName("valores_cards_secundarios")
        layout_card_2024_rentabilidades.addWidget(self.valor_card_2024_rentabilidades)

        card_2025_rentabilidades = QFrame()
        card_2025_rentabilidades.setObjectName("cards_secundarios")
        layout_card_2025_rentabilidades = QVBoxLayout(card_2025_rentabilidades)
        layout_card_2025_rentabilidades.setContentsMargins(0, 0, 0, 0)
        layout_card_2025_rentabilidades.setSpacing(10)
        layout_area_valores_card_rentabilidades.addWidget(card_2025_rentabilidades, 2, 1)

        titulo_card_2025_rentabilidades = QLabel("2025")
        titulo_card_2025_rentabilidades.setObjectName("titulos_cards_secundarios")
        layout_card_2025_rentabilidades.addWidget(titulo_card_2025_rentabilidades)

        self.valor_card_2025_rentabilidades = QLabel()
        self.valor_card_2025_rentabilidades.setObjectName("valores_cards_secundarios")
        layout_card_2025_rentabilidades.addWidget(self.valor_card_2025_rentabilidades)

        card_2026_rentabilidades = QFrame()
        card_2026_rentabilidades.setObjectName("cards_secundarios")
        layout_card_2026_rentabilidades = QVBoxLayout(card_2026_rentabilidades)
        layout_card_2026_rentabilidades.setContentsMargins(0, 0, 0, 0)
        layout_card_2026_rentabilidades.setSpacing(10)
        layout_area_valores_card_rentabilidades.addWidget(card_2026_rentabilidades, 2, 2)

        titulo_card_2026_rentabilidades = QLabel("2026")
        titulo_card_2026_rentabilidades.setObjectName("titulos_cards_secundarios")
        layout_card_2026_rentabilidades.addWidget(titulo_card_2026_rentabilidades)

        self.valor_card_2026_rentabilidades = QLabel()
        self.valor_card_2026_rentabilidades.setObjectName("valores_cards_secundarios")
        layout_card_2026_rentabilidades.addWidget(self.valor_card_2026_rentabilidades)

        self.carregar_dados_card_rentabilidades()

        card_stocks = QFrame()
        card_stocks.setObjectName('cards')
        layout_card_stocks = QVBoxLayout(card_stocks)
        layout_card_stocks.setContentsMargins(20, 20, 20, 20)
        layout_card_stocks.setSpacing(20)
        layout_central.addWidget(card_stocks)

        area_titulos_botao_card_stocks = QFrame()
        layout_area_titulos_botao_card_stocks = QHBoxLayout(area_titulos_botao_card_stocks)
        layout_area_titulos_botao_card_stocks.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_botao_card_stocks.setSpacing(5)
        layout_card_stocks.addWidget(area_titulos_botao_card_stocks)

        area_titulos_card_stocks = QFrame()
        layout_area_titulos_card_stocks = QVBoxLayout(area_titulos_card_stocks)
        layout_area_titulos_card_stocks.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_stocks.setSpacing(0)
        layout_area_titulos_botao_card_stocks.addWidget(area_titulos_card_stocks)

        titulo_card_stocks = QLabel('Stocks')
        titulo_card_stocks.setObjectName('titulos_cards')
        layout_area_titulos_card_stocks.addWidget(titulo_card_stocks)

        subtitulo_card_stocks = QLabel('Visão geral do total em stocks, do total aportado e da variação.')
        subtitulo_card_stocks.setObjectName('subtitulos_cards')
        layout_area_titulos_card_stocks.addWidget(subtitulo_card_stocks)

        self.botao_ver_stocks = QPushButton("Ver Stocks")
        self.botao_ver_stocks.setObjectName("botoes_ver_ativos")
        self.botao_ver_stocks.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_ver_stocks.setCheckable(True)
        self.botao_ver_stocks.clicked.connect(lambda: self.ver_cards(self.container_cards_stocks, self.botao_ver_stocks, "Stocks"))
        layout_area_titulos_botao_card_stocks.addWidget(self.botao_ver_stocks)

        area_valores_card_stocks = QFrame()
        layout_area_valores_card_stocks = QGridLayout(area_valores_card_stocks)
        layout_area_valores_card_stocks.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_stocks.setSpacing(20)
        layout_card_stocks.addWidget(area_valores_card_stocks)

        card_total_stocks = QFrame()
        card_total_stocks.setObjectName("cards_secundarios")
        layout_card_total_stocks = QVBoxLayout(card_total_stocks)
        layout_card_total_stocks.setContentsMargins(0, 0, 0, 0)
        layout_card_total_stocks.setSpacing(10)
        layout_area_valores_card_stocks.addWidget(card_total_stocks, 0, 0)

        titulo_card_total_stocks = QLabel("Total em stocks")
        titulo_card_total_stocks.setObjectName("titulos_cards_secundarios")
        layout_card_total_stocks.addWidget(titulo_card_total_stocks)

        self.valor_card_total_stocks = QLabel()
        self.valor_card_total_stocks.setObjectName("valores_cards_secundarios")
        layout_card_total_stocks.addWidget(self.valor_card_total_stocks)

        card_aporte_total_stocks = QFrame()
        card_aporte_total_stocks.setObjectName("cards_secundarios")
        layout_card_aporte_total_stocks = QVBoxLayout(card_aporte_total_stocks)
        layout_card_aporte_total_stocks.setContentsMargins(0, 0, 0, 0)
        layout_card_aporte_total_stocks.setSpacing(10)
        layout_area_valores_card_stocks.addWidget(card_aporte_total_stocks, 0, 1)

        titulo_card_aporte_total_stocks = QLabel("Aporte total")
        titulo_card_aporte_total_stocks.setObjectName("titulos_cards_secundarios")
        layout_card_aporte_total_stocks.addWidget(titulo_card_aporte_total_stocks)

        self.valor_card_aporte_total_stocks = QLabel()
        self.valor_card_aporte_total_stocks.setObjectName("valores_cards_secundarios")
        layout_card_aporte_total_stocks.addWidget(self.valor_card_aporte_total_stocks)

        card_variacao_stocks = QFrame()
        card_variacao_stocks.setObjectName("cards_secundarios")
        layout_card_variacao_stocks = QVBoxLayout(card_variacao_stocks)
        layout_card_variacao_stocks.setContentsMargins(0, 0, 0, 0)
        layout_card_variacao_stocks.setSpacing(10)
        layout_area_valores_card_stocks.addWidget(card_variacao_stocks, 0, 2)

        titulo_card_variacao_stocks = QLabel("Variação")
        titulo_card_variacao_stocks.setObjectName("titulos_cards_secundarios")
        layout_card_variacao_stocks.addWidget(titulo_card_variacao_stocks)

        self.valor_card_variacao_stocks = QLabel()
        self.valor_card_variacao_stocks.setObjectName("valores_cards_secundarios")
        layout_card_variacao_stocks.addWidget(self.valor_card_variacao_stocks)

        self.carregar_dados_card_stocks()

        self.container_cards_stocks = QFrame()
        self.container_cards_stocks.setObjectName("container_cards_ativos")
        layout_container_cards_stocks = QVBoxLayout(self.container_cards_stocks)
        layout_container_cards_stocks.setContentsMargins(0, 0, 0, 0)
        layout_container_cards_stocks.setSpacing(25)
        self.container_cards_stocks.setVisible(False)
        layout_card_stocks.addWidget(self.container_cards_stocks)

        self.carregar_cards_individuais_stocks()

        card_reits = QFrame()
        card_reits.setObjectName('cards')
        layout_card_reits = QVBoxLayout(card_reits)
        layout_card_reits.setContentsMargins(20, 20, 20, 20)
        layout_card_reits.setSpacing(20)
        layout_central.addWidget(card_reits)

        area_titulos_botao_card_reits = QFrame()
        layout_area_titulos_botao_card_reits = QHBoxLayout(area_titulos_botao_card_reits)
        layout_area_titulos_botao_card_reits.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_botao_card_reits.setSpacing(5)
        layout_card_reits.addWidget(area_titulos_botao_card_reits)

        area_titulos_card_reits = QFrame()
        layout_area_titulos_card_reits = QVBoxLayout(area_titulos_card_reits)
        layout_area_titulos_card_reits.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_reits.setSpacing(0)
        layout_area_titulos_botao_card_reits.addWidget(area_titulos_card_reits)

        titulo_card_reits = QLabel('Reits')
        titulo_card_reits.setObjectName('titulos_cards')
        layout_area_titulos_card_reits.addWidget(titulo_card_reits)

        subtitulo_card_reits = QLabel('Visão geral do total em reits, do total aportado e da variação.')
        subtitulo_card_reits.setObjectName('subtitulos_cards')
        layout_area_titulos_card_reits.addWidget(subtitulo_card_reits)

        self.botao_ver_reits = QPushButton("Ver reits")
        self.botao_ver_reits.setObjectName("botoes_ver_ativos")
        self.botao_ver_reits.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_ver_reits.setCheckable(True)
        self.botao_ver_reits.clicked.connect(lambda: self.ver_cards(self.container_cards_reits, self.botao_ver_reits, "Reits"))
        layout_area_titulos_botao_card_reits.addWidget(self.botao_ver_reits)

        area_valores_card_reits = QFrame()
        layout_area_valores_card_reits = QGridLayout(area_valores_card_reits)
        layout_area_valores_card_reits.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_reits.setSpacing(20)
        layout_card_reits.addWidget(area_valores_card_reits)

        card_total_reits = QFrame()
        card_total_reits.setObjectName("cards_secundarios")
        layout_card_total_reits = QVBoxLayout(card_total_reits)
        layout_card_total_reits.setContentsMargins(0, 0, 0, 0)
        layout_card_total_reits.setSpacing(10)
        layout_area_valores_card_reits.addWidget(card_total_reits, 0, 0)

        titulo_card_total_reits = QLabel("Total em reits")
        titulo_card_total_reits.setObjectName("titulos_cards_secundarios")
        layout_card_total_reits.addWidget(titulo_card_total_reits)

        self.valor_card_total_reits = QLabel()
        self.valor_card_total_reits.setObjectName("valores_cards_secundarios")
        layout_card_total_reits.addWidget(self.valor_card_total_reits)

        card_aporte_total_reits = QFrame()
        card_aporte_total_reits.setObjectName("cards_secundarios")
        layout_card_aporte_total_reits = QVBoxLayout(card_aporte_total_reits)
        layout_card_aporte_total_reits.setContentsMargins(0, 0, 0, 0)
        layout_card_aporte_total_reits.setSpacing(10)
        layout_area_valores_card_reits.addWidget(card_aporte_total_reits, 0, 1)

        titulo_card_aporte_total_reits = QLabel("Aporte total")
        titulo_card_aporte_total_reits.setObjectName("titulos_cards_secundarios")
        layout_card_aporte_total_reits.addWidget(titulo_card_aporte_total_reits)

        self.valor_card_aporte_total_reits = QLabel()
        self.valor_card_aporte_total_reits.setObjectName("valores_cards_secundarios")
        layout_card_aporte_total_reits.addWidget(self.valor_card_aporte_total_reits)

        card_variacao_reits = QFrame()
        card_variacao_reits.setObjectName("cards_secundarios")
        layout_card_variacao_reits = QVBoxLayout(card_variacao_reits)
        layout_card_variacao_reits.setContentsMargins(0, 0, 0, 0)
        layout_card_variacao_reits.setSpacing(10)
        layout_area_valores_card_reits.addWidget(card_variacao_reits, 0, 2)

        titulo_card_variacao_reits = QLabel("Variação")
        titulo_card_variacao_reits.setObjectName("titulos_cards_secundarios")
        layout_card_variacao_reits.addWidget(titulo_card_variacao_reits)

        self.valor_card_variacao_reits = QLabel()
        self.valor_card_variacao_reits.setObjectName("valores_cards_secundarios")
        layout_card_variacao_reits.addWidget(self.valor_card_variacao_reits)

        self.carregar_dados_card_reits()

        self.container_cards_reits = QFrame()
        self.container_cards_reits.setObjectName("container_cards_ativos")
        layout_container_cards_reits = QVBoxLayout(self.container_cards_reits)
        layout_container_cards_reits.setContentsMargins(0, 0, 0, 0)
        layout_container_cards_reits.setSpacing(25)
        self.container_cards_reits.setVisible(False)
        layout_card_reits.addWidget(self.container_cards_reits)

        self.carregar_cards_individuais_reits()

        card_acoes = QFrame()
        card_acoes.setObjectName('cards')
        layout_card_acoes = QVBoxLayout(card_acoes)
        layout_card_acoes.setContentsMargins(20, 20, 20, 20)
        layout_card_acoes.setSpacing(20)
        layout_central.addWidget(card_acoes)

        area_titulos_botao_card_acoes = QFrame()
        layout_area_titulos_botao_card_acoes = QHBoxLayout(area_titulos_botao_card_acoes)
        layout_area_titulos_botao_card_acoes.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_botao_card_acoes.setSpacing(5)
        layout_card_acoes.addWidget(area_titulos_botao_card_acoes)

        area_titulos_card_acoes = QFrame()
        layout_area_titulos_card_acoes = QVBoxLayout(area_titulos_card_acoes)
        layout_area_titulos_card_acoes.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_acoes.setSpacing(0)
        layout_area_titulos_botao_card_acoes.addWidget(area_titulos_card_acoes)

        titulo_card_acoes = QLabel('Ações')
        titulo_card_acoes.setObjectName('titulos_cards')
        layout_area_titulos_card_acoes.addWidget(titulo_card_acoes)

        subtitulo_card_acoes = QLabel('Visão geral do total em ações, do total aportado e da variação.')
        subtitulo_card_acoes.setObjectName('subtitulos_cards')
        layout_area_titulos_card_acoes.addWidget(subtitulo_card_acoes)

        self.botao_ver_acoes = QPushButton("Ver ações")
        self.botao_ver_acoes.setObjectName("botoes_ver_ativos")
        self.botao_ver_acoes.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_ver_acoes.setCheckable(True)
        self.botao_ver_acoes.clicked.connect(lambda: self.ver_cards(self.container_cards_acoes, self.botao_ver_acoes, "Ações"))
        layout_area_titulos_botao_card_acoes.addWidget(self.botao_ver_acoes)

        area_valores_card_acoes = QFrame()
        layout_area_valores_card_acoes = QGridLayout(area_valores_card_acoes)
        layout_area_valores_card_acoes.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_acoes.setSpacing(20)
        layout_card_acoes.addWidget(area_valores_card_acoes)

        card_total_acoes = QFrame()
        card_total_acoes.setObjectName("cards_secundarios")
        layout_card_total_acoes = QVBoxLayout(card_total_acoes)
        layout_card_total_acoes.setContentsMargins(0, 0, 0, 0)
        layout_card_total_acoes.setSpacing(10)
        layout_area_valores_card_acoes.addWidget(card_total_acoes, 0, 0)

        titulo_card_total_acoes = QLabel("Total em ações")
        titulo_card_total_acoes.setObjectName("titulos_cards_secundarios")
        layout_card_total_acoes.addWidget(titulo_card_total_acoes)

        self.valor_card_total_acoes = QLabel()
        self.valor_card_total_acoes.setObjectName("valores_cards_secundarios")
        layout_card_total_acoes.addWidget(self.valor_card_total_acoes)

        card_aporte_total_acoes = QFrame()
        card_aporte_total_acoes.setObjectName("cards_secundarios")
        layout_card_aporte_total_acoes = QVBoxLayout(card_aporte_total_acoes)
        layout_card_aporte_total_acoes.setContentsMargins(0, 0, 0, 0)
        layout_card_aporte_total_acoes.setSpacing(10)
        layout_area_valores_card_acoes.addWidget(card_aporte_total_acoes, 0, 1)

        titulo_card_aporte_total_acoes = QLabel("Aporte total")
        titulo_card_aporte_total_acoes.setObjectName("titulos_cards_secundarios")
        layout_card_aporte_total_acoes.addWidget(titulo_card_aporte_total_acoes)

        self.valor_card_aporte_total_acoes = QLabel()
        self.valor_card_aporte_total_acoes.setObjectName("valores_cards_secundarios")
        layout_card_aporte_total_acoes.addWidget(self.valor_card_aporte_total_acoes)

        card_variacao_acoes = QFrame()
        card_variacao_acoes.setObjectName("cards_secundarios")
        layout_card_variacao_acoes = QVBoxLayout(card_variacao_acoes)
        layout_card_variacao_acoes.setContentsMargins(0, 0, 0, 0)
        layout_card_variacao_acoes.setSpacing(10)
        layout_area_valores_card_acoes.addWidget(card_variacao_acoes, 0, 2)

        titulo_card_variacao_acoes = QLabel("Variação")
        titulo_card_variacao_acoes.setObjectName("titulos_cards_secundarios")
        layout_card_variacao_acoes.addWidget(titulo_card_variacao_acoes)

        self.valor_card_variacao_acoes = QLabel()
        self.valor_card_variacao_acoes.setObjectName("valores_cards_secundarios")
        layout_card_variacao_acoes.addWidget(self.valor_card_variacao_acoes)

        self.carregar_dados_card_acoes()

        self.container_cards_acoes = QFrame()
        self.container_cards_acoes.setObjectName("container_cards_ativos")
        layout_container_cards_acoes = QVBoxLayout(self.container_cards_acoes)
        layout_container_cards_acoes.setContentsMargins(0, 0, 0, 0)
        layout_container_cards_acoes.setSpacing(25)
        self.container_cards_acoes.setVisible(False)
        layout_card_acoes.addWidget(self.container_cards_acoes)

        self.carregar_cards_individuais_acoes()

        card_fiis = QFrame()
        card_fiis.setObjectName('cards')
        layout_card_fiis = QVBoxLayout(card_fiis)
        layout_card_fiis.setContentsMargins(20, 20, 20, 20)
        layout_card_fiis.setSpacing(20)
        layout_central.addWidget(card_fiis)

        area_titulos_botao_card_fiis = QFrame()
        layout_area_titulos_botao_card_fiis = QHBoxLayout(area_titulos_botao_card_fiis)
        layout_area_titulos_botao_card_fiis.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_botao_card_fiis.setSpacing(5)
        layout_card_fiis.addWidget(area_titulos_botao_card_fiis)

        area_titulos_card_fiis = QFrame()
        layout_area_titulos_card_fiis = QVBoxLayout(area_titulos_card_fiis)
        layout_area_titulos_card_fiis.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_fiis.setSpacing(0)
        layout_area_titulos_botao_card_fiis.addWidget(area_titulos_card_fiis)

        titulo_card_fiis = QLabel('Fiis')
        titulo_card_fiis.setObjectName('titulos_cards')
        layout_area_titulos_card_fiis.addWidget(titulo_card_fiis)

        subtitulo_card_fiis = QLabel('Visão geral do total em fiis, do total aportado e da variação.')
        subtitulo_card_fiis.setObjectName('subtitulos_cards')
        layout_area_titulos_card_fiis.addWidget(subtitulo_card_fiis)

        self.botao_ver_fiis = QPushButton("Ver fiis")
        self.botao_ver_fiis.setObjectName("botoes_ver_ativos")
        self.botao_ver_fiis.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_ver_fiis.setCheckable(True)
        self.botao_ver_fiis.clicked.connect(lambda: self.ver_cards(self.container_cards_fiis, self.botao_ver_fiis, "Fiis"))
        layout_area_titulos_botao_card_fiis.addWidget(self.botao_ver_fiis)

        area_valores_card_fiis = QFrame()
        layout_area_valores_card_fiis = QGridLayout(area_valores_card_fiis)
        layout_area_valores_card_fiis.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_fiis.setSpacing(20)
        layout_card_fiis.addWidget(area_valores_card_fiis)

        card_total_fiis = QFrame()
        card_total_fiis.setObjectName("cards_secundarios")
        layout_card_total_fiis = QVBoxLayout(card_total_fiis)
        layout_card_total_fiis.setContentsMargins(0, 0, 0, 0)
        layout_card_total_fiis.setSpacing(10)
        layout_area_valores_card_fiis.addWidget(card_total_fiis, 0, 0)

        titulo_card_total_fiis = QLabel("Total em fiis")
        titulo_card_total_fiis.setObjectName("titulos_cards_secundarios")
        layout_card_total_fiis.addWidget(titulo_card_total_fiis)

        self.valor_card_total_fiis = QLabel()
        self.valor_card_total_fiis.setObjectName("valores_cards_secundarios")
        layout_card_total_fiis.addWidget(self.valor_card_total_fiis)

        card_aporte_total_fiis = QFrame()
        card_aporte_total_fiis.setObjectName("cards_secundarios")
        layout_card_aporte_total_fiis = QVBoxLayout(card_aporte_total_fiis)
        layout_card_aporte_total_fiis.setContentsMargins(0, 0, 0, 0)
        layout_card_aporte_total_fiis.setSpacing(10)
        layout_area_valores_card_fiis.addWidget(card_aporte_total_fiis, 0, 1)

        titulo_card_aporte_total_fiis = QLabel("Aporte total")
        titulo_card_aporte_total_fiis.setObjectName("titulos_cards_secundarios")
        layout_card_aporte_total_fiis.addWidget(titulo_card_aporte_total_fiis)

        self.valor_card_aporte_total_fiis = QLabel()
        self.valor_card_aporte_total_fiis.setObjectName("valores_cards_secundarios")
        layout_card_aporte_total_fiis.addWidget(self.valor_card_aporte_total_fiis)

        card_variacao_fiis = QFrame()
        card_variacao_fiis.setObjectName("cards_secundarios")
        layout_card_variacao_fiis = QVBoxLayout(card_variacao_fiis)
        layout_card_variacao_fiis.setContentsMargins(0, 0, 0, 0)
        layout_card_variacao_fiis.setSpacing(10)
        layout_area_valores_card_fiis.addWidget(card_variacao_fiis, 0, 2)

        titulo_card_variacao_fiis = QLabel("Variação")
        titulo_card_variacao_fiis.setObjectName("titulos_cards_secundarios")
        layout_card_variacao_fiis.addWidget(titulo_card_variacao_fiis)

        self.valor_card_variacao_fiis = QLabel()
        self.valor_card_variacao_fiis.setObjectName("valores_cards_secundarios")
        layout_card_variacao_fiis.addWidget(self.valor_card_variacao_fiis)

        self.carregar_dados_card_fiis()

        self.container_cards_fiis = QFrame()
        self.container_cards_fiis.setObjectName("container_cards_ativos")
        layout_container_cards_fiis = QVBoxLayout(self.container_cards_fiis)
        layout_container_cards_fiis.setContentsMargins(0, 0, 0, 0)
        layout_container_cards_fiis.setSpacing(25)
        self.container_cards_fiis.setVisible(False)
        layout_card_fiis.addWidget(self.container_cards_fiis)

        self.carregar_cards_individuais_fiis()

        card_criptos = QFrame()
        card_criptos.setObjectName('cards')
        layout_card_criptos = QVBoxLayout(card_criptos)
        layout_card_criptos.setContentsMargins(20, 20, 20, 20)
        layout_card_criptos.setSpacing(20)
        layout_central.addWidget(card_criptos)

        area_titulos_botao_card_criptos = QFrame()
        layout_area_titulos_botao_card_criptos = QHBoxLayout(area_titulos_botao_card_criptos)
        layout_area_titulos_botao_card_criptos.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_botao_card_criptos.setSpacing(5)
        layout_card_criptos.addWidget(area_titulos_botao_card_criptos)

        area_titulos_card_criptos = QFrame()
        layout_area_titulos_card_criptos = QVBoxLayout(area_titulos_card_criptos)
        layout_area_titulos_card_criptos.setContentsMargins(0, 0, 0, 0)
        layout_area_titulos_card_criptos.setSpacing(0)
        layout_area_titulos_botao_card_criptos.addWidget(area_titulos_card_criptos)

        titulo_card_criptos = QLabel('Criptos')
        titulo_card_criptos.setObjectName('titulos_cards')
        layout_area_titulos_card_criptos.addWidget(titulo_card_criptos)

        subtitulo_card_criptos = QLabel('Visão geral do total em criptos, do total aportado e da variação.')
        subtitulo_card_criptos.setObjectName('subtitulos_cards')
        layout_area_titulos_card_criptos.addWidget(subtitulo_card_criptos)

        self.botao_ver_criptos = QPushButton("Ver criptos")
        self.botao_ver_criptos.setObjectName("botoes_ver_ativos")
        self.botao_ver_criptos.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_ver_criptos.setCheckable(True)
        self.botao_ver_criptos.clicked.connect(lambda: self.ver_cards(self.container_cards_criptos, self.botao_ver_criptos, "Criptos"))
        layout_area_titulos_botao_card_criptos.addWidget(self.botao_ver_criptos)

        area_valores_card_criptos = QFrame()
        layout_area_valores_card_criptos = QGridLayout(area_valores_card_criptos)
        layout_area_valores_card_criptos.setContentsMargins(0, 0, 0, 0)
        layout_area_valores_card_criptos.setSpacing(20)
        layout_card_criptos.addWidget(area_valores_card_criptos)

        card_total_criptos = QFrame()
        card_total_criptos.setObjectName("cards_secundarios")
        layout_card_total_criptos = QVBoxLayout(card_total_criptos)
        layout_card_total_criptos.setContentsMargins(0, 0, 0, 0)
        layout_card_total_criptos.setSpacing(10)
        layout_area_valores_card_criptos.addWidget(card_total_criptos, 0, 0)

        titulo_card_total_criptos = QLabel("Total em criptos")
        titulo_card_total_criptos.setObjectName("titulos_cards_secundarios")
        layout_card_total_criptos.addWidget(titulo_card_total_criptos)

        self.valor_card_total_criptos = QLabel()
        self.valor_card_total_criptos.setObjectName("valores_cards_secundarios")
        layout_card_total_criptos.addWidget(self.valor_card_total_criptos)

        card_aporte_total_criptos = QFrame()
        card_aporte_total_criptos.setObjectName("cards_secundarios")
        layout_card_aporte_total_criptos = QVBoxLayout(card_aporte_total_criptos)
        layout_card_aporte_total_criptos.setContentsMargins(0, 0, 0, 0)
        layout_card_aporte_total_criptos.setSpacing(10)
        layout_area_valores_card_criptos.addWidget(card_aporte_total_criptos, 0, 1)

        titulo_card_aporte_total_criptos = QLabel("Aporte total")
        titulo_card_aporte_total_criptos.setObjectName("titulos_cards_secundarios")
        layout_card_aporte_total_criptos.addWidget(titulo_card_aporte_total_criptos)

        self.valor_card_aporte_total_criptos = QLabel()
        self.valor_card_aporte_total_criptos.setObjectName("valores_cards_secundarios")
        layout_card_aporte_total_criptos.addWidget(self.valor_card_aporte_total_criptos)

        card_variacao_criptos = QFrame()
        card_variacao_criptos.setObjectName("cards_secundarios")
        layout_card_variacao_criptos = QVBoxLayout(card_variacao_criptos)
        layout_card_variacao_criptos.setContentsMargins(0, 0, 0, 0)
        layout_card_variacao_criptos.setSpacing(10)
        layout_area_valores_card_criptos.addWidget(card_variacao_criptos, 0, 2)

        titulo_card_variacao_criptos = QLabel("Variação")
        titulo_card_variacao_criptos.setObjectName("titulos_cards_secundarios")
        layout_card_variacao_criptos.addWidget(titulo_card_variacao_criptos)

        self.valor_card_variacao_criptos = QLabel()
        self.valor_card_variacao_criptos.setObjectName("valores_cards_secundarios")
        layout_card_variacao_criptos.addWidget(self.valor_card_variacao_criptos)

        self.carregar_dados_card_criptos()

        self.container_cards_criptos = QFrame()
        self.container_cards_criptos.setObjectName("container_cards_ativos")
        layout_container_cards_criptos = QVBoxLayout(self.container_cards_criptos)
        layout_container_cards_criptos.setContentsMargins(0, 0, 0, 0)
        layout_container_cards_criptos.setSpacing(25)
        self.container_cards_criptos.setVisible(False)
        layout_card_criptos.addWidget(self.container_cards_criptos)

        self.carregar_cards_individuais_criptos()

        layout_central.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
    def aplicar_estilo(self, arquivo_css):
        with open(arquivo_css, "r", encoding="utf-8") as file:
            self.setStyleSheet(file.read())

    def formatar_brl(self, valor):
        import locale
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        negativo = valor < 0
        valor_abs = abs(valor)
        texto = locale.currency(valor_abs, grouping=True)
        return f"-{texto}" if negativo else texto

    def formatar_usd(self, valor):
        import locale
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        negativo = valor < 0
        valor_abs = abs(valor)
        texto = locale.currency(valor_abs, grouping=True)
        return f"-{texto}" if negativo else texto

    def carregar_dados_card_patrimonio(self):
        total_patrimonio = float(self.totais["total_patrimonio"].iloc[0].replace(",", "."))
        total_aportado = float(self.totais["total_aportado"].iloc[0].replace(",", "."))
        total_diferenca_patrimonio = float(self.totais["total_diferenca_patrimonio"].iloc[0].replace(",", "."))

        self.valor_card_patrimonio_atual.setText(self.formatar_brl(total_patrimonio))
        self.valor_card_aporte_total_patrimonio.setText(self.formatar_brl(total_aportado))
        sinal = "+" if total_diferenca_patrimonio > 0 else ""
        self.valor_card_variacao_patrimonio.setText(f"{sinal}{self.formatar_brl(total_diferenca_patrimonio)}")
        cor_variacao = "#60b59b" if total_diferenca_patrimonio > 0 else "#e895a4" if total_diferenca_patrimonio < 0 else "#f5f5f7"
        self.valor_card_variacao_patrimonio.setStyleSheet(f"color: {cor_variacao};")

    def carregar_dados_card_reservas(self):
        total_reservas = float(self.totais["total_reservas"].iloc[0].replace(",", "."))
        saldo_conta_corrente = float(self.reservas["saldo_atual"].iloc[0].replace(",", "."))
        saldo_reserva_emergencia = float(self.reservas["saldo_atual"].iloc[1].replace(",", "."))

        self.valor_card_reservas_totais.setText(self.formatar_brl(total_reservas))
        self.valor_card_conta_corrente.setText(self.formatar_brl(saldo_conta_corrente))
        self.valor_card_reserva_emergencia.setText(self.formatar_brl(saldo_reserva_emergencia))

    def carregar_dados_card_investimentos(self):
        total_investimentos = float(self.totais["total_investimentos"].iloc[0].replace(",", "."))
        total_aportado_investimentos = float(self.totais["total_aportado_investimentos"].iloc[0].replace(",", "."))
        total_diferenca_investimentos = float(self.totais["total_diferenca_investimentos"].iloc[0].replace(",", "."))

        self.valor_card_total_investimentos.setText(self.formatar_brl(total_investimentos))
        self.valor_card_total_aportado_investimentos.setText(self.formatar_brl(total_aportado_investimentos))
        sinal = "+" if total_diferenca_investimentos > 0 else ""
        self.valor_card_variacao_investimentos.setText(f"{sinal}{self.formatar_brl(total_diferenca_investimentos)}")
        cor_variacao = "#60b59b" if total_diferenca_investimentos > 0 else "#e895a4" if total_diferenca_investimentos < 0 else "#f5f5f7"
        self.valor_card_variacao_investimentos.setStyleSheet(f"color: {cor_variacao};")

    def carregar_dados_card_alocacao(self):
        alocacao_atual_stocks = float(self.alocacao["alocacao_atual_stocks"].iloc[0].replace(",", "."))
        alocacao_ideal_stocks = float(self.alocacao["alocacao_ideal_stocks"].iloc[0].replace(",", "."))
        alocacao_diferenca_stocks = float(self.alocacao["alocacao_diferenca_stocks"].iloc[0].replace(",", "."))

        alocacao_atual_reits = float(self.alocacao["alocacao_atual_reits"].iloc[0].replace(",", "."))
        alocacao_ideal_reits = float(self.alocacao["alocacao_ideal_reits"].iloc[0].replace(",", "."))
        alocacao_diferenca_reits = float(self.alocacao["alocacao_diferenca_reits"].iloc[0].replace(",", "."))

        alocacao_atual_acoes = float(self.alocacao["alocacao_atual_acoes"].iloc[0].replace(",", "."))
        alocacao_ideal_acoes = float(self.alocacao["alocacao_ideal_acoes"].iloc[0].replace(",", "."))
        alocacao_diferenca_acoes = float(self.alocacao["alocacao_diferenca_acoes"].iloc[0].replace(",", "."))

        alocacao_atual_fiis = float(self.alocacao["alocacao_atual_fiis"].iloc[0].replace(",", "."))
        alocacao_ideal_fiis = float(self.alocacao["alocacao_ideal_fiis"].iloc[0].replace(",", "."))
        alocacao_diferenca_fiis = float(self.alocacao["alocacao_diferenca_fiis"].iloc[0].replace(",", "."))

        alocacao_atual_criptos = float(self.alocacao["alocacao_atual_criptos"].iloc[0].replace(",", "."))
        alocacao_ideal_criptos = float(self.alocacao["alocacao_ideal_criptos"].iloc[0].replace(",", "."))
        alocacao_diferenca_criptos = float(self.alocacao["alocacao_diferenca_criptos"].iloc[0].replace(",", "."))

        self.valor_card_stocks_alocacao.setText(f"{alocacao_atual_stocks}%")
        self.valor_alocacao_ideal_stocks.setText(f"Ideal: {alocacao_ideal_stocks}%")
        sinal = "+" if alocacao_diferenca_stocks > 0 else ""
        self.valor_alocacao_diferenca_stocks.setText(f"Diferença: {sinal}{alocacao_diferenca_stocks}%")

        self.valor_card_reits_alocacao.setText(f"{alocacao_atual_reits}%")
        self.valor_alocacao_ideal_reits.setText(f"Ideal: {alocacao_ideal_reits}%")
        sinal = "+" if alocacao_diferenca_reits > 0 else ""
        self.valor_alocacao_diferenca_reits.setText(f"Diferença: {sinal}{alocacao_diferenca_reits}%")

        self.valor_card_acoes_alocacao.setText(f"{alocacao_atual_acoes}%")
        self.valor_alocacao_ideal_acoes.setText(f"Ideal: {alocacao_ideal_acoes}%")
        sinal = "+" if alocacao_diferenca_acoes > 0 else ""
        self.valor_alocacao_diferenca_acoes.setText(f"Diferença: {sinal}{alocacao_diferenca_acoes}%")

        self.valor_card_fiis_alocacao.setText(f"{alocacao_atual_fiis}%")
        self.valor_alocacao_ideal_fiis.setText(f"Ideal: {alocacao_ideal_fiis}%")
        sinal = "+" if alocacao_diferenca_fiis > 0 else ""
        self.valor_alocacao_diferenca_fiis.setText(f"Diferença: {sinal}{alocacao_diferenca_fiis}%")

        self.valor_card_criptos_alocacao.setText(f"{alocacao_atual_criptos}%")
        self.valor_alocacao_ideal_criptos.setText(f"Ideal: {alocacao_ideal_criptos}%")
        sinal = "+" if alocacao_diferenca_criptos > 0 else ""
        self.valor_alocacao_diferenca_criptos.setText(f"Diferença: {sinal}{alocacao_diferenca_criptos}%")

    def carregar_dados_card_aporte(self):
        MAPA_ALOCACAO = {
            "stock": ("alocacao_ideal_stocks", "alocacao_atual_stocks"),
            "reit": ("alocacao_ideal_reits", "alocacao_atual_reits"),
            "acao": ("alocacao_ideal_acoes", "alocacao_atual_acoes"),
            "fii": ("alocacao_ideal_fiis", "alocacao_atual_fiis"),
            "cripto": ("alocacao_ideal_criptos", "alocacao_atual_criptos"),
        }

        NOME_CLASSE_EXIBICAO = {
            "stock": "Stocks",
            "reit": "Reits",
            "acao": "Ações",
            "fii": "Fiis",
            "cripto": "Criptos",
        }

        alocacao = self.alocacao
        ativos = self.ativos

        classe_escolhida = None
        maior_defasagem = 0

        for classe, (col_ideal, col_atual) in MAPA_ALOCACAO.items():
            try:
                ideal = float(str(alocacao[col_ideal].iloc[0]).replace(",", "."))
                atual = float(str(alocacao[col_atual].iloc[0]).replace(",", "."))
            except Exception:
                continue

            defasagem = ideal - atual

            if defasagem > maior_defasagem:
                maior_defasagem = defasagem
                classe_escolhida = classe

        self.valor_card_classe_aporte.setText(NOME_CLASSE_EXIBICAO.get(classe_escolhida, "N/A"))

        texto_ticker = "N/A"

        if classe_escolhida and not ativos.empty:
            df = ativos.copy()

            df["classe"] = df["classe"].astype(str).str.lower().str.strip()
            df["porcentagem_atual"] = df["porcentagem_atual"].apply(lambda v: float(str(v).replace(",", ".")))

            df_filtrado = df[df["classe"] == classe_escolhida]

            if not df_filtrado.empty:
                df_zero = df_filtrado[df_filtrado["porcentagem_atual"] == 0]

                linha = (df_zero.iloc[0] if not df_zero.empty else df_filtrado.loc[df_filtrado["porcentagem_atual"].idxmin()])

                if "ticker" in linha:
                    texto_ticker = str(linha["ticker"])

        self.valor_card_ticker_aporte.setText(texto_ticker.upper())

    from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout

    def carregar_dados_card_proventos(self):
        total_recebido = float(
            self.proventos["total_recebido"].iloc[0].replace(",", ".")
        )
        self.valor_card_total_recebido_proventos.setText(
            self.formatar_brl(total_recebido)
        )

        labels_por_ano = {
            2019: self.valor_card_2019_proventos,
            2020: self.valor_card_2020_proventos,
            2021: self.valor_card_2021_proventos,
            2022: self.valor_card_2022_proventos,
            2023: self.valor_card_2023_proventos,
            2024: self.valor_card_2024_proventos,
            2025: self.valor_card_2025_proventos,
            2026: self.valor_card_2026_proventos,
        }

        for index, (ano, label) in enumerate(labels_por_ano.items()):
            valor = float(
                self.proventos["total_ano"].iloc[index].replace(",", ".")
            )
            label.setText(self.formatar_brl(valor))

    def carregar_dados_card_rentabilidades(self):

        def sinal_e_cor(valor):
            sinal = "+" if valor > 0 else ""
            cor = "#60b59b" if valor > 0 else "#e895a4" if valor < 0 else "#f5f5f7"
            return sinal, cor

        rentabilidade_total = float(
            self.rentabilidades["rentabilidade_total"].iloc[0].replace(",", ".")
        )

        sinal, cor = sinal_e_cor(rentabilidade_total)
        self.valor_card_rentabilidade_total.setText(f"{sinal}{rentabilidade_total}%")
        self.valor_card_rentabilidade_total.setStyleSheet(f"color: {cor};")

        labels_por_ano = {
            2019: self.valor_card_2019_rentabilidades,
            2020: self.valor_card_2020_rentabilidades,
            2021: self.valor_card_2021_rentabilidades,
            2022: self.valor_card_2022_rentabilidades,
            2023: self.valor_card_2023_rentabilidades,
            2024: self.valor_card_2024_rentabilidades,
            2025: self.valor_card_2025_rentabilidades,
            2026: self.valor_card_2026_rentabilidades,
        }

        for index, (ano, label) in enumerate(labels_por_ano.items()):
            valor = float(
                self.rentabilidades["total_ano"].iloc[index].replace(",", ".")
            )

            sinal, cor = sinal_e_cor(valor)
            label.setText(f"{sinal}{valor}%")
            label.setStyleSheet(f"color: {cor};")

    def carregar_dados_card_stocks(self):
        total_stocks = float(self.totais["total_stocks"].iloc[0].replace(",", "."))
        total_aportado_stocks = float(self.totais["total_aportado_stocks"].iloc[0].replace(",", "."))
        diferenca_stocks = float(self.totais["diferenca_stocks"].iloc[0].replace(",", "."))

        self.valor_card_total_stocks.setText(self.formatar_brl(total_stocks))
        self.valor_card_aporte_total_stocks.setText(self.formatar_brl(total_aportado_stocks))
        sinal = "+" if diferenca_stocks > 0 else ""
        self.valor_card_variacao_stocks.setText(f"{sinal}{self.formatar_brl(diferenca_stocks)}")
        cor_variacao = "#60b59b" if diferenca_stocks > 0 else "#e895a4" if diferenca_stocks < 0 else "#f5f5f7"
        self.valor_card_variacao_stocks.setStyleSheet(f"color: {cor_variacao};")

    def carregar_dados_card_reits(self):
        total_reits = float(self.totais["total_reits"].iloc[0].replace(",", "."))
        total_aportado_reits = float(self.totais["total_aportado_reits"].iloc[0].replace(",", "."))
        diferenca_reits = float(self.totais["diferenca_reits"].iloc[0].replace(",", "."))

        self.valor_card_total_reits.setText(self.formatar_brl(total_reits))
        self.valor_card_aporte_total_reits.setText(self.formatar_brl(total_aportado_reits))
        sinal = "+" if diferenca_reits > 0 else ""
        self.valor_card_variacao_reits.setText(f"{sinal}{self.formatar_brl(diferenca_reits)}")
        cor_variacao = "#60b59b" if diferenca_reits > 0 else "#e895a4" if diferenca_reits < 0 else "#f5f5f7"
        self.valor_card_variacao_reits.setStyleSheet(f"color: {cor_variacao};")

    def carregar_dados_card_acoes(self):
        total_acoes = float(self.totais["total_acoes"].iloc[0].replace(",", "."))
        total_aportado_acoes = float(self.totais["total_aportado_acoes"].iloc[0].replace(",", "."))
        diferenca_acoes = float(self.totais["diferenca_acoes"].iloc[0].replace(",", "."))

        self.valor_card_total_acoes.setText(self.formatar_brl(total_acoes))
        self.valor_card_aporte_total_acoes.setText(self.formatar_brl(total_aportado_acoes))
        sinal = "+" if diferenca_acoes > 0 else ""
        self.valor_card_variacao_acoes.setText(f"{sinal}{self.formatar_brl(diferenca_acoes)}")
        cor_variacao = "#60b59b" if diferenca_acoes > 0 else "#e895a4" if diferenca_acoes < 0 else "#f5f5f7"
        self.valor_card_variacao_acoes.setStyleSheet(f"color: {cor_variacao};")

    def carregar_dados_card_fiis(self):
        total_fiis = float(self.totais["total_fiis"].iloc[0].replace(",", "."))
        total_aportado_fiis = float(self.totais["total_aportado_fiis"].iloc[0].replace(",", "."))
        diferenca_fiis = float(self.totais["diferenca_fiis"].iloc[0].replace(",", "."))

        self.valor_card_total_fiis.setText(self.formatar_brl(total_fiis))
        self.valor_card_aporte_total_fiis.setText(self.formatar_brl(total_aportado_fiis))
        sinal = "+" if diferenca_fiis > 0 else ""
        self.valor_card_variacao_fiis.setText(f"{sinal}{self.formatar_brl(diferenca_fiis)}")
        cor_variacao = "#60b59b" if diferenca_fiis > 0 else "#e895a4" if diferenca_fiis < 0 else "#f5f5f7"
        self.valor_card_variacao_fiis.setStyleSheet(f"color: {cor_variacao};")

    def carregar_dados_card_criptos(self):
        total_criptos = float(self.totais["total_criptos"].iloc[0].replace(",", "."))
        total_aportado_criptos = float(self.totais["total_aportado_criptos"].iloc[0].replace(",", "."))
        diferenca_criptos = float(self.totais["diferenca_criptos"].iloc[0].replace(",", "."))

        self.valor_card_total_criptos.setText(self.formatar_brl(total_criptos))
        self.valor_card_aporte_total_criptos.setText(self.formatar_brl(total_aportado_criptos))
        sinal = "+" if diferenca_criptos > 0 else ""
        self.valor_card_variacao_criptos.setText(f"{sinal}{self.formatar_brl(diferenca_criptos)}")
        cor_variacao = "#60b59b" if diferenca_criptos > 0 else "#e895a4" if diferenca_criptos < 0 else "#f5f5f7"
        self.valor_card_variacao_criptos.setStyleSheet(f"color: {cor_variacao};")

    def ver_cards(self, container, botao, nome):
        is_visible = container.isVisible()
        container.setVisible(not is_visible)

        if not is_visible:
            botao.setText(f"Ocultar {nome}")
        else:
            botao.setText(f"Ver {nome}")

    def ver_cards_stocks(self):
        self.ver_cards(self.container_cards_stocks, self.botao_ver_stocks)

    def ver_cards_reits(self):
        self.ver_cards(self.container_cards_reits, self.botao_ver_reits)

    def ver_cards_acoes(self):
        self.ver_cards(self.container_cards_acoes, self.botao_ver_acoes)

    def ver_cards_fiis(self):
        self.ver_cards(self.container_cards_fiis, self.botao_ver_fiis)

    def ver_cards_criptos(self):
        self.ver_cards(self.container_cards_criptos, self.botao_ver_criptos)

    def criar_campo_card(self, titulo, valor, cor="#f5f5f7"):
        campo_frame = QFrame()
        campo_layout = QVBoxLayout(campo_frame)
        campo_layout.setContentsMargins(0, 0, 0, 0)
        campo_layout.setSpacing(2)
        
        titulo_label = QLabel(titulo)
        titulo_label.setObjectName("titulo_dados_ativos")
        campo_layout.addWidget(titulo_label)
        
        valor_label = QLabel(str(valor))
        valor_label.setObjectName("valor_dados_ativos")
        valor_label.setStyleSheet(f"color: {cor};")
        campo_layout.addWidget(valor_label)
        
        return campo_frame

    def criar_card_individual(self, ativo):
        card = QFrame()
        card.setObjectName("cards_secundarios")
        layout_card = QVBoxLayout(card)
        layout_card.setContentsMargins(20, 20, 20, 20)
        layout_card.setSpacing(10)
        
        header_frame = QFrame()
        layout_header = QHBoxLayout(header_frame)
        layout_header.setContentsMargins(0, 0, 0, 0)
        layout_header.setSpacing(15)
        layout_card.addWidget(header_frame)
        
        logo_label = QLabel()
        ticker_upper = str(ativo['ticker']).upper()
        logo_label.setPixmap(QPixmap(f"img_ativos/{ticker_upper}.png").scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        layout_header.addWidget(logo_label)
        
        info_container = QWidget()
        layout_info = QVBoxLayout(info_container)
        layout_info.setContentsMargins(0, 0, 0, 0)
        layout_info.setSpacing(5)
        
        ticker_label = QLabel(ticker_upper)
        ticker_label.setObjectName("titulos_cards")
        layout_info.addWidget(ticker_label)
        
        nome_label = QLabel(str(ativo['nome']))
        nome_label.setObjectName("nome_ativo")
        layout_info.addWidget(nome_label)
        
        layout_header.addWidget(info_container)
        layout_header.addStretch()
        
        linha = QFrame()
        linha.setFrameShape(QFrame.Shape.HLine)
        linha.setObjectName("divisor_card")
        layout_card.addWidget(linha)
        
        grid_valores = QGridLayout()
        grid_valores.setContentsMargins(0, 10, 0, 0)
        grid_valores.setHorizontalSpacing(20)
        grid_valores.setVerticalSpacing(15)
        
        cotacao = float(str(ativo['cotacao']).replace(",", "."))
        quantidade = float(str(ativo['quantidade']).replace(",", "."))
        preco_medio = float(str(ativo['preco_medio']).replace(",", "."))
        total_investido = float(str(ativo['total_investido']).replace(",", "."))
        total_atual = float(str(ativo['total_atual']).replace(",", "."))
        variacao_total = float(str(ativo['variacao_total']).replace(",", "."))
        porcentagem_meta = float(str(ativo['porcentagem_meta']).replace(",", "."))
        porcentagem_atual = float(str(ativo['porcentagem_atual']).replace(",", "."))
        
        cor_variacao = "#60b59b" if variacao_total > 0 else "#e895a4" if variacao_total < 0 else "#f5f5f7"

        classe = str(ativo['classe']).lower().strip()
        cotacao_formatada = (self.formatar_usd(cotacao) if classe in ('stock', 'reit') else self.formatar_brl(cotacao))
        preco_medio_formatado = self.formatar_usd(preco_medio) if classe in ('stock', 'reit') else self.formatar_brl(preco_medio)
        sinal = "+" if variacao_total > 0 else ""

        campos = [
            ("Cotação", cotacao_formatada, "#f5f5f7", 0, 0),
            ("Quantidade", f"{quantidade}", "#f5f5f7", 0, 1),
            ("Preço médio", preco_medio_formatado, "#f5f5f7", 0, 2),
            ("Total investido", self.formatar_brl(total_investido), "#f5f5f7", 0, 3),
            ("Total atual", self.formatar_brl(total_atual), "#f5f5f7", 1, 0),
            ("Variação atual", f"{sinal}{self.formatar_brl(variacao_total)}", cor_variacao, 1, 1),
            ("% Meta", f"{porcentagem_meta:.2f}%", "#f5f5f7", 1, 2),
            ("% Atual", f"{porcentagem_atual:.2f}%", "#f5f5f7", 1, 3),
        ]
        
        for titulo, valor, cor, row, col in campos:
            campo = self.criar_campo_card(titulo, valor, cor)
            grid_valores.addWidget(campo, row, col)
        
        layout_card.addLayout(grid_valores)
        return card

    def carregar_cards_por_classe(self, classe, container):
        df_filtrado = self.ativos[self.ativos['classe'].str.lower().str.strip() == classe]
        
        for _, ativo in df_filtrado.iterrows():
            card = self.criar_card_individual(ativo)
            container.layout().addWidget(card)

    def carregar_cards_individuais_stocks(self):
        self.carregar_cards_por_classe('stock', self.container_cards_stocks)

    def carregar_cards_individuais_reits(self):
        self.carregar_cards_por_classe('reit', self.container_cards_reits)

    def carregar_cards_individuais_acoes(self):
        self.carregar_cards_por_classe('acao', self.container_cards_acoes)

    def carregar_cards_individuais_fiis(self):
        self.carregar_cards_por_classe('fii', self.container_cards_fiis)

    def carregar_cards_individuais_criptos(self):
        self.carregar_cards_por_classe('cripto', self.container_cards_criptos)
        
    def gerenciar_posicao_tamanho_janela(self, salvar=False):
        if salvar:
            self.posicao_tamanho_janela.setValue('posicao', self.pos())
            self.posicao_tamanho_janela.setValue('tamanho', self.size())
        else:
            self.resize(self.posicao_tamanho_janela.value('tamanho', self.size()))
            self.move(self.posicao_tamanho_janela.value('posicao', self.pos()))

    def closeEvent(self, event):
        self.gerenciar_posicao_tamanho_janela(salvar=True)
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())