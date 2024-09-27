Este es un script de Python que realiza ataques de fuerza bruta simples para descifrar contraseñas. Utiliza un diccionario de contraseñas o genera combinaciones de caracteres para probarlas contra una función de autenticación.
⚠️ Advertencia: Este programa debe ser utilizado únicamente con fines educativos o en entornos controlados donde tengas permiso explícito para realizar pruebas de seguridad.

**Características**
Soporte para ataques de fuerza bruta utilizando un diccionario de contraseñas.
Generación de combinaciones de caracteres (si no se usa un diccionario).
Configurable para atacar diferentes tipos de autenticación (por ejemplo, hash de contraseñas).

**Instalación**
Clona este repositorio en tu máquina local:
bash
Copiar código
git clone https://github.com/tuusuario/password-cracker.git
Navega al directorio del proyecto:
bash
Copiar código
cd password-cracker
Instala las dependencias necesarias (si las hay) con:
bash
Copiar código
pip install -r requirements.txt
Uso
Asegúrate de tener un archivo de diccionario de contraseñas (passwords.txt) o define las reglas de generación de contraseñas dentro del script.
Ejecuta el programa:
bash
Copiar código
python password_cracker.py
Opciones de uso:
--dict para especificar un archivo de diccionario.
--hash para especificar el hash de la contraseña a atacar.
Ejemplo:
bash
Copiar código
python password_cracker.py --dict passwords.txt --hash <hash_a_descifrar>
Uso Ético
Este proyecto debe ser utilizado únicamente para propósitos educativos o pruebas en sistemas donde se tiene autorización explícita. El uso malintencionado de este script para comprometer la seguridad de sistemas sin permiso es ilegal y contrario a los principios de ciberseguridad.

Contribuciones
Las contribuciones son bienvenidas. Si tienes ideas o mejoras para el proyecto, no dudes en hacer un fork y enviar un pull request.

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
