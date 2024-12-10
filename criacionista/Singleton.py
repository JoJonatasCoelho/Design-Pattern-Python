# Singleton em python

# permite apenas uma instancia

# modulos tem comportamento de singleton 
 
class Singleton:
    name = "Seila"

    idd : int
    def __new__(cls):
        _singleton = None
        if(not _singleton):
            _singleton = cls
        return _singleton
    
sing1 = Singleton()
sing1.idd = 1

sing2 = Singleton()
print(sing1 is sing2)