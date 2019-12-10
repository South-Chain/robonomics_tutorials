let
  nixpkgs = import <nixos> {};
  inherit (nixpkgs) stdenv pkgs mkRosPackage python3Packages;

  trader_pkg = mkRosPackage rec {
    name = "${pname}-${version}";
    pname = "trader_acl_pkg";
    version = "master";

    src = ./.;

    propagatedBuildInputs = [ pkgs.robonomics_comm python3Packages.pyyaml ];

    meta = with stdenv.lib; {
      description = "Robonomics Trader with ACL";
      homepage = http://github.com/airalab/;
      license = licenses.bsd3;
      maintainers = with maintainers; [ vourhey ];
    };
  };

in trader_pkg

