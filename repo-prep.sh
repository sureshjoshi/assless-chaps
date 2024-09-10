#! /bin/bash

mkdir -p tools
wget https://github.com/a-scie/lift/releases/download/v0.7.0/science-fat-macos-aarch64 -O ./tools/science
chmod +x ./tools/science

wget https://github.com/pantsbuild/pants/releases/download/release_2.21.0/pants.2.21.0-cp39-darwin_arm64.pex -O ./releases/2.21.0/pants.2.21.0-cp39-darwin_arm64.pex
wget https://github.com/pantsbuild/pants/releases/download/release_2.22.0/pants.2.22.0-cp39-darwin_arm64.pex -O ./releases/2.22.0/pants.2.22.0-cp39-darwin_arm64.pex

pushd releases/2.21.0
../../tools/science lift build ./lift.toml
popd

pushd releases/2.22.0
../../tools/science lift build ./lift.toml
popd

./tools/science lift build ./lift.toml
