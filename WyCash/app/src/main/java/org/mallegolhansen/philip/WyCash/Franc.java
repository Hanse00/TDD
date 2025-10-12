package org.mallegolhansen.philip.WyCash;

public class Franc {
    private int amount;

    Franc(int amount) {
        this.amount = amount;
    }

    Franc times(int multiplier) {
        return new Franc(amount * multiplier);
    }

    public boolean equals(Object object) {
        Franc other = (Franc) object;
        return amount == ((Franc) object).amount;
    }
}

