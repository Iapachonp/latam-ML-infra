
resource "google_storage_bucket" "static-site" {
  name          = "ml-latam-3F89841D-5689-4FFC-ABED-807239371CA6" # weird name due to uniqueness of bucket name
  location      = "EU"
  force_destroy = true
}


