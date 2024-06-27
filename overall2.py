def calcular_overall(pontos, assistencias, rebotes, bloqueios, roubos_bola, eficiencia_arremesso):
    # Pesos para cada estatística
    peso_pontos = 0.3
    peso_assistencias = 0.2
    peso_rebotes = 0.2
    peso_bloqueios = 0.1
    peso_roubos_bola = 0.1
    peso_eficiencia_arremesso = 0.1
    
    # Cálculo do overall ponderado
    overall = (pontos * peso_pontos + 
               assistencias * peso_assistencias + 
               rebotes * peso_rebotes + 
               bloqueios * peso_bloqueios + 
               roubos_bola * peso_roubos_bola + 
               eficiencia_arremesso * peso_eficiencia_arremesso)
    return overall

def main():
    print("Calculadora de Overall Avançada de Jogadores da NBA")
    print("---------------------------------------------------")
    pontos = float(input("Digite o número médio de pontos por jogo: "))
    assistencias = float(input("Digite o número médio de assistências por jogo: "))
    rebotes = float(input("Digite o número médio de rebotes por jogo: "))
    bloqueios = float(input("Digite o número médio de bloqueios por jogo: "))
    roubos_bola = float(input("Digite o número médio de roubos de bola por jogo: "))
    eficiencia_arremesso = float(input("Digite a eficiência de arremesso (0 a 100): "))
    
    overall = calcular_overall(pontos, assistencias, rebotes, bloqueios, roubos_bola, eficiencia_arremesso)
    
    print("\nO overall do jogador é:", overall)

main()