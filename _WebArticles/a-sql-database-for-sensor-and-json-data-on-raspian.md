# A SQL database for sensor and JSON data on Raspian

_Captured: 2017-07-30 at 15:57 from [www.raspberrypi.org](https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=97199&p=674959)_

Preface:

This post is the introductionary part in a little how-to series on how to use the IBM Informix database on the Raspberry Pi to build an efficient sensor data data database for local sensor data analytics/processing/caching.

The other posts can be found here:  
[viewtopic.php?f=37&t=97772&p=678497](https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=97772&p=678497) (An Informix Sensor DB - Part 1)  
[viewtopic.php?f=37&t=100029&p=693935](https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=100029&p=693935) (An Informix Sensor DB - Part 2)  
[viewtopic.php?f=37&t=137392&p=912405](https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=137392&p=912405) (The Informix REST API - Part 3)  
[viewtopic.php?uid=131887&f=37&t=140398](https://www.raspberrypi.org/forums/viewtopic.php?uid=131887&f=37&t=140398) (Round robin sensor data storage with IBM Informix - Part 4)

Hi,

I am not sure if the following might be appropriate to be posted here, but I suppose it might be of interest for the Raspberry Pi community:

IBM has just released a free developer edition of its Informix SQL database for ARM v6 (and ARM v7) and hence its available for the Raspberry Pi (it supports Raspian but might run on similar Linux distributions as well).

Informix has built-in optimized support for time series (sensor-) based data plus JSON plus Geospatial data. Its an object-relational SQL database and supports all major development APIs (eg. JDBC, REST API, MongoDB API, ODBC, .NET etc.).  
That free developer version can be downloaded from here: [https://www14.software.ibm.com/webapp/i ... rce=ifxids](https://www14.software.ibm.com/webapp/iwm/web/reg/pick.do?source=ifxids).

To get you started on the built-in time series/sensor data capabilities, you might want to take a look at the following IBM DeveloperWorks article: [http://www.ibm.com/developerworks/data/ ... timeseries](http://www.ibm.com/developerworks/data/library/techarticle/dm-1203timeseries) and/or take a look at the following free IBM RedBook on that topic: [http://www.redbooks.ibm.com/abstracts/s ... .html?Open](http://www.redbooks.ibm.com/abstracts/sg248021.html?Open).

Finally, here is the link to the official documentation: [http://www-01.ibm.com/support/knowledge ... tm?lang=en](http://www-01.ibm.com/support/knowledgecenter/SSGU8G_12.1.0/com.ibm.welcome.doc/welcome.htm?lang=en).

If you might have any questions, please feel free to get in touch with me by sending a PM.

\- Alexander

PS: If you want to follow me on Twitter: <http://twitter.com/AlexKoeMUC>
