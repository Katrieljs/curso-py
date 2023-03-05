class MiExcepcion(Exception):
    def __init__(self, err):
        print(f'De locos, cometiste el siguiente error: {err}')


try:
    raise MiExcepcion("jasjaja bobito")
except:
    print("Como le hiciste")
