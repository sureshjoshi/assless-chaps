# assless-chaps

Yes, it's a tautology, but it still sounds funny.

## What is this?

Just a proof-of-concept of the baseline functionality of [scie-pants](https://github.com/pantsbuild/scie-pants), missing several obvious features, with significantly less code.

The goal here is to see if the current `scie-pants` repo could be mostly replaced with a few small Python scripts and pre-packaging Pants as a scie, instead of a pex.

## Getting started

- Run `sh repo-prep.sh` to download the requisite files and create several `scie` files
- Run `./pants-runner.scie` to see that Pants is kicked off and emits the correct version as per `pants.toml` (for 2.21.0 or 2.22.0 as those are local)

Currently `scie-pants` launches `pants --version` in about 100ms, while this custom pex scie takes about 500ms - but there has been no effort to optimize or figure out why the installed `pex` is so much slower.
