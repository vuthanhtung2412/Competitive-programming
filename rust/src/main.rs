fn main() {
}

fn iter_rev() {
    let vec = vec![10, 20, 30, 40, 50];
    // Iterating in reverse with index
    for (index, &item) in vec.iter().enumerate().rev() {
        println!("Index: {}, Item: {}", index, item);
    }
}
