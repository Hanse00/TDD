package org.mallegolhansen.philip.WyCash;

public class Franc extends Money {
    Franc(int amount) {
        this.amount = amount;
    }

    Money times(int multiplier) {
        return new Franc(amount * multiplier);
    }
}

