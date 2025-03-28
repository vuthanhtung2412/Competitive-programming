use std::panic;

pub fn calculate(s: String) -> i32 {
    use std::collections::HashSet;

    #[derive(Debug)]
    enum Symbol {
        Value(i32),
        Minus,
        Plus,
        Start,
        End,
    }

    let operators = HashSet::from(['+', '-']);
    let scopes = HashSet::from(['(', ')']);
    let digits = HashSet::from(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']);
    let mut stack: Vec<Symbol> = Vec::new();
    for c in s.chars() {
        if c == ' ' {
            continue;
        }
        // Current char is a digit
        if let Some(d) = digits.get(&c) {
            match stack.last_mut() {
                None => {
                    stack.push(Symbol::Value(c.to_digit(10).unwrap() as i32));
                    continue;
                }
                Some(symbol) => match symbol {
                    Symbol::Value(val) => *val = *val * 10 + c.to_digit(10).unwrap() as i32,
                    Symbol::Start | Symbol::Minus | Symbol::Plus => {
                        stack.push(Symbol::Value(c.to_digit(10).unwrap() as i32));
                    }
                    Symbol::End => {
                        panic!("digit after scope end")
                    }
                },
            }
            continue;
        }
        if let Some(o) = operators.get(&c) {
            match stack.last() {
                None => {
                    if *o == '-' {
                        stack.push(Symbol::Value(0));
                        stack.push(Symbol::Minus);
                        continue;
                    }
                    panic!("plus is not unary operators");
                }
                Some(symbol) => match symbol {
                    Symbol::Value(_) => {
                        if *o == '-' {
                            stack.push(Symbol::Minus);
                        } else {
                            stack.push(Symbol::Plus);
                        }
                    }
                    Symbol::Minus | Symbol::Plus => {
                        panic!("no 2 consecutive operators")
                    }
                    Symbol::End => {
                        panic!("no scope end befor opertor")
                    }
                    Symbol::Start => {
                        if *o == '-' {
                            stack.push(Symbol::Value(0));
                            stack.push(Symbol::Minus);
                        } else {
                            stack.push(Symbol::Plus);
                        }
                    }
                },
            }
            continue;
        }
        if let Some(s) = scopes.get(&c) {
            if *s == '(' {
                match stack.last() {
                    None => stack.push(Symbol::Start),
                    Some(symbol) => match symbol {
                        Symbol::Minus | Symbol::Plus | Symbol::Start => {
                            stack.push(Symbol::Start);
                        }
                        _ => panic!("( can't come after digit or )"),
                    },
                }
            } else {
                let mut start_exp_id = usize::MAX;
                for (i, s) in stack.iter().enumerate().rev() {
                    match *s {
                        Symbol::Start => {
                            start_exp_id = i;
                            break;
                        }
                        _ => continue,
                    }
                }
                let Symbol::Value(mut _eval) = *stack.get(start_exp_id + 1).unwrap() else {
                    panic!("where is the number in the scope");
                };
                let mut i = start_exp_id + 2;
                while i < stack.len() {
                    let Symbol::Value(val) = *stack.get(i + 1).unwrap() else {
                        panic!("where is my fcking number");
                    };
                    match *stack.get(i).unwrap() {
                        Symbol::Minus => _eval -= val,
                        Symbol::Plus => _eval += val,
                        _ => panic!("give me symbol bitch"),
                    }
                    i += 2;
                }
                stack.truncate(start_exp_id);
                stack.push(Symbol::Value(_eval));
            }
            continue;
        }
        panic!("Non existing char")
    }
    println!("Stack : {:?}", stack);
    let Some(Symbol::Value(mut res)) = stack.first() else {
        panic!("WTF where is my number !");
    };
    let mut i = 1;
    while i < stack.len() {
        let Symbol::Value(val) = *stack.get(i + 1).unwrap() else {
            panic!("where is my fcking number");
        };
        match *stack.get(i).unwrap() {
            Symbol::Minus => res -= val,
            Symbol::Plus => res += val,
            _ => panic!("give me symbol bitch"),
        }
        i += 2;
    }
    res
}

// pub fn calculate_w_enum(s: String) -> i32 {
//     enum Expression {
//         Value(i32),
//         Negate(Box<Expression>),
//         Plus(Box<Expression>, Box<Expression>),
//         Minus(Box<Expression>, Box<Expression>),
//     }
//     0
// }

#[cfg(test)]
mod tests {
    use crate::basicCalculator_224::calculate;

    #[test]
    fn test1() {
        assert_eq!(calculate("1 + 1".into()), 2);
    }

    #[test]
    fn test2() {
        assert_eq!(calculate(" 2-1 + 2 ".into()), 3);
    }

    #[test]
    fn test3() {
        assert_eq!(calculate("(1+(4+5+2)-3)+(6+8)".into()), 23);
    }
}
