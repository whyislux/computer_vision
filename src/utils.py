def normalize_name(txt):
    """
        Esta función normaliza strings.
        Lo que hace es quitar espacios en 
        blanco al inicio y fin de mi string,
        espacios en blanco los elimina.
        Y el nombre en titulo. 

        Ej.
        cArLOs     AnToNIo -> Carlos Antonio
        :params (str): texto de entrada
        :return: texto formateado
    """
    return " ".join(txt.strip().title().split())

def to_mxn(valor, tasa: float=1.0):
    """
    Docstring for to_mxn
    Convierte valor numerico a MXN multiplicando por la tasa
    
    :param valor: Description
    :param tasa: Description
    :type tasa: float
    """
    return float(valor)*float(tasa)
