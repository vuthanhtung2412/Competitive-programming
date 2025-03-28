pub fn is_subsequence(s: String, t: String) -> bool {
    if s.is_empty() && t.is_empty(){
        return true;
    }
    let mut sp = 0;
    let mut tp = 0;
    while tp < t.len() {
        if sp == s.len() {
            return true;
        }
        if t.chars().nth(tp).unwrap() == s.chars().nth(sp).unwrap() {
            sp += 1;
            if sp == s.len() {
                return true;
            }
        }
        tp += 1;
    }
    false
}

#[cfg(test)]
mod tests {
    use crate::isSubsequence_392::is_subsequence;

    #[test]
    fn test1() {
        assert!(is_subsequence(String::from("abc"), String::from("ahbgdc")));
    }

    #[test]
    fn test2() {
        assert!(!is_subsequence(String::from("axc"), String::from("ahbgdc")),);
    }
}
