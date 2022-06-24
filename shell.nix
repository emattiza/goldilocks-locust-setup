{ pkgs ? import <nixpkgs> {}, ...}:
let 
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix";
    ref = "refs/tags/3.5.0";
  }) {
    # optionally bring your own nixpkgs
    pkgs = import <nixpkgs> {};

    # optionally specify the python version
    python = "python39";

    # optionally update pypi data revision from https://github.com/DavHau/pypi-deps-db
    # pypiDataRev = "some_revision";
    # pypiDataSha256 = "some_sha256";
  };
  pythonEnv = mach-nix.mkPython { requirements = builtins.readFile ./requirements.txt ; };
in
pkgs.mkShell {
  buildInputs = with pkgs; [
    awscli2
    curl
    httpie
    k9s
    kubernetes-helm
    kubectl
    kubectx
    rancher
    gitFull
    pythonEnv
    subversion
  ];
}
