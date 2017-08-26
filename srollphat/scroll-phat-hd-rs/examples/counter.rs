extern crate scroll_phat_hd;

use scroll_phat_hd::display::*;
use scroll_phat_hd::scroller::*;

fn main() {
    println!("start");

    // let mut display = I2CDisplay::new(1);
    let mut display = TermDisplay::new();
    let mut scroller = Scroller::new(&mut display);

    for i in 0..3000 {
        let v = format!("{}", i);
        scroller.set_text(&v);
        scroller.show();
        std::thread::sleep(std::time::Duration::from_millis(100));
    }

    println!("end");
}
