class Dispositivo:
    def __init__(self, nome, tipo, setor=None):
        self.nome = nome
        self.tipo = tipo  # Servidor, PC, Roteador, Firewall
        self.setor = setor  # RH, Financeiro, Dev, etc.

    def __repr__(self):
        return f"{self.tipo}({self.nome})"


class Rede:
    def __init__(self):
        self.dispositivos = []
        self.regras = []

    def adicionar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def adicionar_regra(self, origem, destino, permitido=True):
        """Define se a comunicação entre origem e destino é permitida"""
        self.regras.append((origem, destino, permitido))

    def enviar_mensagem(self, origem, destino, mensagem):
        for regra in self.regras:
            if regra[0] == origem and regra[1] == destino:
                if regra[2]:
                    print(f"[OK] {origem.nome} → {destino.nome}: {mensagem}")
                else:
                    print(f"[BLOCK] {origem.nome} → {destino.nome}: Acesso negado")
                return
        print(f"[?] {origem.nome} → {destino.nome}: Sem regra definida")

    def mostrar_dispositivos(self):
        print("\n=== Dispositivos na Rede ===")
        for d in self.dispositivos:
            setor_info = f" | Setor: {d.setor}" if d.setor else ""
            print(f"- {d.tipo}: {d.nome}{setor_info}")
        print("============================\n")


# --- Simulação da Rede ---
rede = Rede()

# Criando dispositivos
pc_rh = Dispositivo("RH_PC1", "PC", "RH")
pc_fin = Dispositivo("Financeiro_PC1", "PC", "Financeiro")
pc_dev = Dispositivo("Dev_PC1", "PC", "Desenvolvimento")

servidor_web = Dispositivo("Servidor_Web", "Servidor")
servidor_bd = Dispositivo("Servidor_BD", "Servidor")
servidor_arquivos = Dispositivo("Servidor_Arquivos", "Servidor")

externo = Dispositivo("Externo", "Usuário")

# Adicionando dispositivos na rede
for d in [pc_rh, pc_fin, pc_dev, servidor_web, servidor_bd, servidor_arquivos, externo]:
    rede.adicionar_dispositivo(d)

# Mostrar todos os dispositivos cadastrados
rede.mostrar_dispositivos()

# Regras de comunicação
rede.adicionar_regra(pc_rh, servidor_arquivos, True)
rede.adicionar_regra(pc_fin, servidor_bd, True)
rede.adicionar_regra(pc_rh, servidor_bd, False)  # RH não acessa BD financeiro
rede.adicionar_regra(externo, servidor_web, True)
rede.adicionar_regra(externo, servidor_bd, False)

# Testando comunicações
rede.enviar_mensagem(pc_fin, servidor_bd, "Consulta de relatórios")
rede.enviar_mensagem(pc_rh, servidor_bd, "Tentativa de acesso")
rede.enviar_mensagem(externo, servidor_web, "Acessando site da empresa")
rede.enviar_mensagem(externo, servidor_bd, "Tentando invadir BD")

