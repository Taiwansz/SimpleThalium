try:
    import pyfiglet
except ImportError:
    import os
    os.system('pip install pyfiglet')
    import pyfiglet



import textwrap
import time
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

class ContaBancaria:
    def __init__(self, limite=500, limite_saques=3):
        self.saldo = 0.0
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(Fore.GREEN + "Depósito realizado com sucesso.")
        else:
            print(Fore.RED + "Operação falhou: valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= 0:
            print(Fore.RED + "Operação falhou: valor inválido para saque.")
        elif valor > self.saldo:
            print(Fore.RED + "Operação falhou: saldo insuficiente.")
        elif valor > self.limite:
            print(Fore.RED + f"Operação falhou: valor excede o limite de R$ {self.limite:.2f}.")
        elif self.numero_saques >= self.limite_saques:
            print(Fore.RED + "Operação falhou: número máximo de saques atingido.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print(Fore.GREEN + "Saque realizado com sucesso.")

    def exibir_extrato(self):
        print(Fore.CYAN + "\n╔════════════════════════ EXTRATO ════════════════════════╗")
        if not self.extrato:
            print("║ Nenhuma movimentação registrada.                      ║")
        else:
            for operacao in self.extrato:
                print(f"║ {operacao:<50}║")
        print(f"║ Saldo atual: R$ {self.saldo:>37.2f} ║")
        print("╚═════════════════════════════════════════════════════════╝")

def mostrar_menu():
    menu = f"""
{Fore.YELLOW}
╔════════════════════ MENU ════════════════════╗
║ [d] Depositar                               ║
║ [s] Sacar                                   ║
║ [e] Extrato                                 ║
║ [q] Sair                                    ║
╚═════════════════════════════════════════════╝
=> """
    return input(textwrap.dedent(menu))

def abertura():
    print(Fore.CYAN + pyfiglet.figlet_format("Thalium Bank"))
    print(Fore.LIGHTWHITE_EX + "Bem-vindo ao sistema bancário da Thalium".center(80))
    print(Fore.GREEN + "Inicializando sistema", end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n" + Fore.WHITE + "-" * 60)

def main():
    abertura()
    conta = ContaBancaria()

    while True:
        opcao = mostrar_menu().lower().strip()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: R$ "))
                conta.depositar(valor)
            except ValueError:
                print(Fore.RED + "Entrada inválida. Digite um número.")
        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: R$ "))
                conta.sacar(valor)
            except ValueError:
                print(Fore.RED + "Entrada inválida. Digite um número.")
        elif opcao == "e":
            conta.exibir_extrato()
        elif opcao == "q":
            print(Fore.LIGHTWHITE_EX + "\nEncerrando sessão... Até logo.")
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
