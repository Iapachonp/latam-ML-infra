resource "google_service_account" "latam-ml-service-sa" {
  account_id   = "latam-ml-service-sa"
  display_name = "Service Account for Ml service"
}
