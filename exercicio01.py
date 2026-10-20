nome = input("Nome: ")
salario = float(input("Salário Bruto: ").replace(",","."))
if salario >= 3000:
    inss = salario * 0.11
elif salario >= 2000:
    inss = salario * 0.09
else:
    inss = salario * 0.08

if salario >= 2000:
    vale = salario * 0.06
else:
    vale = salario *0.05

if salario >= 3000:
    bonus = 300
else:
    bonus = 200

if salario >= 3000:
    cargo = "Acionista"
elif salario >= 2000:
    cargo = "Gerente"
else:
    cargo = "Vendedor"

salarioLiquido = salario - (inss + vale) + bonus
print(f"Nome: {nome}")
print(f"Salário Bruto: R$ {salario:.2f}".replace(".",","))
print(f"INSS: R$ {inss:.2f}".replace(".",","))
print(f"Vale Transporte: R$ {vale:.2f}".replace(".",","))
print(f"Bônus: R$ {bonus:.2f}".replace(".",","))
print(f"Cargo: {cargo}")
print(f"Salário Líquido: R$ {salarioLiquido:.2f}".replace(".",","))