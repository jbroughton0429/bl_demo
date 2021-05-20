provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "terraform-state" {

  bucket = var.terraform-state

  force_destroy = true

  acl    = "private"

  tags = {
    Name        = "TFState"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "files-bucket" {

  bucket = var.files-bucket

  force_destroy = true
  
  acl = "private"

  tags = {
    Name = "FilesBucket"
    Environment = "Dev"
  }
}
