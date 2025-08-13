/*
====================================================================================================
VARIABLES
====================================================================================================
*/
fn foobar(x: any) {
    return;
}

fn variables() {
    let x;
    x = 5;

    let y = 3;

    // with an explicit type
    let z: i32 = 6; // signed 32bit integer
    // there's i8, i16, i32, i64, i128, also u8, u16, u32, u64, u128 for unsigned

    // you can't use a variable before it's assigned a value
    let x;
    foobar(x); // error: borrow of possibly-uninitialized variable: `x`
    x = 42;

    // okay
    let x;
    x = 42;
    foobar(x); // the type of `x` will be inferred from here

    // throw away values -> use _
    let _ = 42;

    let _ = get_thing(); // throw away return value
}

/*
====================================================================================================
FUNCTIONS
====================================================================================================
*/
fn fn_test() {
    println("Hello, World!")
}

fn main() {
    variables();
}
