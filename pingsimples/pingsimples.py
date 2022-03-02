import os   #importa o módulo ou biblioteca os (integra os programas e recursos)

print("#"*60)

ip_ou_host = input("Digite o IP ou host a ser verificado: ")
#criando uma variável que vai receber do usuário um ip
print("-"*60) ##Imprimindo - 60 vezes
os.system('ping -n 6 {}' .format(ip_ou_host)) ##chamando o system da biblioteca os - comando ping
print("-"*60)
