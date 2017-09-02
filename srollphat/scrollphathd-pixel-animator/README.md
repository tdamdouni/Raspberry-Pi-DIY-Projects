# scrollphathd-pixel-animator
*Renders (really low-res) videos with the [Pimoroni Scroll pHat HD](https://github.com/pimoroni/scroll-phat-hd) LED matrix using python*

This example script shows how an array of several frames of matrix brightness values are used to display animations, such as this [candle animation](https://youtu.be/Bzze-ceYA8c). Run it on your Raspberry Pi Zero (W) as you would run other Scroll pHAT HD scripts.

## 1. How to generate the array files

You may need some manual work to animate your own video, but I hope that these steps help along. 

To generate these files you can use [ASCII-Video](https://github.com/fossage/ASCII-Video). That project allows you to take a video and render it as ASCII characters, in our case as brightness values to control the LED brightness of the scrollphat matrix. Important, before generating the output file you need to adjust the javascript files by:

- editing the contained ImageToAscii command to apply a pixel array with numbers so that scrollphat can render them as numbers rather than characters
- disabling the coloration to generate just the brightness values
- setting the pxWidth and size_options to control the output size

The command I ended up using looks like this:
```
    imageToAscii(tmpDirPath + files[idx], {
		pxWidth: 2,
		size_options: {
			screen_size: {
				height: 17
			},
			px_size: {
				width: 0.8,
				height: 1	
			},
			fit_screen: false
		},
		colored: false,
		pixels: ['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020','021','022','023','024','025','026','027','028','029','030','031','032','033','034','035','036','037','038','039','040','041','042','043','044','045','046','047','048','049','050','051','052','053','054','055','056','057','058','059','060','061','062','063','064','065','066','067','068','069','070','071','072','073','074','075','076','077','078','079','080','081','082','083','084','085','086','087','088','089','090','091','092','093','094','095','096','097','098','099','100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122','123','124','125','126','127','128','129','130','131','132','133','134','135','136','137','138','139','140','141','142','143','144','145','146','147','148','149','150','151','152','153','154','155','156','157','158','159','160','161','162','163','164','165','166','167','168','169','170','171','172','173','174','175','176','177','178','179','180','181','182','183','184','185','186','187','188','189','190','191','192','193','194','195','196','197','198','199','200','201','202','203','204','205','206','207','208','209','210','211','212','213','214','215','216','217','218','219','220','221','222','223','224','225','226','227','228','229','230','231','232','233','234','235','236','237','238','239','240','241','242','243','244','245','246','247','248','249','250','251','252','253','254','255'], 
      image_type: 'jpg'
    }
```
instead of:
```
imageToAscii(tmpDirPath + files[idx], {
      image_type: 'jpg'
    }
```
With the resulting output file you can display your own animation.

## 2. How to use them to display the animation

Take a look at the provided example candle_example.py, and use it as template. You need to take care that the Array size corresponds to the pixel size of the LED matrix, particularly when regarding the indexes for accessing the array and the scrollphat set_pixel command. Remember that the LED matrix is 7 pixels high times 17 pixels wide.

## 3. Things to consider

- The input video should have a reasonable number of frames. You can clip the video to the required number of frames by using VLC, for example. The provided examples has 333 frames
- The input video should have a reasonable size to fit in the LED matrix. You can use an online tool to crop your video such as [this](https://ezgif.com/crop-video) one.
- By resizing the command line window of ASCII-Video you can affect the size of the generated array, so try to tweak the window size so that the resulting array size corresponds to the size of the LED matrix (17x7 pixels). Alternatively use the size_option of the image-to-ascii command to control the output size more precisely as shown above.
