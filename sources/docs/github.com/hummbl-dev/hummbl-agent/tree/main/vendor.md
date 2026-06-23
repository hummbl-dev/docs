# Source: https://github.com/hummbl-dev/hummbl-agent/tree/main/vendor

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

## FilesExpand file tree

 main

/

# vendor

/

Copy path

## Directory actions

## More options

More options

## Directory actions

## More options

More options

## Latest commit

## History

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/vendor)

History

 main

/

# vendor

/

Copy path

Top

## Folders and files

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

### parent directory

[..](https://github.com/hummbl-dev/hummbl-agent/tree/main) |
| 

[README.md](https://github.com/hummbl-dev/hummbl-agent/blob/main/vendor/README.md 'README.md')

 | 

[README.md](https://github.com/hummbl-dev/hummbl-agent/blob/main/vendor/README.md 'README.md')

 | 

 | 

 |
| 

[UPSTREAM\_PINS.md](https://github.com/hummbl-dev/hummbl-agent/blob/main/vendor/UPSTREAM_PINS.md 'UPSTREAM_PINS.md')

 | 

[UPSTREAM\_PINS.md](https://github.com/hummbl-dev/hummbl-agent/blob/main/vendor/UPSTREAM_PINS.md 'UPSTREAM_PINS.md')

 | 

 | 

 |
| 

View all files

 |

## [README.md](https://github.com/#readme)

Outline

# VENDOR

## Purpose

Upstream mirrors pinned by commit for reproducible integration.

## Update Procedure

- Use `scripts/sync-upstreams.sh` only.
- Do not edit `vendor/*` directly (except this README and `vendor/UPSTREAM_PINS.md`). Pins are commit SHAs; branch names are not accepted as pins.
- Do not record `unknown` pins. If a configured upstream cannot be resolved to a commit SHA, keep it out of `vendor/UPSTREAM_PINS.md` and record it as a retired unresolved upstream.

## Add a New Upstream

1. Add the upstream entry to `scripts/sync-upstreams.sh`.
2. Run `./scripts/sync-upstreams.sh init` and execute the printed commands.
3. Record the pin in `vendor/UPSTREAM_PINS.md` (the script will update it).

## No-Edit Rule

No edits inside `vendor/*` except `vendor/README.md` and `vendor/UPSTREAM_PINS.md`.