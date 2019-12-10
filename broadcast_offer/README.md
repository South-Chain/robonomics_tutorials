# Broadcast Offer Example

This is a simple example of sending an offer message to the network

Take a look at [messages specification](https://aira.readthedocs.io/en/latest/specs/market_messages.html)

## Try it out

Before running the script make sure `robonomics_comm` is up and running. To send a predefined message run:

```
nix-shell
python main.py
```

`nix-shell` helps you enter a virtual environment with necessary dependencies.

You can change `test_offer_mainnet.yaml` file accordingly to your needs and run:

```
python main.py test_offer_mainnet.yaml
```

