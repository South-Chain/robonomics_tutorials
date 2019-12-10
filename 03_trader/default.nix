let
  nixpkgs = import <nixos> {};
  inherit (nixpkgs) stdenv pkgs mkRosPackage;

  trader_pkg = mkRosPackage rec {
    name = "${pname}-${version}";
    pname = "trader_pkg";
    version = "master";

    src = ./.;

    propagatedBuildInputs = [ pkgs.robonomics_comm ];

    meta = with stdenv.lib; {
      description = "Your first Robonomics Trader";
      homepage = http://github.com/airalab/;
      license = licenses.bsd3;
      maintainers = with maintainers; [ vourhey ];
    };
  };

in trader_pkg

