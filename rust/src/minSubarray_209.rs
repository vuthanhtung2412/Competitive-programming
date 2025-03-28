pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
    use std::cmp::min;
    let mut res = 100_001;
    let (mut l, mut r) = (0, 1);
    let mut curr = *nums.first().unwrap();
    while r < nums.len() {
        if curr >= target {
            res = min(res, r - l);
            curr -= *nums.get(l).unwrap();
            l += 1;
            continue;
        }
        if l == r {
            curr += *nums.get(r).unwrap();
            r += 1;
            continue;
        }
        if curr < target {
            curr += *nums.get(r).unwrap();
            r += 1;
            continue;
        }
    }
    while l < nums.len() {
        if curr >= target {
            res = min(res, r - l);
            curr -= *nums.get(l).unwrap();
            l += 1;
            continue;
        }
        if curr < target {
            break;
        }
    }
    if res == 100_001 {
        return 0;
    }
    res as i32
}

#[cfg(test)]
mod tests {
    use crate::minSubarray_209::min_sub_array_len;

    #[test]
    fn test1() {
        assert_eq!(min_sub_array_len(7, [2, 3, 1, 2, 4, 3].to_vec()), 2);
    }

    #[test]
    fn test2() {
        assert_eq!(min_sub_array_len(4, [1, 4, 4].to_vec()), 1);
    }

    #[test]
    fn test3() {
        assert_eq!(min_sub_array_len(11, [1, 4, 4].to_vec()), 0);
    }

    #[test]
    fn test4() {
        assert_eq!(min_sub_array_len(11, [1, 2, 3, 4, 5].to_vec()), 3);
    }

    #[test]
    fn test5() {
        assert_eq!(min_sub_array_len(15, [5,1,3,5,10,7,4,9,2,8].to_vec()), 2);
    }
}
