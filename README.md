# web-app-deployment-cloudbuild
Use to deploy source code on using cicd 
fg

This is the sample GKE CI/CD Pipeline which does following

1) As soon as code is pushed to the repo it will trigger the cloud build in -cloud-studio-369512 project
2) it will create the docker image and k8 manifest file and push it to another GKE repo - https://github.com/mayurkasliwal/web-app-manifests
3) this manifest will be deployed to k8.

****
1) if not already present -create the cloud build trigger for this repo 
2) it uses the secret manager 
