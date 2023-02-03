
resource "google_storage_bucket" "static-site" {
  name          = "ml-latam-3f89841d-5689-4ffc-abed-807239371ca6" # weird name due to uniqueness of bucket name
  location      = "EU"
  force_destroy = true
}


