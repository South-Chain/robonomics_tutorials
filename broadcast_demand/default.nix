let
  pkgs = import <nixos> {};
in
  pkgs.stdenv.mkDerivation {
    name = "broadcast_demand_pkg";
    src = null;
    buildInputs = [
      pkgs.robonomics_comm
      pkgs.python3Packages.pyyaml
    ];
    shellHook = ''
      . ${pkgs.robonomics_comm}/setup.bash
      echo "Welcome to your Broadcast Demand Environment"
    '';
}
