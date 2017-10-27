## Adding a GUI

If you want to, you could create a GUI (Graphical User Interface) to control your buggy.

![Buggy GUI forwards button](images/buggy-gui-forwards.png)

- With your other import statements, add a line of code to import features from the **guizero** library:

    ```python
    from guizero import App, PushButton
    ```

- Underneath your import statements, define a function called `forwards()`:

    ```python
    def forwards():
    ```

- Move your code to make the buggy move forwards so that it is __inside the function__. For Python to understand which code is inside the function, the code must be indented, like this:

    ```python
    def forwards():
        explorerhat.motor.one.forward(100)
        explorerhat.motor.two.forward(100)

        sleep(2)

        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
    ```

- Underneath your function, create the GUI app. The text "Buggy controller" will appear in the title bar - you can change this if you like.

    ```python
    app = App("Buggy controller")
    ```

- Now add a button to your GUI:

    ```python
    drive = PushButton(app, forwards, text="Forwards")
    ```

    Let's look at the code in more detail:
    - `drive =` - this is the variable name, so we can refer to the button
    - `PushButton` - tells Python to create a button using the PushButton class from guizero
    - `app` - adds this button to the app we just created
    - `forwards` - calls the function called forwards when the button is pressed
    - `text="Forwards"` - this text will be displayed on the button
    

- Finally, add the following line at the bottom of your program to display and update the GUI:

    ```python
    app.display()
    ```

- Save your program and press F5 to run it. You should see your GUI appear. Press the forwards button on the GUI and check that your robot moves forwards.

    ![Buggy GUI forwards button](images/buggy-gui-forwards.png)

    The full GUI code is [here](resources/buggygui.py) for you to look at if you wish.

