# Este projeto simula um sistema bancário simples, 100% operado via terminal, desenvolvido com base nos conteúdos apresentados nas aulas da DIO (Digital Innovation One) e **incrementado com melhorias visuais e estruturais**.

## 🚀 Funcionalidades

- Depósito com validação de valor  
- Saque com limite de valor e quantidade diária  
- Visualização do extrato com histórico de operações  
- Encerramento do sistema  
- Feedback visual para cada operação  

---

## 🧠 Tecnologias e conceitos aplicados

- **Python 3**  
- **Programação Orientada a Objetos (POO)**  
- **Validação de entrada do usuário**  
- **Manipulação de strings e listas**  
- Estilização no terminal com:  
  - [`colorama`](https://pypi.org/project/colorama/) — cores para interface  
  - [`pyfiglet`](https://pypi.org/project/pyfiglet/) — logo ASCII no terminal  

---

## 🎨 Diferenciais do projeto

Além de seguir a lógica ensinada nas aulas, foram feitos diversos incrementos para elevar a experiência do usuário, mesmo dentro do terminal:

- Layout do menu com **cores e divisões elegantes**  
- Cabeçalho visual com o nome do banco (`pyfiglet`)  
- Separação clara entre funções com mensagens destacadas  
- Estrutura de código modular e reutilizável com classes  

---

## 📸 Exemplo no terminal

```plaintext
████████╗██╗  ██╗ █████╗ ██╗     ██╗██╗   ██╗███╗   ███╗
╚══██╔══╝██║  ██║██╔══██╗██║     ██║██║   ██║████╗ ████║
   ██║   ███████║███████║██║     ██║██║   ██║██╔████╔██║
   ██║   ██╔══██║██╔══██║██║     ██║██║   ██║██║╚██╔╝██║
   ██║   ██║  ██║██║  ██║███████╗██║╚██████╔╝██║ ╚═╝ ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝     ╚═╝

Bem-vindo ao sistema bancário da Thalium

Inicializando sistema...
------------------------------------------------------------

╔════════════════════ MENU ════════════════════╗
║ [d] Depositar                               ║
║ [s] Sacar                                   ║
║ [e] Extrato                                 ║
║ [q] Sair                                    ║
╚═════════════════════════════════════════════╝
=> 
