package org.mallegolhansen.philip.WyCash;

public class Dollar extends Money {

    Dollar(int amount) {
        this.amount = amount;
    }

    Dollar times(int multiplier) {
        return new Dollar(amount * multiplier);
    }

    public boolean equals(Object object) {
        Dollar other = (Dollar) object;
        return amount == ((Dollar) object).amount;
    }
}
