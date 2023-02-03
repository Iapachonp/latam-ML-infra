terraform {
  backend "gcs" {
    bucket = "tf-state-prod-a16a0eed-a739-4ff1-b44f-b5a95d54f4df"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = "latam-poc-prod"
  region  = "us-east1"
}
