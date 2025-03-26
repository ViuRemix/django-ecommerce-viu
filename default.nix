{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python39
    pkgs.postgresql_16
    pkgs.gcc
    pkgs.doc  # Replace 'dev' with 'doc'
  ];
}
