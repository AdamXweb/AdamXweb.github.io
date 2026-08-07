# List available commands
default:
    @just --list

# Fetch the Hugo theme submodules (one-time after clone)
[group("dev")]
setup:
    git submodule update --init --recursive

# Serve the site locally with live reload
[group("dev")]
run:
    hugo server

# Build the minified production site to ./public (matches gh-pages.yml)
[group("ship")]
build:
    hugo --minify

# Remove generated build output
[group("dev")]
clean:
    rm -rf public
