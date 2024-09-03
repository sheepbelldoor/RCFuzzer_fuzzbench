# RCFuzzer


### Build docker image
We have built the docker image for you, but you want to build it by yourself; here is the process.

First build baseline fuzzers and benchmarks.

```
./docker/build.sh
```

Then, build the all-in-one docker including `autofz` and all the fuzzers/benchmarks.

```
./build.sh
```

You can tune the image name/tag in these `build.sh`.

You might need to tune `_UID` and `GID` (they are hard-coded to `2000` when building the pre-built image) in `build.sh` to bypass docker volume permission issue if you don't want to use root user.

