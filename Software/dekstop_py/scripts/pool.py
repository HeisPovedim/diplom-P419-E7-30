from sys import argv
import serial
import struct
from math import *

# Конфигурация порта - ARDUINO
'''
Для систем под управление Windows обычно используется COM3 порт, для подключения к устройству.
Для систем под управлением Linux обычно используется /dev/ttyUSB0 порт, для подключения к устройству.

ВНИМАНИЕ! В Windows используется другая система нумерации COM-портов.
Вы должны заменить /dev/ttyUSB0 на соответствующий номер COM-порта для вашей системы.
Также может потребоваться установить драйверы для вашего устройства,
чтобы оно было распознано как COM-порт в Windows.
'''

ser = serial.Serial(
  port = '/COM3',
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1.2
)

#---------------------Команды-------------------------
default = (0xAA, 71)    # состояние по-умолчанию
parameters = (0xAA, 72) # выдача полной измеряемой информации
scheme = (0xAA, 0x0d)   # смена схемы замещения
#-----------------------------------------------------

def set_default():
  """Проверки и перевод прибора в состояние по-умолчанию"""

  try:
    if ser.isOpen():
      ser.write(default)
      checkout = ser.read(2)
      if struct.unpack('>2B', checkout) == default:
        ser.read(4)
    else:
      print(">> Неполадки с портом\n")
  except struct.error:
    print(">> Нет соединения с прибором\n")

def change_scheme():
  """Изменение схемы замещения"""
  ser.write(scheme)
  check_scheme = ser.read(2)
  if struct.unpack('>2B', check_scheme) == scheme:
    ser.read(2)
    

def set_freq(F):
  """Установка частоты"""
  f = int(F).to_bytes(4,'big')
  freq = (0xAA, 67, f[0], f[1], f[2], f[3])
  ser.write(freq)
  data = ser.read(4)
  
def calc_all(Fstart, Fstop, Step, z_only):
  """Измерение всех величин"""

  Gp_list = []
  Rp_list = []
  Cp_list = []
  Z_list = []
  Phi_list = []
  F_list_Parallel = []
  F_list_Consistent = []

  if not z_only:
    change_scheme() # изменение схемы замещения
    for i in range(Fstart, Fstop + Step, Step):
      set_freq(i)
      ser.write(parameters)
      data = struct.unpack('>3B3bhiff', ser.read(20))
      f, z, fi = data[7], data[8], data[9]
      F_list_Parallel.append(i/1000.)
      Gp_list.append(cos(fi) / abs(z))
      Rp_list.append(abs(z) / cos(fi))
      Cp_list.append(1 / (2. * pi * f * abs(z) * sin(-fi)))

      # !ДЛЯ ОТЛАДКИ: ВЫВОД ЗНАЧЕНИЙ НА КАЖДОЙ ИТЕРАЦИИ
      # print(f"Параллельная, F={i/1000.} кГц", end='\n', flush=True)
      # print(f"Gp={Gp_list} См", end='\n', flush=True)
      # print(f"Rp={Rp_list} Ом", end='\n', flush=True)
      # print(f"Cp_list={Cp_list} нФ", end='\n', flush=True)

    # Вывод всех данных после подсчета
    print(F_list_Parallel, end='\n', flush=True)
    print(Gp_list, end='\n', flush=True)
    print(Rp_list, end='\n', flush=True)
    print(Cp_list, end='\n', flush=True)

    change_scheme() # изменение схемы замещения

  for i in range(Fstart, Fstop + Step, Step):
    
    set_freq(i)
    ser.write(parameters)
    data = struct.unpack('>3B3bhiff', ser.read(20))
    f, z, fi = data[7], data[8], data[9]
    F_list_Consistent.append(i/1000.)
    Z_list.append(z)
    Phi_list.append(fi)

    # !ДЛЯ ОТЛАДКИ: ВЫВОД ЗНАЧЕНИЙ НА КАЖДОЙ ИТЕРАЦИИ
    # print(f"Последовательная, F={i/1000.} кГц", end='\n', flush=True)
    # print(f"Z={z} Oм", end='\n', flush=True)
    # print(f"Phi={fi} Гр", end='\n', flush=True)

  # Вывод всех данных после подсчета
  print(F_list_Consistent, end='\n', flush=True)
  print(Z_list, end='\n', flush=True)
  print(Phi_list, end='\n', flush=True)
  

set_default() # Проверки и перевод прибора в состояние по-умолчанию
calc_all() # измерение всех величин