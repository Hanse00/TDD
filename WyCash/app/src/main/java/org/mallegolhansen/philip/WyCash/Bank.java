package org.mallegolhansen.philip.WyCash;

public class Bank {
    Money reduce(Expression source, String to) {
        return source.reduce(to);
    }
}
