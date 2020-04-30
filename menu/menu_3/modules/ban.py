class logo:
  @classmethod
  def tool_header(self):
    print('''\033[1;33m
("`-''-/").___..--''"`-._
 `6_ 6  )   `-.  (     ).`-.__.`)
 (_Y_.)'  ._   )  `._ `. ``-..-'
   _..`--'_..-_/  /--'_.'	\033[1;32mHERRAMIENTAS
  ((((.-''  ((((.'  (((.-'
''')

  @classmethod
  def nonet(self):
    print ("")
    print ("\033[1;35m Not_Found")
    print ("")
    print ('''
\033[1;31m  [*]  \033[1;31mNo tienes internet, CONECTATE!!\033[00m''')
    print ("")

  @classmethod
  def already_installed(self,name):
    print(f'''\033[1;32m'{name}'\033[1;32m Ya esta instalado''')

  @classmethod
  def installed(self,name):

    print(f'''\033[1;37m
░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░░
░░░░░░▄▄▀▀░░░░░░░▀▀▄▄░░░░░░
░░░░▄▀░░░░░░░░░░░░░░░▀▄░░░░
░░░▄▀░░░▄▄▄▄▄▄▄▄▄▄▄░░░░█░░░ \033[1;33m '{name}'\033[01;32m Instalado correctamente\033[1;37m
░░█░░▄███████████████▄░░█░░
░█░░▄██▀░▄▄▀███▀▄▄░▀███░░█░
░█░░▀█████████████████▀░░█░
░█░░░░▀▀████████████▀░░░░█░  No olvides leer el archivo README.md para
░░█░░░░░░░░▀▀▀▀▀░░░░░░░▄▀░░  que sepas la funcionalidad del script, y
░░░▀▀▄▄▄▄░░░░░░░░░▄▄▄▀▀░░░░  el proceso de uso.\033[1;37m
░░▄██▀▄▄▄█▀▀▀▀▀▀▀█▄▄▄▀██▄░░
░▄▀██░░░░░▀▀▀▀▀▀▀░░░░░██▀▄░\033[1;32m  cat README.md\033[1;37m
█░░██░░░░░░░░░░░░░░░░░██░░░
█░░██░░░░░░░░░░░░░░░░░██░░█
█░░██░░░░░░░░░░░░░░░░░██░░█
█░░██░░░░░░░░░░░░░░░░░██░░█
█░░██░░░░░░░░░░░░░░░░░██░░█
█░░██▄░░░░░░░░░░░░░░░▄██░░█
▀▀▄█░█▄▄▄▄░░░░░░░▄▄▄▄█░█▄▀▀
░░░░░░░░░█▄▄▄▄▄▄▄█░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33mNo se pudo instalar\033[1;32m'{name}'
''')

  @classmethod
  def back(self):
    print ("""\033[01;32m 00) \033[1;33m Volver al menú""")
    print("")

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
\033[1;33m  [1] \033[1;32m Todas las herramientas.
\033[1;33m  [2] \033[1;32m Categorias.
\033[1;33m  [00] \033[1;32m Volver al menú.

''')
  @classmethod
  def exit(self):
    self.tool_header()
    print ('''\033[00m''')

