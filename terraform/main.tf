terraform {
  backend "gcs" {
    bucket = "tf-state-prod"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = "latam-poc-prod"
  region  = "us-east1"
}
