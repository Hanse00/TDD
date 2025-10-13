package org.mallegolhansen.philip.WyCash;

public abstract class Money {
    protected int amount;

    static Money dollar(int amount) {
        return new Dollar(amount);
    }

    abstract Money times(int multiplier);

    public boolean equals(Object object) {
        Money other = (Money) object;
        return amount == other.amount && getClass() == other.getClass();
    }
}
