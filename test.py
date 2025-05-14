print("test")
print('Hola')
print('coucuo')

def integral(a, b, n):
    """
    Calcule l'intégrale de la fonction f(x) = x^2 sur l'intervalle [a, b] en utilisant la méthode des trapèzes.
    
    :param a: Limite inférieure de l'intervalle
    :param b: Limite supérieure de l'intervalle
    :param n: Nombre de subdivisions
    :return: Valeur approchée de l'intégrale
    """
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    
    integral *= h
    return integral