import sqlite3

conexao = sqlite3.connect('reservas.db')
cursor = conexao.cursor()
cursor.execute('PRAGMA foreign_keys = ON')

def laboratorios():
    cursor.execute('''CREATE TABLE IF NOT EXISTS informatica01(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_solicitante TEXT NOT NULL,
                        laboratorio TEXT NOT NULL,
                        data TEXT UNIQUE NOT NULL,
                        horario TEXT NOT NULL)''')

     cursor.execute('''CREATE TABLE IF NOT EXISTS informatica02(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_solicitante TEXT NOT NULL,
                        laboratorio TEXT NOT NULL,
                        data TEXT UNIQUE NOT NULL,
                        horario TEXT NOT NULL)''')

     cursor.execute('''CREATE TABLE IF NOT EXISTS robotica(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_solicitante TEXT NOT NULL,
                        laboratorio TEXT NOT NULL,
                        data TEXT UNIQUE NOT NULL,
                        horario TEXT NOT NULL)''')

     cursor.execute('''CREATE TABLE IF NOT EXISTS eletronicos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_solicitante TEXT NOT NULL,
                        laboratorio TEXT NOT NULL,
                        data TEXT UNIQUE NOT NULL,
                        horario TEXT NOT NULL)''')

def 
