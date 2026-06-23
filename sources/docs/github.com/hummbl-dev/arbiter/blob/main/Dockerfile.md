# Source: https://github.com/hummbl-dev/arbiter/blob/main/Dockerfile

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# Dockerfile

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/Dockerfile)

History

14 lines (9 loc) · 357 Bytes

 main

/

# Dockerfile

Copy path

Top

## File metadata and controls

- Code
 
- Blame
 

14 lines (9 loc) · 357 Bytes

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/Dockerfile)

Copy raw file

Download raw file

Open symbols panel

Edit and raw actions

1

2

3

4

5

6

7

8

9

10

11

12

13

14

FROM python:3.12-slim

# Install git (needed for git historian) and analysis tools

RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/\*

COPY . /app/

WORKDIR /app

# Install Arbiter + analysis tools via pip

RUN pip install --no-cache-dir ".\[analyzers\]"

EXPOSE 8080

CMD \["arbiter", "serve", "--port", "8080"\]