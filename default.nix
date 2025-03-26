{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python39
    pkgs.postgresql_16
    pkgs.gcc
    pkgs.doc
  ];

  # Example of a problematic package reference
  # src = fetchurl {
  #   url = "http://example.com/invalid-url.tar.gz";
  #   sha256 = "0v1h1k1...";
  # };

  # Update the URL to a valid one
  src = fetchurl {
    url = "http://example.com/valid-url.tar.gz";
    sha256 = "0v1h1k1...";
  };
}
