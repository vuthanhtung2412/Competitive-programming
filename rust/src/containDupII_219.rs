pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
    use std::collections::HashMap;
    let mut m: HashMap<i32, Vec<usize>> = HashMap::new();
    for (i, n) in nums.into_iter().enumerate() {
        match m.get_mut(&n) {
            None => {
                m.insert(n, vec![i]); // Create a new entry if `n` is not found
            }
            Some(positions) => {
                for pos in positions.iter() {
                    if i - *pos <= k as usize {
                        return true;
                    }
                }
                positions.push(i); // Add `i` to the existing vector
            }
        }
    }
    false
}

#[cfg(test)]
mod tests {

    use crate::containDupII_219::contains_nearby_duplicate;
    #[test]
    fn test1() {
        assert!(contains_nearby_duplicate([1, 2, 3, 1].to_vec(), 3));
    }

    #[test]
    fn test2() {
        assert!(contains_nearby_duplicate([1, 0, 1, 1].to_vec(), 1));
    }

    #[test]
    fn test3() {
        assert!(!contains_nearby_duplicate([1, 2, 3, 1, 2, 3].to_vec(), 2));
    }
}
