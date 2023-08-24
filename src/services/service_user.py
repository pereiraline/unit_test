from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def validando_se_existe_usuario(self, name):
        lista = self.store.bd

        if len(lista) >= 1:
            for i in range(len(lista)):
                if lista[i].name == name:
                    return True

    def add_user(self, name, job):

        if name is not None and job is not None:

            if isinstance(name, str) and isinstance(job, str):
                #if self.search_user(name) is None:"
                if not self.validando_se_existe_usuario(name):
                    user = User(name, job)
                    self.store.bd.append(user)
                    return f"Usuário {name} adicionado"
                else:
                    return "Não é possivel adicionar usuário já cadastrado!"
            else:
                return "Parametros Invalidos"
        else:
            return "Requer preenchimento dos campos"

    def remove_user(self, name):
        if self.validando_se_existe_usuario(name):
            lista = self.store.bd

            for i in range(len(lista)):
                if lista[i].name == name:
                    lista.pop(i)
                    return f"Usuário {name} removido"

        return f"Não foi possível remover o usuário {name}, já que ele não foi encontrado!"


    def get_user(self, name):
        if self.validando_se_existe_usuario(name):
            lista = self.store.bd

            for i in range(len(lista)):
                if lista[i].name == name:
                    lista.pop(i)
                    return f"Usuário {name} recuperado!"

        return f"Usuário {name}, não localizado!"