use nix::unistd::execv;
use std::ffi::CString;
use std::{env, fs};

// TODO: This only works in the root directory (with the pants.toml)

fn main() {
    let toml_str = fs::read_to_string("pants.toml").expect("Cannot find pants.toml");

    let version = toml_str
        .lines()
        .find(|line| line.starts_with("pants_version"))
        .map(|line| line.split("=").map(|l| l.trim().trim_matches('"')).last())
        .flatten()
        .expect("There was no valid pants_version");

    // TODO: Download the release, or check cache if it's already there
    // This example just keeps them in the "releases" directory to keep the prototype concept simple

    // TODO: Be smarter about figuring out which arch/filename
    let scie_path = CString::new(format!(
        "releases/{version}/pants.{version}-cp311-darwin_arm64.scie"
    ))
    .expect("Unable to create CString from release path");

    let c_args: Vec<CString> = env::args()
        .map(|arg| CString::new(arg).expect("Unable to create CString from String"))
        .collect();

    // Replace the current process (ignoring errors)
    // TODO: Env vars and whatever else that matters, and b
    let _ = execv(&scie_path, &c_args);
}
