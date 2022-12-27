class Node: #nó 
    def __init__(self, data):
        self.data = data # dado armazenado
        self.left = None # filho a esqueda
        self.right = None # filho a direita
    
    def __str__(self) -> str:
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None) -> None:
        if data:
            node = Node(data)
            self.root = node # raiz da árvore 
        else:
            self.root = None

    # percurso em ordem simétrica 
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            # parênteses são específicos para o nosso exemplo,
            # um percurso em ordem simétrica não precisa deles
            print('(', end='') 
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')
        

    

