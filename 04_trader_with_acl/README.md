# Trader with ACL Example

Sometimes we want to restrict some users of using our service. There is a simple pattern of using an access control list (ACL).
Basically the ACL contains a list of address which are allowed to work with a service.

This example extends our previous trader and adds an ACL in YAML format. Take a look at `robonomics/acl.yaml`

The only difference is at initialization the trader loads the list of addresses and then at every incoming demand message it checks not only the model but also whether a sender is in the list or not.

## Build

```
nix build
```

## Launch

Notice that you must provide the model and the path to an ACL file

```
source result/setup.bash
rosrun trader_acl_pkg trader.py _model:=QmZDYSkbpBSBZ1SzTMe8MR5WCWJPmkFo9qjx1CzzLxXPSk _acl:=./robonomics/acl.yaml
```

