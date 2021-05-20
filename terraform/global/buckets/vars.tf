variable "region" {
  description = "Region"
  type = string
  default = "us-east-1"
  }

variable "terraform-state" {
  description = "Name of the TFState Bucket"
  type = string
  default = "jaysons-fancy-terraform-state"
  }

variable "files-bucket" {
  description = "Name of the files bucket"
  type = string
  default = "jaysons-files-bucket"
  }