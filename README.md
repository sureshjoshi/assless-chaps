# assless-chaps

Yes, it's a tautology, but it still sounds funny.

## What is this?

Just a proof-of-concept of the baseline functionality of [scie-pants](https://github.com/pantsbuild/scie-pants), missing several obvious features, with significantly less code.

The goal here is to see if the current [scie-pants](https://github.com/pantsbuild/scie-pants) repo could be mostly replaced with a thin runner and pre-packaging Pants as a scie, instead of a pex. This comes with some benefits:

- Pants' Python version is defined in a `lift.toml`, instead of needing to update `scie-pants` to support new Python versions
- Pants GitHub releases are immediately downloadable/usable for those people (me) who don't like multiple levels of indirection in stuff that runs on their machines
- We could build a "fat" Pants, which comes packed with the interpreter (and ideally everything else it needs to run) for no-network CI
- Reduced `scie-pants` code, means smaller surface for supply chain attacks, and fewer dependencies to update

N.B. This example is a straight-line path, there was no attempt to investigate backwards compatibility, performance, or even to put in the legwork of setting up on-the-fly Pants downloads, as that would miss the point of this prototype.

## Getting started

- Run `python3 generate-scie-releases.py` to download the `science` tool, as well as download the last 5 Pants pex releases and turn them into scies
- Run `cargo build --release` in the `pants-runner` directory
- Run `./pants-runner/target/release/pants-runner --version` in the root directory
- Update `pants.toml` and re-try

## Performance

There has been no effort in tuning or debugging start-up performance.

The most I can say is that it seems to be slower than running `time pants --version` in this same repo. That is approximately 150ms, while running `time ./pants-runner/target/release/pants-runner --version` is closer to 750ms.

Why? Don't know, don't care - yet.
