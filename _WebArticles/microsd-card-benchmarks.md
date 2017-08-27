# microSD Card Benchmarks

_Captured: 2017-08-24 at 23:38 from [www.pidramble.com](http://www.pidramble.com/wiki/benchmarks/microsd-cards)_

In my experience, one of the highest-impact upgrades you can perform is to buy the fastest possible microSD card--especially for applications where you need to do a lot of random reads and writes.

There is an **order-of-magnitude difference** between most cheap cards and the slightly-more-expensive ones (even if both are rated as being in the same class)--especially in small-block random I/O performance. As an example, if you use a normal, cheap microSD card for your database server, normal database operations can literally be _100x slower_ than if you used a standard microSD card.

Because of this, I went and purchased over a dozen different cards and have been putting them through their paces. Here are the results of those efforts, in a nice tabular format:

## Rasbperry Pi model 2 B

Card Make/Model `hdparm` buffered `dd` write 4K rand read 4K rand write

[OWC Envoy SSD](https://eshop.macsales.com/shop/drive/enclosure-kits/OWC/Envoy) (USB) 64GB
34.13 MB/s
34.4 MB/s
7.06 MB/s
8.20 MB/s

[SanDisk Ultra Fit](https://www.amazon.com/SanDisk-Ultra-SDCZ43-032G-GAM46-Newest-Version/dp/B01BGTG41W/ref=as_li_ss_tl?ie=UTF8&qid=1467829411&sr=8-3&keywords=sandisk+ultra+fit&linkCode=ll1&tag=mmjjg-20&linkId=137ae38c9b22f9815c195d714f669627) (USB) 32GB
31.72 MB/s
14.5 MB/s
4.99 MB/s
1.07 MB/s

[Samsung Pro+](https://www.amazon.com/Samsung-Plus-MicroSDHC-Memory-Write/dp/B01273L37G/ref=as_li_ss_tl?ie=UTF8&qid=1467829450&sr=8-3&keywords=samsung+pro+&linkCode=ll1&tag=mmjjg-20&linkId=ced652b3c5e4cfaee029f75048d3ee59) 32GB
21.75 MB/s
18.7 MB/s
8.31 MB/s
1.75 MB/s

[Samsung Pro](https://www.amazon.com/Samsung-Class-Adapter-MB-MG32EA-AM/dp/B014W1ZKX4/ref=as_li_ss_tl?ie=UTF8&dpID=41Q+7HuVd0L&dpSrc=sims&preST=_AC_UL160_SR160,160_&psc=1&refRID=JBNRPWQNFDQHQ9ZQYG9B&linkCode=ll1&tag=mmjjg-20&linkId=4f7e155ea991185ef4b10a3ee2612b00) 16GB
18.39 MB/s
18.2 MB/s
7.66 MB/s
1.01 MB/s

[Samsung Evo+](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829489&sr=1-3&keywords=evo+&linkCode=ll1&tag=mmjjg-20&linkId=dbb3aff130ee0dede5197fca4c8fdb3f) 32GB
18.45 MB/s
14.0 MB/s
8.02 MB/s
3.00 MB/s

[Samsung Evo](https://www.amazon.com/Samsung-Class-Adapter-MB-MP16DA-AM/dp/B00IVPU7KE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829506&sr=1-12&keywords=evo&linkCode=ll1&tag=mmjjg-20&linkId=c5f192be2948687b3f939a4be2982117) 16GB
17.39 MB/s
10.4 MB/s
5.36 MB/s
1.05 MB/s

[SanDisk Extreme Pro](https://www.amazon.com/SDSDQXP-008G-X46-SanDisk-Extreme-MicroSDHC-Memory/dp/B008HK25BC/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829544&sr=1-6&keywords=extreme+pro+microsd&linkCode=ll1&tag=mmjjg-20&linkId=8bf4cbdcaf3cd0540cd2aae5540686d3) 8GB
18.43 MB/s
17.6 MB/s
7.52 MB/s
1.18 MB/s

[SanDisk Extreme](https://www.amazon.com/SanDisk-Extreme-microSDHC-Adapter-SDSQXNE-016G-GN6MA/dp/B013CP5F90/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829564&sr=1-1&keywords=extreme+microsd&linkCode=ll1&tag=mmjjg-20&linkId=6c0f8d2f599dd4587ea65768c3bdbc37) 16GB
18.51 MB/s
18.3 MB/s
8.10 MB/s
2.30 MB/s

[SanDisk Ultra](https://www.amazon.com/SanDisk-Ultra-Micro-Adapter-SDSQUNC-016G-GN6MA/dp/B010Q57SEE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829582&sr=1-5&keywords=sandisk+ultra+microsd&linkCode=ll1&tag=mmjjg-20&linkId=5054a4f20a2b93bd5ba00c015653bb8d) 16GB
17.73 MB/s
7.3 MB/s
5.34 MB/s
1.52 MB/s

[NOOBS](https://www.amazon.com/Raspberry-Pi-Preloaded-NOOBS-Card/dp/B00ENPQ1GK/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829621&sr=1-2&keywords=noobs+microsd&linkCode=ll1&tag=mmjjg-20&linkId=df31655186686fd98751002e636a8e8f) (1.4, C6) 8GB
17.62 MB/s
6.5 MB/s
5.63 MB/s
1.01 MB/s

[Transcend Premium 300x](https://www.amazon.com/dp/B00CES44EO/ref=as_li_ss_tl?_encoding=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=3bd2e9f06869dca27e15aed25cd05928) 32GB
18.14 MB/s
10.3 MB/s
5.21 MB/s
0.84 MB/s

[PNY Turbo](https://www.amazon.com/PNY-Turbo-Performance-MicroSDHC-P-SDU16GU190G-GE/dp/B00W77C2FA/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829679&sr=1-3&keywords=pny+turbo+microsd&linkCode=ll1&tag=mmjjg-20&linkId=65847985e0198424f880c0015edc0b51) (C10 90MB/s) 16GB
17.46 MB/s
TODO
6.25 MB/s
0.62 MB/s

[Toshiba](https://www.amazon.com/Toshiba-Micro-SDHC-Class-PFM008U-2DCK/dp/B00TQFMNIW/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829708&sr=1-8&keywords=toshiba+microsd+class+10&linkCode=ll1&tag=mmjjg-20&linkId=6df6c4ae1cdfe73f6efb5e6f6d91913e) (C10 40MB/s) 16GB
17.66 MB/s
11.2 MB/s
5.21 MB/s
0.21 MB/s

[Sony](https://www.amazon.com/Sony-Memory-SR16UY2A-TQ-VERSION/dp/B00X1404P8/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829730&sr=1-3&keywords=sony+microsd+class+10&linkCode=ll1&tag=mmjjg-20&linkId=dfe7fc71631a63cb0109f06a7a9a8654) (C10 70MB/s) 16GB
15.38 MB/s
8.9 MB/s
2.47 MB/s
0.24 MB/s

[Kingston](https://www.amazon.com/Kingston-Digital-microSDHC-SDC10G2-8GBSP/dp/B0166RR8OG/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829749&sr=1-2&keywords=kingston+microsd+class+10&linkCode=ll1&tag=mmjjg-20&linkId=db62e547e18662afebe0eef1862c47a4) (C10) 16GB
17.78 MB/s
9.0 MB/s
5.75 MB/s
0.21 MB/s

[Kingston](https://www.amazon.com/Kingston-Digital-microSDHC-SDC10G2-8GBSP/dp/B0166RR8OG/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829749&sr=1-2&keywords=kingston+microsd+class+10&linkCode=ll1&tag=mmjjg-20&linkId=db62e547e18662afebe0eef1862c47a4) (C10) 8GB
12.80 MB/s
7.2 MB/s
5.56 MB/s
0.17 MB/s

Nasya (C10) 16GB
16.05 MB/s
8.4 MB/s
2.28 MB/s
0.38 MB/s

No-name (C4) 4GB
13.37 MB/s
Sad
Painful
Excruciating

## Rasbperry Pi model 3 B

Card Make/Model `hdparm` buffered `dd` write 4K rand read 4K rand write

[Samsung Pro+](https://www.amazon.com/Samsung-Plus-MicroSDHC-Memory-Write/dp/B01273L37G/ref=as_li_ss_tl?ie=UTF8&qid=1467829450&sr=8-3&keywords=samsung+pro+&linkCode=ll1&tag=mmjjg-20&linkId=ced652b3c5e4cfaee029f75048d3ee59) 32GB
21.88 MB/s
20.2 MB/s
9.61 MB/s
2.16 MB/s

[Samsung Pro](https://www.amazon.com/Samsung-Class-Adapter-MB-MG32EA-AM/dp/B014W1ZKX4/ref=as_li_ss_tl?ie=UTF8&dpID=41Q+7HuVd0L&dpSrc=sims&preST=_AC_UL160_SR160,160_&psc=1&refRID=JBNRPWQNFDQHQ9ZQYG9B&linkCode=ll1&tag=mmjjg-20&linkId=4f7e155ea991185ef4b10a3ee2612b00) 16GB
21.62 MB/s
22.1 MB/s
9.41 MB/s
1.66 MB/s

[Samsung Evo+](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829489&sr=1-3&keywords=evo+&linkCode=ll1&tag=mmjjg-20&linkId=dbb3aff130ee0dede5197fca4c8fdb3f) 32GB
21.77 MB/s
15.8 MB/s
9.66 MB/s
3.43 MB/s

[Samsung Evo Select](https://www.amazon.com/gp/product/B01DOB6Y5Q/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=9ccf2847b17522d793023573679917f1) 32GB
19.59 MB/s
5.7 MB/s
4.34 MB/s
0.71 MB/s

[Samsung Evo](https://www.amazon.com/Samsung-Class-Adapter-MB-MP16DA-AM/dp/B00IVPU7KE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829506&sr=1-12&keywords=evo&linkCode=ll1&tag=mmjjg-20&linkId=c5f192be2948687b3f939a4be2982117) 16GB
20.08 MB/s
10.4 MB/s
6.02 MB/s
1.02 MB/s

[SanDisk Extreme Pro](https://www.amazon.com/SDSDQXP-008G-X46-SanDisk-Extreme-MicroSDHC-Memory/dp/B008HK25BC/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829544&sr=1-6&keywords=extreme+pro+microsd&linkCode=ll1&tag=mmjjg-20&linkId=8bf4cbdcaf3cd0540cd2aae5540686d3) 8GB
21.02 MB/s
21.2 MB/s
9.07 MB/s
1.25 MB/s

[SanDisk Extreme](https://www.amazon.com/SanDisk-Extreme-microSDHC-Adapter-SDSQXNE-016G-GN6MA/dp/B013CP5F90/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829564&sr=1-1&keywords=extreme+microsd&linkCode=ll1&tag=mmjjg-20&linkId=6c0f8d2f599dd4587ea65768c3bdbc37) 16GB
22.08 MB/s
21.8 MB/s
9.44 MB/s
2.42 MB/s

[SanDisk Ultra](https://www.amazon.com/SanDisk-Ultra-Micro-Adapter-SDSQUNC-016G-GN6MA/dp/B010Q57SEE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829582&sr=1-5&keywords=sandisk+ultra+microsd&linkCode=ll1&tag=mmjjg-20&linkId=5054a4f20a2b93bd5ba00c015653bb8d) 16GB
20.79 MB/s
7.9 MB/s
5.98 MB/s
1.57 MB/s

## Rasbperry Pi model 3 B results - overclocked microSD

You can double the microSD card reader's speed by adding an extra `dtoverlay` configuration inside `/boot/config.txt` (for instructions, see [How to overclock the microSD card reader in the Raspberry Pi 3](http://www.jeffgeerling.com/blog/2016/how-overclock-microsd-card-reader-on-raspberry-pi-3)).

Card Make/Model `hdparm` buffered `dd` write 4K rand read 4K rand write

[Samsung Pro+](https://www.amazon.com/Samsung-Plus-MicroSDHC-Memory-Write/dp/B01273L37G/ref=as_li_ss_tl?ie=UTF8&qid=1467829450&sr=8-3&keywords=samsung+pro+&linkCode=ll1&tag=mmjjg-20&linkId=ced652b3c5e4cfaee029f75048d3ee59) 32GB
39.93 MB/s
31.0 MB/s
12.15 MB/s
1.84 MB/s

[Samsung Pro](https://www.amazon.com/Samsung-Class-Adapter-MB-MG32EA-AM/dp/B014W1ZKX4/ref=as_li_ss_tl?ie=UTF8&dpID=41Q+7HuVd0L&dpSrc=sims&preST=_AC_UL160_SR160,160_&psc=1&refRID=JBNRPWQNFDQHQ9ZQYG9B&linkCode=ll1&tag=mmjjg-20&linkId=4f7e155ea991185ef4b10a3ee2612b00) 16GB1
31.59 MB/s
32.8 MB/s
11.20 MB/s
1.48 MB/s

[Samsung Evo+](https://www.amazon.com/Samsung-Class-Micro-Adapter-MB-MC32DA/dp/B00WR4IJBE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829489&sr=1-3&keywords=evo+&linkCode=ll1&tag=mmjjg-20&linkId=dbb3aff130ee0dede5197fca4c8fdb3f) 32GB
37.68 MB/s
20.0 MB/s
12.20 MB/s
3.75 MB/s

[Samsung Evo Select](https://www.amazon.com/gp/product/B01DOB6Y5Q/ref=as_li_ss_tl?ie=UTF8&psc=1&linkCode=ll1&tag=mmjjg-20&linkId=9ccf2847b17522d793023573679917f1) 32GB
24.56 MB/s
13.2 MB/s
4.69 MB/s
0.82 MB/s

[Samsung Evo](https://www.amazon.com/Samsung-Class-Adapter-MB-MP16DA-AM/dp/B00IVPU7KE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829506&sr=1-12&keywords=evo&linkCode=ll1&tag=mmjjg-20&linkId=c5f192be2948687b3f939a4be2982117) 16GB
32.47 MB/s
11.8 MB/s
6.44 MB/s
1.25 MB/s

[SanDisk Extreme Pro](https://www.amazon.com/SDSDQXP-008G-X46-SanDisk-Extreme-MicroSDHC-Memory/dp/B008HK25BC/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829544&sr=1-6&keywords=extreme+pro+microsd&linkCode=ll1&tag=mmjjg-20&linkId=8bf4cbdcaf3cd0540cd2aae5540686d3) 8GB
40.52 MB/s
35.9 MB/s
11.31 MB/s
1.28 MB/s

[SanDisk Extreme](https://www.amazon.com/SanDisk-Extreme-microSDHC-Adapter-SDSQXNE-016G-GN6MA/dp/B013CP5F90/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829564&sr=1-1&keywords=extreme+microsd&linkCode=ll1&tag=mmjjg-20&linkId=6c0f8d2f599dd4587ea65768c3bdbc37) 16GB
40.88 MB/s
39.1 MB/s
11.77 MB/s
2.36 MB/s

[SanDisk Ultra](https://www.amazon.com/SanDisk-Ultra-Micro-Adapter-SDSQUNC-016G-GN6MA/dp/B010Q57SEE/ref=as_li_ss_tl?s=pc&ie=UTF8&qid=1467829582&sr=1-5&keywords=sandisk+ultra+microsd&linkCode=ll1&tag=mmjjg-20&linkId=5054a4f20a2b93bd5ba00c015653bb8d) 16GB
37.41 MB/s
8.5 MB/s
6.71 MB/s
1.61 MB/s

1 The Samsung Pro refused to overclock to 100 MHz; I could only overclock at 80 MHz reliably.

## Benchmarks

All the benchmarks can be run quickly and easily by running a shell script in the Raspberry Pi Dramble repository:
    
    
    curl https://raw.githubusercontent.com/geerlingguy/raspberry-pi-dramble/master/setup/benchmarks/microsd-benchmarks.sh | sudo bash

### `hdparm` buffered
    
    
    sudo hdparm -t /dev/mmcblk0

Rationale: `hdparm` gives basic raw throughput stats for buffered reads (by the disk/device itself). You could also test with `-T` instead of `-t` to test the OS filesystem cache performance (which allows the OS to dramatically speed up certain read operations), but for our purposes we just want to test the device itself.

Setup:

  1. Install hdparm: `sudo apt-get install -y hdparm`

### `dd` write
    
    
    sudo dd if=/dev/zero of=/home/pi/test bs=8k count=50k conv=fsync; sudo rm -f /home/pi/test

Rationale: `dd` simply copies data from one place (`if`) to another (`of`). If your filesystem caches are big enough, this is a pretty poor disk speed comparison test. Because of that, make sure that `count` is set to a parameter large enough to cause the OS to actually write data to the drive (e.g. `50k` `8k` blocks ~= 400 MB, which shouldn't be able to be cached on a microSD card in a Pi!.

### `iozone` 4K Random read/write
    
    
    iozone -e -I -a -s 100M -r 4k -i 0 -i 1 -i 2 [-f /path/to/file]

Rationale: `iozone` is a very robust filesystem benchmark tool, which does a lot of useful tests that make sure you're getting a broad overview of read and write performance for a variety of block sizes and situations. I like the lower block size random I/O tests especially, because many operations (like logging data, writing a row to an ACID-compliant database, or bulk loading of data) require as fast of small-block-size random I/O as possible.

Most cheap microSD cards, even if rated as being 100MB/sec+ class 10 cards, can't sustain anywhere near that rate when writing random data--especially on the Raspberry Pi's measly data bus. (Note that most of the above benchmarks, when run on a USB 3.0 card reader on my MacBook Air, show 5, 10, or 15 times greater performance in that environment).

Setup:

  1. Download the [latest version](http://www.iozone.org/): `wget http://www.iozone.org/src/current/iozone3_434.tar`
  2. Expand the tarfile: `cat iozone3_434.tar | tar -x`
  3. Go into the `src` folder: `cd iozone3_434/src/current`
  4. Build the executable: `make linux-arm`
  5. Symlink the executable into your local bin folder: `sudo ln -s /home/pi/iozone_434/src/current/iozone /usr/local/bin/iozone`
