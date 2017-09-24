# Empezando a controlar pins con GPIO Zero

## Pins GPIO 

Al conjunto de pines que se encuentran a un lado de la Raspberry Pi se les llama pins GPIO (General-Purpose Input/Output) o Entradas y Salidas de Propósito General.

Estos pines permiten a la Raspberry controlar cosas en el mundo real. Puedes conectar componentes electrónicos a estos pines: estos componentes pueden ser de salida, como los LEDs (Diodos Emisores de Luz) que se pueden encender y apagar a voluntad, o componentes de entrada, como un botón o un sensor que puedes usar para disparar otros eventos. Por ejemplo, puedes encender un LED cada vez que detectes que un botón ha sido pulsado. 

Con la librería GPIO Zero, podrás controlar los pins GPIO de la Raspberry de manera sencilla. Hay 40 pins en la Raspberry Pi (26 en los modelos más antiguos) que permiten diferentes funciones.

La etiqueta de identificación RasPIO puede ayudarte a identificar cuál es el uso de cada pin. Asegúrate de que la etiqueta está colocada de manera que el pequeño agujero quede al lado de los puertos USB, ligeramente hacia afuera de la placa.

![](images/raspio-ports.jpg)

Si no tienes una etiqueta, esta guía puede ayudarte a identificar el número de cada pin.

![](images/pinout.png)

Verás que hay pins que están marcados con 3V3, 5V, GND y GP2, GP3, etc:
|     |     |     |
| --- | --- | --- |
|3V3|3.3 voltios|Cualquier cosa que conectes a estos pins recibirá un voltaje de 3.3V|
|5V|5 voltios|Cualquier cosa que conectes a estos pins recibirá un voltaje de 5V|
|GND|Tierra|Tierra o cero voltios, usado para cerrar el circuito.|
|GP2|GPIO pin 2|Estos pines son de propósito general y se pueden configurar como entrada o como salida
|ID_SC/ID_SD/DNC|Pins de propósito especial|

## Encender un LED
Prueba a conectar un LED a los pins de 3.3V y GND con una resistencia.

![](images/led-3v3.png)

El LED se debería encender. Siempre estará encendido, porque está conectado a un pin de 3.3 voltios.

Ahora prueba a moverlo del pin 3.3V al pin GPIO 17:

![](images/led-gpio17.png)

El LED ahora se debería apagar, pero como está conectado a un pin GPIO podemos controlarlo con código.

## Encendiendo y apagando un LED

GPIO Zero es una nueva librería de Python que proporciona una interfaz sencilla para interactuar con componentes a través de los pines GPIO
1. Abre Python 3 desde el menú principal

1. Puedes encender y apagar un LED tecleando comandos directamente en la ventana del intérprete de Python (también llamada Python shell). Vamos a hacerlo así primero, importando la librería GPIO Zero. También es necesario establecer qué pin GPIO es el que vamos a usar; en este caso será el 17.  Junto a los símbolos `>>>`, teclea:

	``` python
	from gpiozero import LED
	
	led = LED(17)
	```
Pulsa **Enter** en el teclado.

1. Para que hacer que el LED se encienda, escribe la siguiente línea y pulsa Enter:

	``` python
	led.on()
	```

1. Para apagar el LED puedes teclear:

	``` python
	led.off()
	```
	
## Haciendo parpadear el LED

Con la ayuda de la librería time y un pequeño bucle, podemos hacer que el LED parpadee.

1. Crea un nuevo archivo en **Archivo** > **Archivo nuevo**.
1. Guarda el archivo en **Archivo** > **Guardar**.
1. Guarda el archivo como `gpio_led.py`
1. Escribe el siguiente código para empezar:

	``` python
	from gpiozero import LED
	from time import sleep

	led = LED(17)

	while True:
		led.on()
		sleep(1)
		led.off()
		sleep(1)

	```
14. Guarda con **Ctrl + s** y ejecuta el código con **F5**.
15. El LED debería estar encendiéndose y apagándose continuamente. Para salir del programa pulsa **Ctrl + c** en el teclado.

## Usando los botones para tener una entrada
Ahora eres capaz de controlar un componente de salida, un LED. Vamos a conectar y controlar un componente de entrada: un botón.

1. Conecta un botón a un pin GND y a al pin 2 GPIO, como se muestra en el diagrama:

    ![](images/button.png)
	
1. Crea un nuevo archivo en **Archivo** > **Archivo nuevo**.
1. Guarda el archivo en **Archivo** > **Guardar**.
1. Guarda el archivo como `gpio_button.py`.

1. Esta vez necesitarás la clase Button (botón en inglés), y declarar que el botón estará en el pin 2. Escribe el siguiente código en tu archivo: 

	``` python
	from gpiozero import Button
	button = Button(2)
	```

1. Ahora puedes hacer que el programa haga algo cuando el botón esté pulsado. Prueba a añadir esta línea:

	``` python
	button.wait_for_press()
	print('Me has apretado')
	```

1. Guarda con **Ctrl + S** y ejecuta el código con **F5**.
1. Pulsa el botón y verás cómo tu texto aparece en pantalla.
 
## Controlando un LED manualmente

Ahora podemos combinar los dos programas que has escrito hasta ahora para controlar el LED usando el botón

1. Crea un nuevo archivo en **Archivo** > **Archivo nuevo**.
2. Guarda el archivo en **Archivo** > **Guardar**.
3. Guarda el archivo como `gpio_control.py`.
4. Ahora escribe el siguiente código:

	``` python
	from gpiozero import LED, Button
	from time import sleep

	led = LED(17)
	button = Button(2)

	button.wait_for_press()
	led.on()
	sleep(3)
	led.off()
	```

1. Guarda y ejecuta el programa. Cuando pulses el botón, el LED deberé encenderse durante 3 segundos.

## Haciendo un interruptor
Con un interruptor, pulsando el botón un avez deberá encender el LED, y con la siguiente pulsación el LED se volverá a apagar.

1. Modifica tu código para que quede como este. Estamos usando un flag llamado active para almacenar el estado del LED. La línea `active = not active` conmutará el LED entre los estados `True` y `False`:

	``` python
	from gpiozero import LED, Button
	from time import sleep

	led = LED(17)
	button = Button(2)
	active = False

	while True:
		if active == False:
			led.off()
		else:
			led.on()
		button.wait_for_press()
		button.wait_for_release()
		active = not active
	```

Estaría genial si pudieramos hacer que el LED se encendiera sólo cuando el botón está pulsado. Con la librería GPIO Zero, es bien sencillo.

1. Hay dos métodos de la clase Button llamados `when_pressed` y `when_released`. Estos métodos no bloquean el flujo del programa, así que si se colocan en un bucle, el programa se ejecutará indefinidamente. 

1. Modifica tu código para que quede como este:

	``` python
	from gpiozero import LED, Button
	from signal import pause

	led = LED(17)
	button = Button(2)

	button.when_pressed = led.on
	button.when_released = led.off

	pause()

	```
1. Guarda y ejecuta el programa. Ahora cuando el botón está pulsado, el LED se encenderá, y se volverá a apagar cuando el botón deje de estar pulsado. 

## Y ahora qué?

Hay muchas otras cosas que probar con GPIO Zero. Puedes echarle un vistazo a la documentación [aquí](https://gpiozero.readthedocs.org/).
Intenta controlar otros componentes como un zumbador, un LED RGD, un motor o un robot.
