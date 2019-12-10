# Trader Example

Now we are ready to bring some automation to deal with offers and demands.

This example contains the simplest trader node which waits for a demand message and replies with a corresponding offer one.

It's a good practice to have a `robonomics/` folder where you keep `model.txt` file. An IPFS hash of the file is your agent's model

## Build

```
nix build
```

## Launch

There is one required parameter - model. Basically it's unique identifier

```
source result/setup.bash
rosrun trader_pkg trader.py _model:=QmXvW32SiSESvoRmndc6sJmMDEQ4bWVpaMpa8NFuGakBCA
```

