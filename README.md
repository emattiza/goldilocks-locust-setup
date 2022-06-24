# Locust and Goldilocks

This repo has a sample setup for load-testing kubernetes deployments using VPA and Goldilocks.

Nix is in here that will make your life easier, just `nix-shell`, including installing python and libs.

## Steps

1. Helm install VPA to K8s under test
1. Helm install Goldilocks to K8s under test
1. Ensure deployment replicas of 1 pod
1. Author a locust file with a useful load pattern
1. run `locust` in the locustfile directory
1. navigate to the new locust server and point at system of your choice
1. Port forward and navigate to goldilocks 
1. monitor your recommendations


See [This video](https://www.youtube.com/watch?v=DfmQWYiwFDk)
