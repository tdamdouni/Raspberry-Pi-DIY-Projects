# HyperPixel touchscreen radio

_Captured: 2017-12-10 at 15:08 from [www.suppertime.co.uk](http://www.suppertime.co.uk/blogmywiki/2017/12/hyperpixel-touchscreen-radio/)_

I just got a [HyperPIxel Raspberry Pi touch-screen LCD display from Pimoroni.](https://shop.pimoroni.com/products/hyperpixel) This neat display is the same size as the Raspberry Pi itself, and covers all its GPIO pins but it is a touchscreen and it does shift 800×480 pixel video at 60 frames a second. I have plans to do something with a camera and this screen, but as a first project I fell back to my standard: can I make a radio from it?

Being a touch screen, some kind of GUI would be a good idea, and the project I hacked together gave me an excuse to play with Tkinter, the default, but far from ideal, GUI toolkit that Python has installed by default.

I had problems getting the HyperPixel to work at first - I had to do a clean install of Raspbian Jesse, presumably because some other project was interfering with some of the GPIO pins.

First I installed mpc and mpd which I use on the Raspberry Pi to play radio streams or mp3 files:

`sudo apt-get install mpc mpd`

If you've not used mpc before, open the mpd config file with nano like this:  
`sudo nano /etc/mpd.conf`

Then edit these lines to remove some # signs (uncomment) and change the mixer_type from hardware to software so it looks like this:

`audio_output {  
type "alsa"  
name "My ALSA Device"  
device "hw:0,0" # optional  
mixer_type "software" # optional  
mixer_device "default" # optional  
mixer_control "PCM" # optional  
mixer_index "0" # optional  
}`

Now add some radio station URLs using the `mpc add` command. I added BBC 6music, BBC World Service News, FIP, Radio 4 and others. For example to add FIP I typed  
`mpc add http://chai5she.cdn.dvmr.fr/fip-midfi.mp3`

You can find BBC radio URLs on [my big list here](http://www.suppertime.co.uk/blogmywiki/2015/04/updated-list-of-bbc-network-radio-urls/).

I added 7 stations but you can add more or fewer. They get added in order but you can check your playlist of stations or MP3 files by typing  
`mpc playlist`

And you can change the order using the move command, for example to move station 4 to preset 2 just type:  
`mpc move 4 2`

I then made some 100×100 pixel GIF images (see end of post) for the station logos and wrote some Python/Tkinter code to display the buttons to play each station, a stop/pause button and one to exit the app as it runs full screen. The volume buttons don't work on my installation for some reason I haven't fathomed yet.

You could add loads of extras to this like weather and news headlines - or 'now playing' information using [the frankly mad workaround I used on my web-interface radio back in 2014](http://www.suppertime.co.uk/blogmywiki/2014/10/raspberry-pi-internet-radio-with-web-interface/) (it's harder than you'd think!)

I **did** add a digital clock, which accounts for the cut-and-shunt abomination of Python code you see below. If someone can make it more elegant, I'd be highly delighted. It does, however, work.
    
    
    from tkinter import Tk, Label, Button, E, W, PhotoImage
    import os, time
    
    class MyFirstGUI:
        def __init__(self, master):
            global fiplogo
            self.master = master
            master.title("HyperPixelRadio")
    
            fiplogo = PhotoImage(file="fip100.gif")
    
            self.label = Label(master, text="HyperPixel Radio by @blogmywiki", font=('Roboto',25), fg = 'blue')
            self.label.grid(columnspan=7, pady=20)
    
            self.fip_button = Button(master, image=fiplogo, command=self.fip, height=100, width = 100)
            self.fip_button.image = fiplogo
            self.fip_button.grid(row=1, pady=10)
    
            r2logo = PhotoImage(file="radio2.gif")
            self.r2_button = Button(master, image=r2logo, command=self.r2, height=100, width = 100)
            self.r2_button.image = r2logo
            self.r2_button.grid(row=1, column=1)
    
            r4logo = PhotoImage(file="radio4.gif")
            self.r4_button = Button(master, image=r4logo, command=self.r4, height=100, width = 100)
            self.r4_button.image = r4logo
            self.r4_button.grid(row=1, column=2)
    
            x4logo = PhotoImage(file="4extra.gif")
            self.x4_button = Button(master, image=x4logo, command=self.x4, height=100, width = 100)
            self.x4_button.image = x4logo
            self.x4_button.grid(row=1, column=3)
    
            r5logo = PhotoImage(file="5live.gif")
            self.r5_button = Button(master, image=r5logo, command=self.r5, height=100, width = 100)
            self.r5_button.image = r5logo
            self.r5_button.grid(row=1, column=4)
    
            r6logo = PhotoImage(file="6music.gif")
            self.r6music_button = Button(master, image=r6logo, command=self.r6music, height=100, width = 100)
            self.r6music_button.image = r6logo
            self.r6music_button.grid(row=1, column=5)
    
            wslogo = PhotoImage(file="bbcws.gif")
            self.ws_button = Button(master, image=wslogo, command=self.ws, height=100, width = 100)
            self.ws_button.image = wslogo
            self.ws_button.grid(row=1, column=6)
    
            self.down_button = Button(master, text="< VOL", command=self.down, height=5, width=10)
            self.down_button.grid(row=3)
    
            self.stop_button = Button(master, text="STOP", command=self.stop, height=5, width = 10)
            self.stop_button.grid(row=3, column=2)
    
            self.close_button = Button(master, text="close app", command=self.close, height=5, width=10)
            self.close_button.grid(row=3, column=4)
    
            self.up_button = Button(master, text="VOL >", command=self.up, height=5, width=10)
            self.up_button.grid(row=3, column=6)
    
        def fip(self):
            print("fip!")
            self.label.config(text='fip - France Inter Paris')
            os.system("mpc play 1")
    
        def r4(self):
            print("BBC Radio 4 FM")
            self.label.config(text='BBC Radio 4 FM')
            os.system("mpc play 2")
    
        def x4(self):
            print("BBC Radio 4 Extra")
            self.label.config(text='BBC Radio 4 Extra')
            os.system("mpc play 7")
    
        def r6music(self):
            print("BBC 6music")
            self.label.config(text='BBC Radio 6Music')
            os.system("mpc play 3")
    
        def ws(self):
            print("BBC World Service News Stream")
            self.label.config(text='BBC World Service News')
            os.system("mpc play 4")
    
        def r2(self):
            print("BBC Radio 2")
            self.label.config(text='BBC Radio 2')
            os.system("mpc play 5")
    
        def r5(self):
            print("BBC Radio 5 Live")
            self.label.config(text='BBC Radio 5 Live')
            os.system("mpc play 6")
    
        def stop(self):
            print("stop MPC player")
            self.label.config(text='-paused-')
            os.system("mpc stop")
    
        def close(self):
            os.system("mpc stop")
            root.destroy()
    
        def up(self):
            os.system("mpc volume +30")
    
        def down(self):
            os.system("mpc volume -30")
    
    root = Tk()
    
    #root.geometry('720x480')
    #root.configure(background='cyan3')
    root.attributes('-fullscreen', True)
    my_gui = MyFirstGUI(root)
    
    time1 = ''
    clock = Label(root, font=('Roboto', 48, 'bold'))
    clock.grid(row=4, columnspan=7, pady=20)
    def tick():
        global time1
        # get the current local time from the PC
        time2 = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        clock.after(200, tick)
    tick()
    
    root.mainloop()
    
