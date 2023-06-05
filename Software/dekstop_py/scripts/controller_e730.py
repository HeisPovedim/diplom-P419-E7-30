# ШАГИ ЗАПУСКА И РАБОТЫ С Контроллером
# 1 - создать объект - там настроится весь cfg
# 2 -  вызвать функцию set_default() # Проверки и перевод прибора в состояние по-умолчанию
# 3 calc_all() # измерение всех величин - здесь также данные сразу побегут в БД

import serial
import struct
from PyQt6.QtWidgets import QMessageBox,QWidget
from math import *
from typing import Any, Union
from database.requests import add_parameters_parallel,add_parameters_consistent



class ControllerE730(object):
    def __init__(self, id_object: int, fstart: int, fend: int, step: int, z_only: bool):
        self.modal = QWidget()
        self.id_object = id_object
        
        # ПАРАМЕТРЫ
        self.fstart = fstart
        self.fend = fend
        self.step = step
        self.z_only = z_only
        
        '''
        Конфигурация порта - ARDUINO
        Для систем под управление Windows обычно используется COM3 порт, для подключения к устройству.
        Для систем под управлением Linux обычно используется /dev/ttyUSB0 порт, для подключения к устройству.

        ВНИМАНИЕ! В Windows используется другая система нумерации COM-портов.
        Вы должны заменить /dev/ttyUSB0 на соответствующий номер COM-порта для вашей системы.
        Также может потребоваться установить драйверы для вашего устройства,
        чтобы оно было распознано как COM-порт в Windows.
        '''

        self.ser = serial.Serial(
            port='COM0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1.2
        )
        # ---------------------Команды-------------------------
        self.default = (0xAA, 71)  # состояние по-умолчанию
        self.parameters = (0xAA, 72)  # выдача полной измеряемой информации
        self.scheme = (0xAA, 0x0d)  # смена схемы замещения
        # -----------------------------------------------------

    # utils
    def get_real_and_imag_parts(self,complex_num: Union[complex, Any]) -> tuple[float, float]:
        if isinstance(complex_num, complex):
            real_part = complex_num.real
            imag_part = complex_num.imag
            return real_part, imag_part
        else:
            raise ValueError("Input is not a complex number.")

    # end utils
        # ----------Проверки и перевод прибора в состояние по-умолчанию----------
    def set_default(self):
        """Проверки и перевод прибора в состояние по-умолчанию"""
        
        try:
            if self.ser.isOpen():
                self.ser.write(self.default)
                checkout = self.ser.read(2)
                if struct.unpack('>2B', checkout) == self.default:
                    self.ser.read(4)
                    return True
                else:
                    QMessageBox.warning(self.modal,'Ошибка подключения','неполадки с портом')
        except struct.error:
            QMessageBox.warning(self.modal,'Ошибка подключения','Нет соединения с прибором')
        # -----------------------------------------------------------------------
        # #-----------------------Изменение схемы замещения-----------------------
    
    def change_scheme(self):
        """Изменение схемы замещения"""
        
        self.ser.write(self.scheme)
        check_scheme = self.ser.read(2)
        if struct.unpack('>2B', check_scheme) == self.scheme:
            self.ser.read(2)
        # #-----------------------------------------------------------------------
        # #---------------------------Установка частоты---------------------------
    
    def set_freq(self, F):
        """Установка частоты"""
        
        f = int(F).to_bytes(4, 'big')
        freq = (0xAA, 67, f[0], f[1], f[2], f[3])
        self.ser.write(freq)
        self.ser.read(4)
        
        # #-----------------------------------------------------------------------
    
    # #------------------------Измерение всех величин-------------------------
    def calc_all(self):
        """Измерение всех величин"""
        
        global Gp_list, Rp_list, Cp_list, Z_list, Phi_list, F_list_Consistent, F_list_Parallel
        
        Gp_list = []
        Rp_list = []
        Cp_list = []
        Z_list = []
        Phi_list = []
        F_list_Parallel = []
        F_list_Consistent = []
        
        if not self.z_only:
            self.change_scheme()  # изменение схемы замещения
            for i in range(self.fstart, self.fstart + self.step, self.step):
                self.set_freq(i)
                self.ser.write(self.parameters)
                data = struct.unpack('>3B3bhiff', self.ser.read(20))
                f, z, fi = data[7], data[8], data[9]
                F_list_Parallel.append(i / 1000.)
                Gp_list.append(cos(fi) / abs(z))
                Rp_list.append(abs(z) / cos(fi))
                Cp_list.append(1 / (2. * pi * f * abs(z) * sin(-fi)))
            self.change_scheme()  # изменение схемы замещения
        
        for i in range(self.fstart, self.fstart + self.step, self.step):
            self.set_freq(i)
            self.ser.write(self.parameters)
            data = struct.unpack('>3B3bhiff', self.ser.read(20))
            f, z, fi = data[7], data[8], data[9]
            F_list_Consistent.append(i / 1000.)
            Z_list.append(z)
            Phi_list.append(fi)
        # #----------------------------------------------------------------------- 
        # 
        # Запись результатов измерия в базу данных      
        if not self.z_only:
            # call add parallel and consistent

            # перебор массива в котором хранится значение частот измерений на парал схеме замещения
            for i,freq in enumerate(F_list_Parallel):
                add_parameters_parallel(freq,Gp_list[i],Rp_list[i],Cp_list[i],self.id_object)

            # перебор массива в котором хранится значение частот измерений на последовательной схеме замещения
            for i,freq in enumerate(F_list_Consistent):
                real,imaginary = self.get_real_and_imag_parts(Z_list[i])
                add_parameters_consistent(freq,real,imaginary,Phi_list[i],self.id_object)

        else:
            # перебор массива в котором хранится значение частот измерений на последовательной схеме замещения

            for i,freq in enumerate(F_list_Consistent):
                real,imaginary = self.get_real_and_imag_parts(Z_list[i])
                add_parameters_consistent(freq,real,imaginary,Phi_list[i],self.id_object)