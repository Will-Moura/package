from packagecp.formatar import output

def aumento(valor, porcentagem, formatar=False):
    r = valor + (valor * (porcentagem / 100))  

    if formatar == True:
        return output.real(r)
    else: 
        return r
 
def reducao (valor, porcentagem, formatar=False):
    r = valor - (valor * (porcentagem/100)) 
    
    if formatar == True:
        return output.real(r) 
    else: 
        return r