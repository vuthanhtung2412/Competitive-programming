pub fn str_str(haystack: String, needle: String) -> i32 {
    for (i, _) in haystack.chars().enumerate() {
        let Some(slice) = haystack.get(i..(i + needle.len())) else {
            return -1;
        };
        if slice == needle {
            return i as i32;
        }
    }
    -1
}

#[cfg(test)]
mod tests {
    use crate::findFirstOccurrence_28::str_str;

    #[test]
    fn test1() {
        assert_eq!(str_str(String::from("sadbutsad"), String::from("sad")), 0);
    }

    #[test]
    fn test2() {
        assert_eq!(str_str(String::from("leetcode"), String::from("leeto")), -1);
    }
}
