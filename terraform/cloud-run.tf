# resource "google_cloud_run_service" "Latam_ML_service" {
#  name     = "latam-ml-service"
# location = "us-east1"
#
# template {
#   spec {
#     containers {
#       image = "us-docker.pkg.dev/iapachonp/latam-ml-api"
#     }
#   }
# }

# traffic {
#   percent         = 100
#   latest_revision = true
# }
# }
