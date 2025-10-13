package org.mallegolhansen.philip.WyCash;

public class Money {
    protected int amount;

    public boolean equals(Object object) {
        Money other = (Money) object;
        return amount == other.amount && getClass() == other.getClass();
    }
}
