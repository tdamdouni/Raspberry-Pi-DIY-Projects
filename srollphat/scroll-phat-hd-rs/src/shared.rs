pub type Column = [u8; DISPLAY_HEIGHT];
pub type Glyph = Vec<Column>;

pub const EMPTY_COLUMN: Column = [0; DISPLAY_HEIGHT];

pub const DISPLAY_WIDTH: usize = 17;
pub const DISPLAY_HEIGHT: usize = 7;
