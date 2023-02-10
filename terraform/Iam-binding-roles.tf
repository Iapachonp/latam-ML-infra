resource "google_service_account_iam_binding" "cloudrun-account-iam" {
  service_account_id = google_service_account.latam-ml-service-sa.id
  role               = "roles/iam.serviceAccountUser"

}
