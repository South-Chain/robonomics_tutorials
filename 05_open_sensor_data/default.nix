let
  nixpkgs = import <nixos> {};
  inherit (nixpkgs) stdenv pkgs mkRosPackage python3Packages;

  open_sensor_data_pkg = mkRosPackage rec {
    name = "${pname}-${version}";
    pname = "open_sensor_data_pkg";
    version = "master";

    src = ./.;

    propagatedBuildInputs = [ pkgs.robonomics_comm ];

    meta = with stdenv.lib; {
      description = "Robonomics Trader with ACL";
      homepage = http://github.com/airalab/;
      license = licenses.bsd3;
      maintainers = with maintainers; [ vourhey ];
    };
  };

in open_sensor_data_pkg

