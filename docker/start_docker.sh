docker run -it --rm \
  --gpus all \
  -v $(git rev-parse --show-toplevel):/work \
  -v /net/ustc_03/yangz:/data \
  -w /work \
  starp/hepynet:v0.4.1
