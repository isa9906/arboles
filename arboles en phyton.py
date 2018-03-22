class Arbol:
    def __init__ (self,val,izq=None,der=None):
        self.valor=val
        self.izquierda=izq
        self.derecha=der
        
def buscar (valor,arbol):
    if arbol == None:
        return False
    if arbol.valor==valor:
        return True
    if valor>arbol.valor:
        return buscar(valor,arbol.derecha)
    return buscar(valor,arbol.izquierda)
def inorder (arbol):
    if arbol==None:
        return []
    else:
       return inorder(arbol.izquierda)+[arbol.valor]+inorder(arbol.derecha) 
   
        
def insert (arbol,valor):
    if (arbol==None):  
        return Arbol(valor)
    if(valor>arbol.valor):
        return Arbol(arbol.valor,arbol.izquierda,insert(arbol.derecha,valor))
    if (valor<arbol.valor):
        return Arbol(arbol.valor,insert(arbol.izquierda,valor),arbol.derecha)
    if arbol.valor == valor:
        return arbol

def insertLista(arbol,lista):
    if lista==[]:
        return arbol
    else:
        return insertLista(insert(arbol,lista[0]),lista[1:]) 
        
    
    
arbol1=Arbol(10,Arbol(5),Arbol(50,Arbol(30,Arbol(20),Arbol(40))))
arbol2=insertLista(arbol1,[10,18,22])
print(inorder(arbol2))
#print(inorder (insertLista(arbol1,[18,20,1])))
