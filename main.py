import tkinter as tk
from captura_nome import CapturaNomeApp
from interface_principal import InterfacePrincipalApp

def main():
    # Iniciar a captura do nome
    root_captura_nome = tk.Tk()
    app_captura_nome = CapturaNomeApp(root_captura_nome)
    root_captura_nome.mainloop()

    # Obtendo o nome capturado
    nome_capturado = app_captura_nome.nome_capturado if hasattr(app_captura_nome, 'nome_capturado') else "Nome Padrão"

    # Iniciar a interface principal com o nome capturado
    root_interface_principal = tk.Tk()
    app_interface_principal = InterfacePrincipalApp(root_interface_principal, nome_capturado)
    root_interface_principal.mainloop()

if __name__ == "__main__":
    main()