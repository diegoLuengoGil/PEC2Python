class Utils:
    """
    Clase que contiene métodos estáticos para validación de entrada de datos.   
    """

    @staticmethod
    def get_int(prompt: str) -> int:
        '''Solicita un entero al usuario hasta que se ingrese un valor válido'''
        valid = False
        value = 0
        while not valid:
            try:
                user_input = input(prompt)
                value = int(user_input)
                valid = True
            except ValueError:
                print("Error: Please enter a valid integer.")
        return value

    @staticmethod
    def get_float(prompt: str) -> float:
        '''Solicita un decimal al usuario hasta que se ingrese un valor válido'''
        valid = False
        value = 0.0
        while not valid:
            try:
                user_input = input(prompt)
                value = float(user_input)
                valid = True
            except ValueError:
                print("Error: Please enter a valid number.")
        return value

    @staticmethod
    def get_non_empty_str(prompt: str) -> str:
        """Repeatedly asks for a string until non-empty."""
        valid = False
        value = ""
        while not valid:
            value = input(prompt).strip()
            if value:
                valid = True
            else:
                print("Error: Input cannot be empty.")
        return value

    

    @staticmethod
    def confirmar_accion(mensaje: str) -> bool:
        '''Solicita una confirmación al usuario hasta que se ingrese un valor válido'''
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        return respuesta == 's'
