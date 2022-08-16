""" Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade 
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo 
usando este link (em minutos).
"""

tamanho = float(input("Informe o tamanho do arquivo a ser baixado (em MB): "))
velocidade = float(input("Informe a velocidade da conexão (em Mbps): "))
tamanho_mbps = tamanho * 8
min_download = (tamanho_mbps / velocidade) / 60
seg_download = (tamanho_mbps / velocidade) % 60

print(f"Seu arquivo irá levar {min_download:.0f} minutos e {seg_download:.0f} segundos para concluir o download!")