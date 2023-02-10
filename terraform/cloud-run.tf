resource "google_cloud_run_service" "Latam_ML_service" {
  name     = "Latam_ML_service"
  location = "us-east1"

  template {
    spec {
      containers {
        image = "us-docker.pkg.dev/iapachonp/latam-ml-api"
      }
      service_account_name = google_service_account.latam-ml-service-sa.id
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}
