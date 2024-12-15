class Dia:
  def __init__(self, temperatura):
    self.temperatura = temperatura

  def get_temperatura(self):
    return self.temperatura

class Semana:
  def __init__(self):
    self.dias = []

  def agregar_dia(self, dia):
    self.dias.append(dia)

  def calcular_promedio(self):
    temperaturas = [dia.get_temperatura() for dia in self.dias]
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

if __name__ == "__main__":
  semana = Semana()
  for dia in range(1, 14):
    temperatura = float(input(f"8°,18°,9°,15°,17°,10°,20°,18° {dia}: "))
    dia_obj = Dia(temperatura)
    semana.agregar_dia(dia_obj)

  promedio_semanal = semana.calcular_promedio()
  print(f"El promedio semanal de temperaturas es: {promedio_semanal:.4f} °C")