**Password Cracker - Fuerza Bruta en Python**

**Descripción**
Este proyecto contiene tres scripts en Python que realizan ataques de fuerza bruta simples para adivinar contraseñas. Cada script emplea un enfoque diferente, desde la adivinación de contraseñas con caracteres alfabéticos hasta contraseñas numéricas mediante búsqueda secuencial o aleatoria.

⚠️ **Advertencia:** Estos scripts deben utilizarse con fines educativos o en entornos controlados donde tengas autorización explícita para realizar pruebas de seguridad. El uso no autorizado de técnicas de cracking es ilegal.

**Scripts Incluidos**
1. Adivinación de Contraseñas con Caracteres Minúsculas: Este script intenta adivinar una contraseña compuesta por caracteres alfanuméricos en minúscula (a-z, 0-9). Usa combinaciones aleatorias hasta que adivina la longitud y el contenido de la contraseña ingresada.

**Ejecución:**
python cracker_alpha.py
El script solicita la contraseña como entrada, y luego prueba diferentes combinaciones aleatorias hasta encontrarla.

Ejemplo de uso:
Ingresá la contraseña: clave123
La contraseña es clave123

2. Adivinación Secuencial de Contraseñas Numéricas: Este script realiza un ataque de fuerza bruta secuencial, incrementando el número hasta encontrar la contraseña numérica ingresada.

Ejecución:
python cracker_secuencial.py
El script solicita una contraseña numérica como entrada y prueba todas las combinaciones desde 0 hasta el número ingresado.

Ejemplo de uso:
Input a number that is a password: 1234
La contraseña es 1234

3. Adivinación Aleatoria de Contraseñas Numéricas: Este script intenta adivinar contraseñas numéricas generando valores aleatorios dentro del rango 0 a 999999.

Ejecución:
python cracker_aleatorio.py
El script pide una contraseña numérica e intenta adivinarla mediante números aleatorios generados hasta que encuentra la correcta.

Ejemplo de uso:
Contraseña: 56789
La contraseña es 56789

**Requisitos**
Este proyecto requiere la instalación de Python 3.x. No es necesario instalar bibliotecas adicionales, ya que se utilizan solo bibliotecas estándar como random.

**Instalación**
Clona este repositorio en tu máquina local:
git clone https://github.com/natuska26/password-cracker.git

Navega al directorio del proyecto:
cd password-cracker

**Uso**
Para ejecutar los scripts, simplemente utiliza python seguido del nombre del script. Asegúrate de ingresar contraseñas que sigan el formato esperado por cada script (alfanuméricas minúsculas o numéricas).

**Uso Ético**
Este software está destinado a fines educativos y para probar la seguridad de sistemas propios o de terceros con autorización explícita. El uso malicioso para vulnerar sistemas sin consentimiento está prohibido y es ilegal.

**Licencia**
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

