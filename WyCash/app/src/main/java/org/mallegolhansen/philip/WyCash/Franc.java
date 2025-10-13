package org.mallegolhansen.philip.WyCash;

public class Franc extends Money {
    Franc(int amount, String currency) {
        super(amount, currency);
    }

    Money times(int multiplier) {
        return Money.franc(amount * multiplier);
    }
}

