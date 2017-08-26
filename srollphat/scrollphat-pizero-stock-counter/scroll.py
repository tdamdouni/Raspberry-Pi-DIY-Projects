import scrollphat

class scroll:
    def __init__(self, brightness):
        scrollphat.set_brightness(brightness)
        scrollphat.clear()
        scrollphat.update()

    def show(self, total):
        val = total
        if total > 999:
            val = 999
        scrollphat.write_string(str(val))
