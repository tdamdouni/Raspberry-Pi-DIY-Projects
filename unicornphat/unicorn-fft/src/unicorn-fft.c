#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h> // for memset
#include <fftw3.h>
#include <math.h>

#define CHUNK 1024
#define SAMPLE_RATE 44100
#define BINS 8

// unicorn hat
#include "ws2811.h"
#include "board_info.h"
#include <signal.h>

#define LED_COUNT 64

ws2811_t unicorn = {
	.freq = WS2811_TARGET_FREQ,
	.dmanum = 5,
	.channel = {
		[0] = {
			.gpionum    = 18,
			.count      = LED_COUNT,
			.invert     = 0,
			.brightness = 50
		}
	}
};
const int ledmap[8][8] = {
	{7 ,6 ,5 ,4 ,3 ,2 ,1 ,0 },
	{8 ,9 ,10,11,12,13,14,15},
	{23,22,21,20,19,18,17,16},
	{24,25,26,27,28,29,30,31},
	{39,38,37,36,35,34,33,32},
	{40,41,42,43,44,45,46,47},
	{55,54,53,52,51,50,49,48},
	{56,57,58,59,60,61,62,63}
};
void setBrightness(int b) {
	unicorn.channel[0].brightness = b;
}
void setPixelColorRGB(int pixel, uint8_t r, uint8_t g, uint8_t b) {
	unicorn.channel[0].leds[pixel] = (r << 16) | (g << 8) | b;
}
int getPixelPosition(int x, int y) {
	y = 7-y;
	x = 7-x;
	return ledmap[x][y];
}
void showLED() {
	ws2811_render(&unicorn);
}
void clearLED() {
	int i;
	for (i=0; i < LED_COUNT; i++){
		setPixelColorRGB(i, 0, 0, 0);
	}
}
void unicorn_exit(int status) {
	clearLED();
	ws2811_render(&unicorn);
	ws2811_fini(&unicorn);

	exit(status);
}

void hsv2rgb(float h, float s, float v, float *r, float *g, float *b) {

	int i;
	float f, p, q, t;

	// Wrap hue
	if(h < 0.0 || h > 1.0){
		h=fabsf(fmodf(h,1.0));
	}

	h *= 360.0;
	h /= 60.0;

	i = floor( h );
	f = h - i;
	p = (v * ( 1 - s ));
	q = (v * ( 1 - s * f ));
	t = (v * ( 1 - s * ( 1 - f ) ));

	switch( i ){
		case 0:
			*r = v;
			*g = t;
			*b = p;
			break;
		case 1:
			*r = q;
			*g = v;
			*b = p;
			break;
		case 2:
			*r = p;
			*g = v;
			*b = t;
			break;
		case 3:
			*r = p;
			*g = q;
			*b = v;
			break;
		case 4:
			*r = t;
			*g = p;
			*b = v;
			break;
		default:
			*r = v;
			*g = p;
			*b = q;
			break;
	}
}


void ledbar(int pos, double value, float r, float g, float b) {
	double height = value*8.0;
	int i;
	for (i = 0; i < 8; i++) {
		double brightness = 1.0;
		if (i == (int)height) {
			brightness = fmod(height, 1.0);
		} else if (i > (int)height) {
			brightness = 0.0;
		}

		// uncomment for a green-yellow-red visualization
		//hsv2rgb(((7-i)/8.0)*0.3, 1.0, brightness, &r, &g, &b);

		setPixelColorRGB(getPixelPosition(pos, i), r*brightness*255, g*brightness*255, b*brightness*255);
	}
}
// end of unicorn hat


// from impulse. I have no idea how these numbers were generated
// https://github.com/ianhalpern/Impulse/blob/master/src/Impulse.c#L30
const long fft_max[] = { 12317168L, 7693595L, 5863615L, 4082974L, 5836037L, 4550263L, 3377914L, 3085778L, 3636534L, 3751823L, 2660548L, 3313252L, 2698853L, 2186441L, 1697466L, 1960070L, 1286950L, 1252382L, 1313726L, 1140443L, 1345589L, 1269153L, 897605L, 900408L, 892528L, 587972L, 662925L, 668177L, 686784L, 656330L, 1580286L, 785491L, 761213L, 730185L, 851753L, 927848L, 891221L, 634291L, 833909L, 646617L, 804409L, 1015627L, 671714L, 813811L, 689614L, 727079L, 853936L, 819333L, 679111L, 730295L, 836287L, 1602396L, 990827L, 773609L, 733606L, 638993L, 604530L, 573002L, 634570L, 1015040L, 679452L, 672091L, 880370L, 1140558L, 1593324L, 686787L, 781368L, 605261L, 1190262L, 525205L, 393080L, 409546L, 436431L, 723744L, 765299L, 393927L, 322105L, 478074L, 458596L, 512763L, 381303L, 671156L, 1177206L, 476813L, 366285L, 436008L, 361763L, 252316L, 204433L, 291331L, 296950L, 329226L, 319209L, 258334L, 388701L, 543025L, 396709L, 296099L, 190213L, 167976L, 138928L, 116720L, 163538L, 331761L, 133932L, 187456L, 530630L, 131474L, 84888L, 82081L, 122379L, 82914L, 75510L, 62669L, 73492L, 68775L, 57121L, 94098L, 68262L, 68307L, 48801L, 46864L, 61480L, 46607L, 45974L, 45819L, 45306L, 45110L, 45175L, 44969L, 44615L, 44440L, 44066L, 43600L, 57117L, 43332L, 59980L, 55319L, 54385L, 81768L, 51165L, 54785L, 73248L, 52494L, 57252L, 61869L, 65900L, 75893L, 65152L, 108009L, 421578L, 152611L, 135307L, 254745L, 132834L, 169101L, 137571L, 141159L, 142151L, 211389L, 267869L, 367730L, 256726L, 185238L, 251197L, 204304L, 284443L, 258223L, 158730L, 228565L, 375950L, 294535L, 288708L, 351054L, 694353L, 477275L, 270576L, 426544L, 362456L, 441219L, 313264L, 300050L, 421051L, 414769L, 244296L, 292822L, 262203L, 418025L, 579471L, 418584L, 419449L, 405345L, 739170L, 488163L, 376361L, 339649L, 313814L, 430849L, 275287L, 382918L, 297214L, 286238L, 367684L, 303578L, 516246L, 654782L, 353370L, 417745L, 392892L, 418934L, 475608L, 284765L, 260639L, 288961L, 301438L, 301305L, 329190L, 252484L, 272364L, 261562L, 208419L, 203045L, 229716L, 191240L, 328251L, 267655L, 322116L, 509542L, 498288L, 341654L, 346341L, 451042L, 452194L, 467716L, 447635L, 644331L, 1231811L, 1181923L, 1043922L, 681166L, 1078456L, 1088757L, 1221378L, 1358397L, 1817252L, 1255182L, 1410357L, 2264454L, 1880361L, 1630934L, 1147988L, 1919954L, 1624734L, 1373554L, 1865118L, 2431931L, 2431931L };

int16_t buffer[ CHUNK / 2];
double magnitude[ CHUNK / 4 + 1];
double bands[12];
double bins[ BINS ];
double smoothbins[ BINS ];
double bandwidth = (2.0f/(CHUNK/2.0f)) * (SAMPLE_RATE / 2.0f);

// each bar has a defined hue
int hues[ BINS ] = {0, 35, 60, 120, 170, 240, 280, 310};


// function from https://github.com/rm-hull/raspberry-vu which is a fork of https://github.com/ianhalpern/Impulse
void getFFT() {
	double *in;
	fftw_complex *out;
	fftw_plan p;

	in = (double*) malloc( sizeof( double ) * ( CHUNK / 2 ) );
	out = (fftw_complex*) fftw_malloc( sizeof( fftw_complex ) * ( CHUNK / 2 ) );

	if ( buffer != NULL ) {
		int i;
		for ( i = 0; i < CHUNK / 2; i++ ) {
			in[ i ] = (double) buffer[ i ];
		}
	}

	p = fftw_plan_dft_r2c_1d( CHUNK / 2, in, out, 0 );

	fftw_execute(p);
	fftw_destroy_plan(p);

	if (out != NULL) {
		int i;

		for ( i = 0; i < CHUNK / 4 + 1; i++ ) {
			magnitude[ i ] = (double) sqrt( pow( out[ i ][ 0 ], 2 ) + pow( out[ i ][ 1 ], 2 ) ) /  (double)fft_max[ i ];
			if ( magnitude[ i ] > 1.0 ) {
				magnitude[ i ] = 1.0;
			}
		}
	}

	free(in);
	fftw_free(out);
}

int freqToIndex(int freq) {
	// special case: freq is lower than the bandwidth of spectrum[0]
	if ( freq < bandwidth/2.0f ) return 0;
	// special case: freq is within the bandwidth of spectrum[512]
	if ( freq > SAMPLE_RATE/2.0f - bandwidth/2.0f ) return CHUNK/4;
	// all other cases
	double fraction = (double)freq/(double)SAMPLE_RATE;
	int i = round((CHUNK/2) * fraction);
	return i;
}

int main(int argc, char const *argv[]) {

	int i, j;

	// this code senses Ctrl+C, and turns off the Unicorn Hat LEDs when pressed
	struct sigaction sa;
	memset(&sa, 0, sizeof(sa));
	sa.sa_handler = unicorn_exit;
	sigaction(SIGINT, &sa, NULL);
	//setvbuf(stdout, NULL, _IONBF, 0);

	// unicorn init
	if (board_info_init() < 0) {
		return -1;
	}
	if (ws2811_init(&unicorn)) {
		return -1;
	}
	clearLED();
	setBrightness(15);

	int n = 0; // result from read()

	unsigned int c = 0;


	while ((n = read(STDIN_FILENO, buffer, CHUNK)) > 0) {

		// do the magic, fill 'magnitude' with the frequency-domain from 'buffer' time-domain
		getFFT();

		// code from http://code.compartmental.net/2007/03/21/fft-averages/
		// go check it out!

		// go through each band
		for (i = 0; i < 12; i++) {
			double avg = 0.0;
			int lowFreq;
			if (i == 0) {
				lowFreq = 0;
			}
			else {
				lowFreq = ((SAMPLE_RATE/2) / pow(2, 12 - i));
			}
			int hiFreq = (int)((SAMPLE_RATE/2) / pow(2, 11 - i));
			int lowBound = freqToIndex(lowFreq);
			int hiBound = freqToIndex(hiFreq);
			for (j = lowBound; j <= hiBound; j++) {
				avg += magnitude[j];
			}
			avg /= (double)(hiBound - lowBound + 1);

			bands[i] = avg;
		}

		// convert the 12 bands to 8 bins/bars (Unicorn Hat have a 8x8 LED matrix)
		bins[0] = (bands[0] + bands[1] + bands[2] + bands[3])/4.0;
		bins[1] = bands[4];
		bins[2] = bands[5];
		bins[3] = bands[6];
		bins[4] = bands[7];
		bins[5] = bands[8];
		bins[6] = bands[9];
		bins[7] = (bands[10] + bands[11]) / 2.5;

		for (i = 0; i < BINS; i++) {

			double avg = bins[i];

			if (avg > smoothbins[i]) {
				smoothbins[i] = avg;
			}

			double value = smoothbins[i];

			// increase the value for each bar, looks better. Not sure how to improve the scale though
			value *= 2.0;

			if (value > 1.0) {
				value = 1.0;
			}

			float r, g, b;
			hsv2rgb(hues[i]/360.0, 1.0, 1.0, &r, &g, &b);
			ledbar(i, value, r, g, b);

			smoothbins[i] *= 0.97;

			if (c % 8 == 0) {
				char fill[18];
				sprintf(fill, "%0*d", (int)fmin(avg*20, 10), 0);
				//printf("|%-10s", fill);
			}

		}

		showLED();

		if (c % 8 == 0) {
			//printf("|\n");
			//fflush(stdout);
		}

		c++;
	}

	unicorn_exit(0);

	return 0;
}
