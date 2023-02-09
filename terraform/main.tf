terraform {
  backend "gcs" {
    bucket = "tf-state-prod-a16a0eed-a739-4ff1-b44f-b5a95d54f4df2"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = "aa-study"
  region  = "us-east1"
}
