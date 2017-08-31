'use strict';

class Converter {
	static hsv2rgb(hue, saturation, value) {
		if (hue === undefined) { return [0, 0, 0]; }

		const chroma = (value / 100) * (saturation / 100);
		const prime = hue / 60;
		const sc = chroma * (1 - Math.abs(prime % 2 - 1));
		const adjustment = (value / 100) - chroma;

		const pprime = parseInt(prime, 10);
		const rgb = (
			pprime === 0 ? [chroma, sc, 0] :
			pprime === 1 ? [sc, chroma, 0] :
			pprime === 2 ? [0, chroma, sc] :
			pprime === 3 ? [0, sc, chroma] :
			pprime === 4 ? [sc, 0, chroma] :
			pprime === 5 ? [chroma, 0, sc] :
			[0,0,0]
		);

		return [
			Math.round(255 * (rgb[0] + adjustment)),
			Math.round(255 * (rgb[1] + adjustment)),
			Math.round(255 * (rgb[2] + adjustment))
		];

	}

	static hsl2rgb(hue, saturation, lightness) {
		if (hue === undefined) { return [0, 0, 0]; }

		const chroma = (1 - Math.abs((2 * (lightness / 100)) - 1)) * (saturation / 100);
		const prime = hue / 60;
		const sc = chroma * (1 - Math.abs(prime % 2 - 1));
		const adjustment = (lightness / 100) - (chroma / 2);

		const pprime = parseInt(prime, 10);
		const rgb = (
			pprime === 0 ? [chroma, sc, 0] :
			pprime === 1 ? [sc, chroma, 0] :
			pprime === 2 ? [0, chroma, sc] :
			pprime === 3 ? [0, sc, chroma] :
			pprime === 4 ? [sc, 0, chroma] :
			pprime === 5 ? [chroma, 0, sc] :
			[0,0,0]
		);

		return [
			Math.round(255 * (rgb[0] + adjustment)),
			Math.round(255 * (rgb[1] + adjustment)),
			Math.round(255 * (rgb[2] + adjustment))
		];
	}
}

module.exports = Converter;