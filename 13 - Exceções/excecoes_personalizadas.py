class SaldoInsuficienteError(Exception):
    pass

def sacar(valor, saldo):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente.")
    saldo = saldo - valor
    return saldo

sacar(100, 50)