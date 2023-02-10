resource "google_artifact_registry_repository" "latam-repo" {
  location      = "us-central1"
  repository_id = "latam-repo"
  description   = "latam docker repository"
  format        = "DOCKER"
}
