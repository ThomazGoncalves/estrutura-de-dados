from no import No

class ListaEncadeada:
    def __init__(self) -> None:
        self.cabeca = None   # localização do primeiro nó 
        self._tamanho = 0        # tamanho do meus nós 

    def append(self, elem):
        if self.cabeca:
            # insert quando a lista já tem um elemento
            ponteiro = self.cabeca
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(elem)
        else:
            # primeiro insert se a lista estiver vazia 
            self.cabeca = No(elem)
        self._tamanho += 1

    def __len__(self): # mostra o tamanho da minha lista
        return self._tamanho

    def __getitem__(self, index): #busco um item na minha lista através do index
        # a = lista[6]
        # a = lista.get(6)
        ponteiro = self.cabeca
        for i in range(index):
            if ponteiro:
                ponteiro =  ponteiro.proximo
            else:
                raise IndexError('índice da lista fora do intervalo')
        if ponteiro:
            return ponteiro.dado
        raise IndexError('índice da lista fora do intervalo')

    def __setitem__(self, index, elem): # substituo um item da minha lista, passando o indíce e o elemento 
        # a = lista.set(6, 5)
        ponteiro = self.cabeca
        for i in range(index):
            if ponteiro:
                ponteiro =  ponteiro.proximo
            else:
                raise IndexError('índice da lista fora do intervalo')
        if ponteiro:
             ponteiro.dado = elem
        else:
            raise IndexError('índice da lista fora do intervalo')

    def index(self, elem): # busco o elemento através do índice 
        ponteiro = self.cabeca
        i = 0
        while ponteiro:
            if ponteiro.dado == elem:
                return i
            ponteiro = ponteiro.proximo
            i += 1
        raise IndexError('índice da lista fora do intervalo')

