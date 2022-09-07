

resource "cloudflare_record" "test" {
  zone_id    = var.zone_id
  name       = "test"
  value      = aws_eip.eip.public_dns
  type       = "CNAME"
  ttl        = 1
  proxied    = true
  depends_on = [aws_instance.public]
}
resource "cloudflare_record" "first" {
  zone_id    = var.zone_id
  name       = "first"
  value      = aws_eip.eip.public_dns
  type       = "CNAME"
  ttl        = 1
  proxied    = true
  depends_on = [aws_instance.public]
}