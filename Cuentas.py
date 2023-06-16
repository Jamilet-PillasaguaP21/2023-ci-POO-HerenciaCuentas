from abc import ABC, abstractmethod

class Cuenta(ABC):
    def init(self, numero, nombre_propietario, saldo):
        self.numero = numero
        self.nombre_propietario = nombre_propietario
        self.saldo = saldo

    @abstractmethod
    def credito(self, valor):
        pass

    @abstractmethod
    def debito(self, valor):
        pass

    @abstractmethod
    def mostrar_saldo(self):
        pass


class CuentaAhorro(Cuenta):
    def init(self, numero, nombre_propietario, saldo, interes):
        super().init(numero, nombre_propietario, saldo)
        self.interes = interes

    def credito(self, valor):
        self.saldo += valor

    def debito(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print("No se puede realizar la operación. Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

    def pagar_interes(self):
        interes_generado = self.saldo * self.interes
        self.saldo += interes_generado


class CuentaCorriente(Cuenta):
    def init(self, numero, nombre_propietario, saldo, tiene_chequera):
        super().init(numero, nombre_propietario, saldo)
        self.tiene_chequera = tiene_chequera

    def credito(self, valor):
        self.saldo += valor

    def debito(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print("No se puede realizar la operación. Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

    def pagar_cheque(self, valor):
        if self.tiene_chequera:
            if self.saldo - valor >= 0:
                self.saldo -= valor
            else:
                print("No se puede realizar la operación. Saldo insuficiente.")
        else:
            print("No se puede pagar el cheque. La cuenta no tiene una chequera.")
