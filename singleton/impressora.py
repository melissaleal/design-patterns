class GerenciadorDeImpressao():
    __instance = None
    
    def __new__(cls):
        if GerenciadorDeImpressao.__instance is None:
            GerenciadorDeImpressao.__instance = super().__new__(cls)
        return GerenciadorDeImpressao.__instance
    
    def __init__(self):
        if not hasattr(self, 'documentos'):
            self.documentos = []
            
    def addDoc(self, documento):
        self.documentos.append(documento)
        
    def delDoc(self, doc):
        if self.documentos:
            self.documentos.pop(doc)
            
    def fila(self):
        print(f'Documentos na fila de impressão: ', self.documentos)
        
if __name__ == "__main__":
    impressora1 = GerenciadorDeImpressao()
    impressora1.addDoc('Atividade de matemática.pdf')
    impressora1.addDoc('Letra de Star Lost.pdf')
    impressora1.addDoc('Gabarito do vestibular.pdf')
    impressora1.addDoc('Seungmin em tamanho real.pdf')
    
    impressora2 = GerenciadorDeImpressao()
    impressora2.fila()
    
    impressora1.delDoc(2)
    impressora2.fila()
