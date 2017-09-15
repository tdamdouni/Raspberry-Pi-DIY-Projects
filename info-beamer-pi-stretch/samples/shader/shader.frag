uniform sampler2D Texture;
uniform float Effect;
varying vec2 TexCoord;

void main() {
    float force = Effect * (0.5- min(0.5, distance(TexCoord.st, vec2(0.5, 0.5))));
    float x = sin(force*2.0)/5.0 * force;
    float y = cos(force*2.0)/5.0 * force;
    vec4 color = texture2D(Texture, TexCoord.st + vec2(x, y));
    gl_FragColor = vec4(
        color[1] + force/2.0,
        color[2] - force/2.0,
        color[3] - force/2.0,
        color[3]
    );
}
