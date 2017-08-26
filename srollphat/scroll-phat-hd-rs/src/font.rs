use std::collections::HashMap;

use shared::*;

fn make_glyph(v: [&'static str; 7]) -> Glyph {
    let width = v[0].len();
    let mut glyph = vec![];
    for _ in 0..width {
        glyph.push(EMPTY_COLUMN);
    }
    for y in 0..v.len() {
        let row = v[y];
        for x in 0..row.len() {
            let c = row.chars().nth(x).unwrap();
            glyph[x][y] = if c == ' ' { 0x00 } else { 0x0F };
        }
    }
    glyph
}

#[cfg_attr(rustfmt, rustfmt_skip)]
pub fn font() -> HashMap<char, Glyph> {
    let mut glyphs = HashMap::new();
    glyphs.insert(' ', make_glyph([
                  " " ,
                  " ",
                  " ",
                  " ",
                  " ",
                  " ",
                  " "]));
    glyphs.insert('.', make_glyph([
                  " " ,
                  " ",
                  " ",
                  " ",
                  " ",
                  " ",
                  "x"]));
    glyphs.insert('!', make_glyph([
                  " " ,
                  "x",
                  "x",
                  "x",
                  "x",
                  " ",
                  "x"]));
    glyphs.insert(',', make_glyph([
                  " " ,
                  " ",
                  " ",
                  " ",
                  " ",
                  "x",
                  "x"]));
    glyphs.insert('-', make_glyph([
                  "   " ,
                  "   ",
                  "   ",
                  "xxx",
                  "   ",
                  "   ",
                  "   "]));
    glyphs.insert('_', make_glyph([
                  "   " ,
                  "   ",
                  "   ",
                  "   ",
                  "   ",
                  "   ",
                  "xxx"]));
    glyphs.insert('+', make_glyph([
                  "   " ,
                  "   ",
                  " x ",
                  "xxx",
                  " x ",
                  "   ",
                  "   "]));
    glyphs.insert('=', make_glyph([
                  "   " ,
                  "   ",
                  "xxx",
                  "   ",
                  "xxx",
                  "   ",
                  "   "]));
    glyphs.insert('0', make_glyph([
                  "    " ,
                  " xx ",
                  "x  x",
                  "x xx",
                  "xx x",
                  "x  x",
                  " xx "]));
    glyphs.insert('1', make_glyph([
                  "   " ,
                  " x ",
                  "xx ",
                  " x ",
                  " x ",
                  " x ",
                  "xxx"]));
    glyphs.insert('2', make_glyph([
                  "    " ,
                  "xxx ",
                  "   x",
                  "  x ",
                  " x  ",
                  "x   ",
                  "xxxx"]));
    glyphs.insert('3', make_glyph([
                  "    " ,
                  "xxx ",
                  "   x",
                  " xx ",
                  "   x",
                  "   x",
                  "xxx "]));
    glyphs.insert('4', make_glyph([
                  "    " ,
                  "   x",
                  "  x ",
                  " x  ",
                  "x  x",
                  "xxxx",
                  "   x"]));
    glyphs.insert('5', make_glyph([
                  "    " ,
                  "xxxx",
                  "x   ",
                  "xxx ",
                  "   x",
                  "   x",
                  "xxx "]));
    glyphs.insert('6', make_glyph([
                  "    " ,
                  " xxx",
                  "x   ",
                  "xxx ",
                  "x  x",
                  "x  x",
                  " xx "]));
    glyphs.insert('7', make_glyph([
                  "    " ,
                  "xxxx",
                  "   x",
                  "  x ",
                  " x  ",
                  "x   ",
                  "x   "]));
    glyphs.insert('8', make_glyph([
                  "    " ,
                  " xx ",
                  "x  x",
                  " xx ",
                  "x  x",
                  "x  x",
                  " xx "]));
    glyphs.insert('9', make_glyph([
                  "    " ,
                  " xx ",
                  "x  x",
                  " xxx",
                  "   x",
                  "   x",
                  " xx "]));
    glyphs.insert('A', make_glyph([
                  "    " ,
                  " xx ",
                  "x  x",
                  "x  x",
                  "xxxx",
                  "x  x",
                  "x  x"]));
    glyphs.insert('B', make_glyph([
                  "    " ,
                  "xxx ",
                  "x  x",
                  "xxx ",
                  "x  x",
                  "x  x",
                  "xxx "]));
    glyphs.insert('C', make_glyph([
                  "    " ,
                  " xxx",
                  "x   ",
                  "x   ",
                  "x   ",
                  "x   ",
                  " xxx"]));
    glyphs.insert('D', make_glyph([
                  "    " ,
                  "xxx ",
                  "x  x",
                  "x  x",
                  "x  x",
                  "x  x",
                  "xxx "]));
    glyphs.insert('E', make_glyph([
                  "    " ,
                  "xxxx",
                  "x   ",
                  "xxx ",
                  "x   ",
                  "x   ",
                  "xxxx"]));
    glyphs.insert('F', make_glyph([
                  "    " ,
                  "xxxx",
                  "x   ",
                  "xxx ",
                  "x   ",
                  "x   ",
                  "x   "]));
    glyphs.insert('G', make_glyph([
                  "    " ,
                  " xxx",
                  "x   ",
                  "x   ",
                  "x xx",
                  "x  x",
                  " xxx"]));
    glyphs.insert('H', make_glyph([
                  "    " ,
                  "x  x",
                  "x  x",
                  "xxxx",
                  "x  x",
                  "x  x",
                  "x  x"]));
    glyphs.insert('I', make_glyph([
                  " " ,
                  "x",
                  "x",
                  "x",
                  "x",
                  "x",
                  "x"]));
    glyphs.insert('J', make_glyph([
                  "    " ,
                  "   x",
                  "   x",
                  "   x",
                  "   x",
                  "x  x",
                  " xx "]));
    glyphs.insert('K', make_glyph([
                  "    " ,
                  "x  x",
                  "x x ",
                  "xx  ",
                  "x x ",
                  "x  x",
                  "x  x"]));
    glyphs.insert('L', make_glyph([
                  "   " ,
                  "x  ",
                  "x  ",
                  "x  ",
                  "x  ",
                  "x  ",
                  "xxx"]));
    glyphs.insert('M', make_glyph([
                  "     " ,
                  "x   x",
                  "xx xx",
                  "x x x",
                  "x   x",
                  "x   x",
                  "x   x"]));
    glyphs.insert('N', make_glyph([
                  "    " ,
                  "x  x",
                  "xx x",
                  "x xx",
                  "x  x",
                  "x  x",
                  "x  x"]));
    glyphs.insert('O', make_glyph([
                  "    " ,
                  " xx ",
                  "x  x",
                  "x  x",
                  "x  x",
                  "x  x",
                  " xx "]));
    glyphs.insert('P', make_glyph([
                  "    " ,
                  "xxx ",
                  "x  x",
                  "xxx ",
                  "x   ",
                  "x   ",
                  "x   "]));
    glyphs.insert('Q', make_glyph([
                  "     " ,
                  " xx  ",
                  "x  x ",
                  "x  x ",
                  "x  x ",
                  "x xx ",
                  " xx x"]));
    glyphs.insert('R', make_glyph([
                  "     " ,
                  "xxx  ",
                  "x  x ",
                  "xxx  ",
                  "x  x ",
                  "x  x ",
                  "x  x "]));
    glyphs.insert('S', make_glyph([
                  "    " ,
                  " xxx",
                  "x   ",
                  " xx ",
                  "   x",
                  "   x",
                  "xxx "]));
    glyphs.insert('T', make_glyph([
                  "     " ,
                  "xxxxx",
                  "  x  ",
                  "  x  ",
                  "  x  ",
                  "  x  ",
                  "  x  "]));
    glyphs.insert('U', make_glyph([
                  "    " ,
                  "x  x",
                  "x  x",
                  "x  x",
                  "x  x",
                  "x  x",
                  " xx "]));
    glyphs.insert('V', make_glyph([
                  "     " ,
                  "x   x",
                  "x   x",
                  "x   x",
                  "x   x",
                  " x x ",
                  "  x  "]));
    glyphs.insert('W', make_glyph([
                  "     " ,
                  "x   x",
                  "x   x",
                  "x   x",
                  "x x x",
                  "x x x",
                  " x x "]));
    glyphs.insert('X', make_glyph([
                  "     " ,
                  "x   x",
                  " x x ",
                  "  x  ",
                  " x x ",
                  "x   x",
                  "x   x"]));
    glyphs.insert('Y', make_glyph([
                  "     " ,
                  "x   x",
                  " x x ",
                  "  x  ",
                  "  x  ",
                  "  x  ",
                  "  x  "]));
    glyphs.insert('Z', make_glyph([
                  "    " ,
                  "xxxx",
                  "   x",
                  "  x ",
                  " x  ",
                  "x   ",
                  "xxxx"]));
    glyphs
}
