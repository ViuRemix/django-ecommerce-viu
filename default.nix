{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python39
    pkgs.postgresql_16
    pkgs.gcc
    pkgs.doc  # Ensure 'doc' is correct and replace 'dev' with 'doc'
  ];
}
