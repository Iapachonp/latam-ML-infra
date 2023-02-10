# resource "google_cloud_run_service" "Latam_ML_service" {
#   name     = "latam-ml-service"
#   location = "us-east1"
#
#   template {
#     spec {
#       containers {
#         image = "us-central1-docker.pkg.dev/aa-study/latam-repo/latam-ml-api:production" 
#         ports { container_port = 8000 }
#       }
#     }
#   }
#
#   traffic {
#     percent         = 100
#     latest_revision = true
#   }
# }
